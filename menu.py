from enum import Enum
from graph import Flight_map
from airport import Airport
from tool import Tool


class MenuChoice(Enum):
    EXIT = 0
    ADD_NEW_AIRPORT = 1
    SHOW_AIRPORTS_DETAILS = 2
    SEARCH_AIRPORT_BY_NAME = 3
    CALCULATE_COST_BETWEEN_TWO_AIRPORTS = 4
    UPDATE_AIRPORT_INFORMATION = 5
    DELETE_AIRPORT = 6
    SAVE_TO_FILE = 7


class Menu:
    def __init__(self, flight_map=None) -> None:
        if flight_map is None:
            flight_map = Flight_map()
        self.air_map = flight_map

    def showMenu(self):
        print("+---------+---------+| Menu |+---------+---------+")
        for choice in MenuChoice:
            method = " ".join(choice.name.split("_")).lower()
            print(f"| {choice.value}. To {method:40} |")
        print("+--------+---------+----------+---------+--------+")

    def getChoiceFromUser(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if (MenuChoice(choice)):
                    return choice
            except ValueError:
                print("Invalid choice! Please enter a number in the menu.")

    def handleUserChoice(self, choice):
        match choice:
            case 0:
                # self.handleSaveToFile()
                print("Thanks for using...")
                return False
            case 1:
                print("Processing...")
                self.handleAddAirport()
                print("Done.")
            case 2:
                print("Processing...")
                self.handleShowAllAirportsDetails()
                print("Done.")
            case 3:
                print("Processing...")
                self.handleSearchAirportByName()
                print("Done.")
            case 4:
                print("Processing...")
                self.handleShowCostBetweenTwoAirport()
                print("Done.")
            case 5:
                print("Processing...")
                self.handleUpdateAirportInfor()
                print("Done.")
            case 6:
                print("Processing...")
                self.handleDeleteAirport()
                print("Done.")
            case 7:
                print("Processing...")
                self.handleSaveToFile()
                print("Done.")
        return True

    def handleAddAirport(self):
        while True:
            try:
                id = int(input("Enter airport's id: "))
                break
            except ValueError:
                print("Invalid airport's id!")
        name = input("Enter airport's name: ").strip(" ")
        name = " ".join([word.capitalize() for word in name.split(" ")])
        while "  " in name:
            name = name.replace("  ", " ")
        self.air_map.addAirport(Airport(id, name))

    def handleShowAllAirportsDetails(self):
        self.air_map.showFlightRoute()

    def handleSearchAirportByName(self):
        name = input("Enter airport's name: ").strip(" ")
        name = " ".join([word.capitalize() for word in name.split(" ")])
        while "  " in name:
            name = name.replace("  ", " ")
        self.air_map.searchAirportByName(name)

    def handleShowCostBetweenTwoAirport(self):
        while True:
            try:
                first_airport_id = int(input("Enter first airport's id: "))
                second_airport_id = int(input("Enter second airport's id: "))
                break
            except ValueError:
                print("Invalid airport's id!")
                return
        self.air_map.calCost(first_airport_id, second_airport_id)

    def handleUpdateAirportInfor(self):
        while True:
            try:
                id = int(input("Enter airport's id: "))
                break
            except ValueError:
                print("Invalid airport's id!")
        name = input("Enter airport's name: ").strip(" ")
        name = " ".join([word.capitalize() for word in name.split(" ")])
        while "  " in name:
            name = name.replace("  ", " ")

        isupdate = int(input("Do you want to update cost? (1: Yes, 0: No): "))

        self.air_map.updateAirportInfor(id, name, isupdate)

    def handleDeleteAirport(self):
        while True:
            try:
                id = int(input("Enter airport's id: "))
                break
            except ValueError:
                print("Invalid airport's id!")
        self.air_map.deleteAirport(id)

    def handleSaveToFile(self):
        try:
            Tool.saveToFile(self.air_map, "flight_map.pickle")
        except Exception as e:
            print(e)
