import requests
import json
class driver():
    def __init__(self, endpoin, image, static):
        self.endpoint = endpoin
        self.image_endpoint = image
        self.static_endpoint = static
        self.sess = requests.Session()
    def get_boards(self):
        return self.wrap_route("/boards.json")
    def get_threads(self, board):
        return self.wrap_route(f"/{board}/threads.json")
    def get_catalog(self, board):
        return self.wrap_route(f"/{board}/catalog.json")
    def get_archive(self, board):
        return self.wrap_route(f"/{board}/archive.json")
    def get_page(self, board, page):
        return self.wrap_route(f"/{board}/{page}.json")
    def get_thread(self, board, thread_id):
        return self.wrap_route(f"/{board}/thread/{thread_id}.json")
    def wrap_route(self, route):
        return json.loads(self.sess.get(self.endpoint+route).text)
instance = driver("https://a.4cdn.org", "https://i.4cdn.org", "https://s.4cdn.org")