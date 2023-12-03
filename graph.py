import random
from node import Node
from airport import Airport


class Flight_map:
    def __init__(self) -> None:
        self.airports = []

    def _addAirport(self, newAirport: Airport):
        for airport in self.airports:
            if airport.airport.id == newAirport.id:
                raise ValueError("ID already exists!")

        newNode = Node(newAirport)
        self.airports.append(newNode)

    def _setCostByDefault(self, newAirport: Airport):
        for curr in self.airports:
            if curr.airport.id != newAirport.id:
                self._setCost(curr.airport.id, newAirport.id,
                              random.randint(100, 500))
                self._setCost(newAirport.id, curr.airport.id,
                              random.randint(100, 500))

    def _setCost(self, dep_id, des_id, cost):
        for node in self.airports:
            if node.airport.id == dep_id:
                node.airport.route[des_id] = cost

    def _getCost(self, dep_id, des_id):
        for node in self.airports:
            if (node.airport.id == dep_id):
                return node.airport.route[des_id]

    def _calCost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self._getCost(path[i], path[i + 1])
        return cost

    def _getDestinationByAirportID(self, dep_id: int):
        for node in self.airports:
            if node.airport.id == dep_id:
                return node.airport.route

    def _getAirportByName(self, airport_name: str):
        for node in self.airports:
            if node.airport.name == airport_name:
                return node.airport
        return None

    def _getAirportName(self, airport_id: int):
        for node in self.airports:
            if node.airport.id == airport_id:
                return node.airport.name

    def _deleteAirport(self, airport_id: int):
        index = -1
        for node in self.airports:
            if node.airport.id == airport_id:
                index = self.airports.index(node)
                break

        if index == -1:
            raise ValueError("ID không tồn tại!")
        deleted = self.airports.pop(index)
        return deleted

    def _destructeFlightRoute(self, airport_id: int):
        for node in self.airports:
            if airport_id in node.airport.route:
                del node.airport.route[airport_id]

    def _findAllPaths(self, dep_id, des_id, path):
        path = path + [dep_id]
        if dep_id == des_id:
            return [path]
        paths = []
        start = self._getDestinationByAirportID(dep_id)
        for des in start:
            if des not in path:
                newpaths = self._findAllPaths(des, des_id, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def _showPath(self, path):
        for i in range(len(path) - 1):
            print("✈️  " + self._getAirportName(path[i]), end=' -> ')
        print("✈️  " + self._getAirportName(path[-1]))

    def _findShortestPath(self, dep_id, des_id):
        all_paths = self._findAllPaths(dep_id, des_id, path=list())
        min_path = []
        min_cost = int(1e9)
        for path in all_paths:
            cost = 0
            for i in range(len(path) - 1):
                cost += self._getCost(path[i], path[i + 1])
            if min_cost > cost:
                min_cost = cost
                min_path = path
        return {'path': min_path, 'cost': min_cost}

    def _findCostPath(self, dep_id, des_id):
        all_paths = self._findAllPaths(dep_id, des_id, path=list())

        for path in all_paths:
            cost = 0
            for i in range(len(path) - 1):
                cost += self._getCost(path[i], path[i + 1])
            print(f"Path: ", end="")
            self._showPath(path)
            print(f"Cost: {cost} 💵")

    def _showFlightRoute(self):
        for node in self.airports:
            self._display(node.airport)

    def _display(self, airport: Airport):
        print(f"Sân bay: {airport.name}")
        print(f"ID: {airport.id}")
        print(f"Thông tin chuyến bay:")
        print(format("Điểm đến", "^15"), format("Chi phí", ">12"))
        for key, val in airport.route.items():
            print(format("✈️  " + self._getAirportName(key), "<15"),
                  format(val, ">10") + " 💵")
        print("+---------------------------+")


# --------------------------------------------------------------------------------------------------------------------------------------------

    def addAirport(self, newAirport: Airport):
        try:
            self._addAirport(newAirport)
            self._setCostByDefault(newAirport)
            return True
        except ValueError as error:
            print(error)
            return False

    def showFlightRoute(self):
        self._showFlightRoute()

    def searchAirportByName(self, name: str):
        result = self._getAirportByName(name)
        if result == None:
            print("Không tìm thấy sân bay!")
            return
        self._display(result)

    def calCost(self, dep_id, des_id):
        exist_dep_id = False
        exist_des_id = False
        for node in self.airports:
            if node.airport.id == dep_id:
                exist_dep_id = True
            if node.airport.id == des_id:
                exist_des_id = True
        if exist_dep_id == False or exist_des_id == False:
            print("ID không tồn tại!")
            return

        # Tìm đường đi có chi phí nhỏ nhất
        path, cost = self._findShortestPath(dep_id, des_id).values()
        print(f"Path: ", end="")
        self._showPath(path)
        print(f"Cost: {cost} 💵")

        # Tìm chi phí cho tất cả các đường đi
        # self._findCostPath(dep_id, des_id)

    def deleteAirport(self, airport_id: int):
        try:
            deleted = self._deleteAirport(airport_id)
            self._destructeFlightRoute(airport_id)
            print("Đã xóa sân bay: ")
            self._display(deleted.airport)
            return deleted
        except ValueError as error:
            print(error)
            return None

    def updateAirportInfor(self, airport_id: int, airport_name: str, isupdate: int):
        try:
            old_infor = self._deleteAirport(airport_id)
            new_cost = old_infor.airport.route.copy()
            print("Cập nhật chi phí sân bay mới:")
            if isupdate:
                for key in new_cost:
                    cost = int(
                        input(f"Nhập chi phí từ {airport_name} đến {self._getAirportName(key)}: "))
                    new_cost[key] = cost
            newAirport = Airport(airport_id, airport_name, new_cost)
            self._addAirport(newAirport)
        except ValueError as error:
            print(error)

    def showPaths(self, paths):
        for path in paths:
            self._showPath(path)
