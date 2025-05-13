class Bus:
    """
    Represents a bus with its associated details.
    """

    def __init__(self, bus_id: int, route: str, time: str, total_seats: int, available_seats: int, rent: int):
        """
        Initializes a new Bus object.

        Args:
            bus_id (int): The unique identifier for the bus.
            route (str): The route the bus travels.
            time (str): The scheduled departure time of the bus.
            total_seats (int): The total number of seats on the bus.
            available_seats (int): The number of seats currently available.
            rent (int): The rental cost of the bus.
        """
        self.bus_id = bus_id
        self.route = route
        self.time = time
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.rent = rent

    def __repr__(self):
        """
        Provides a string representation of the Bus object.
        """
        return (f"Bus(bus_id={self.bus_id}, route='{self.route}', time='{self.time}', "
                f"total_seats={self.total_seats}, available_seats={self.available_seats}, rent={self.rent})")
