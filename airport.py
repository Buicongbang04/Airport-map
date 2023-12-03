class Airport:
    def __init__(self, id: int, name: str, route=None) -> None:
        self.id = id
        self.name = name
        self.route = dict() if route is None else route
