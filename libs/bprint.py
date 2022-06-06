from inspect import stack
from os.path import basename
def p(*args):
    print(f"[{basename(stack()[1].filename)}/{stack()[1].function}]:", *args)