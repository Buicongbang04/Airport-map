from airport import Airport


class Node:
    def __init__(self, airport: Airport) -> None:
        self.airport = airport
        self.linked = dict()
