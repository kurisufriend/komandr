from sys import path as sys_path
from os import listdir
from threading import Thread

##################################################
# TODO: THIS IS DUMB, FIGURE OUT ANOTHER WAY TO LET US DO IT WITHOUT INFRINGING ON PLUGINSPACE 
##################################################
from inspect import stack
from os.path import basename
def bprint(*args):
    print(f"[{basename(stack()[1].filename)}/{stack()[1].function}]:", *args)
##################################################

class komandr():
    def __init__(self):
        self.libs_loaded = self.load_modules_to_dict("libs")
        self.plugins_loaded = self.load_modules_to_dict("plugins")
        
        for p in self.plugins_loaded.values():
            depends_correct = True
            for d in p.depends:
                if d not in self.libs_loaded.keys(): bprint(f"{p.__name__} requires {d} library! plugin will not be started.");depends_correct = False
            if not depends_correct: continue

            Thread(target = p.run, args = (self.libs_loaded,)).start()
            bprint("started plugin", p.__name__)
    def load_modules_to_dict(self, fro):
        res = {}
        sys_path.append(sys_path[0]+f"/{fro}")
        modules = [name.split(".py")[0] for name in listdir(sys_path[-1]) if name.endswith(".py")]
        for mod in modules:
            try: temp_mod = __import__(mod)
            except: continue
            # TODO: CHECK FOR VALIDITY ACCORDING TO RULES
            res[mod] = temp_mod
            bprint(f"loaded module {mod} from {fro}")
        return res
    def run(self):
        pass