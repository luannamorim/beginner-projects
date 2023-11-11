from bs4 import BeautifulSoup
import requests

class WebScraping:
    def __init__(self, url):
        self.url = url

    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup
    
    del __get_rooms(self):
        return self.soup.find_all("div", class_ = "_1fdf")