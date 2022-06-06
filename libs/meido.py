import requests
import json
class driver():
    def __init__(self, endpoin, image, static):
        self.endpoint = endpoin
        self.image_endpoint = image
        self.static_endpoint = static
    def get_boards(self):
        return self.wrap_route("/boards.json")
    def get_threads(self, board):
        return self.wrap_route(f"/{board}/threads.json")
    def get_catalog(self, board):
        return self.wrap_route(f"/{board}/catalog.json")
    def wrap_route(self, route):
        return json.loads(requests.get(self.endpoint+route).text)
instance = driver("https://a.4cdn.org", "https://i.4cdn.org", "https://s.4cdn.org")