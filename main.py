from menu import Menu
from tool import Tool

flight_map = Tool.loadFromFile("flight_map.pickle")
menu = Menu(flight_map)
while True:
    menu.showMenu()
    choice = menu.getChoiceFromUser()
    if not menu.handleUserChoice(choice):
        break
