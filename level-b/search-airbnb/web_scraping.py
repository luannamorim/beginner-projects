from bs4 import BeautifulSoup
import requests


class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.__get_html()

    def __get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def __get_rooms(self):
        return self.soup.find_all("div", class_="c4mnd7m")

    def __get_subtitle(self, room):
        return room.find("div", class_="g1qv1ctd c1v0rf5q dir dir-ltr").find("span", class_="t6mzqp7 dir dir-ltr").text

    def __get_title(self, room):
        return room.find("div", class_="t1jojoys dir dir-ltr").text

    # def __get_ass(self, room):
    #     return room.find("div", class_="g1qv1ctd c1v0rf5q dir dir-ltr").find("span", class_="t1a9j9y7 r4a59j5 dir dir-ltr").find("span", class_="r1dxllyb dir dir-ltr").text

    def __get_total(self, room):
        try:
            return room.find("div", class_="_tt122m").text
        except:
            return room.find("div", class_="_i5duul").find("span", class_="a8jt5op dir dir-ltr").text

    def pick_all_room(self):
        list_rooms = []
        for room in self.__get_rooms():
            room_info = {}

            room_info["Title"] = self.__get_title(room)
            room_info["Subtitle"] = self.__get_subtitle(room)
            # room_info["Price per Night (R$)"] = self.__get_price(room)
            # room_info["Assessment"] = self.__get_ass(room)
            room_info["Total Price"] = self.__get_total(room)

            list_rooms.append(room_info)

        return list_rooms
