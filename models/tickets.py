class Ticket:
    """
    Represents a ticket booking for a bus journey.
    """

    def __init__(self, tkt_id: int = None, booked_seats: int = None, validity: str = None, fare: int = None, date: str = None, bus_id: int = None, customer_id: int = None):
        """
        Initializes a new Ticket object.

        Args:
            tkt_id (int, optional): The unique identifier for the ticket. Defaults to None for new tickets.
            booked_seats (int, optional): The number of seats booked on this ticket. Defaults to None.
            validity (str, optional): The validity period of the ticket. Defaults to None.
            fare (int, optional): The total fare for the booked seats. Defaults to None.
            date (str, optional): The date of booking or travel. Defaults to None.
            bus_id (int, optional): The ID of the bus associated with this ticket. Defaults to None.
            customer_id (int, optional): The ID of the customer who booked the ticket. Defaults to None.
        """
        self.tkt_id = tkt_id
        self.booked_seats = booked_seats
        self.validity = validity
        self.fare = fare
        self.date = date
        self.bus_id = bus_id
        self.customer_id = customer_id

    def __repr__(self):
        """
        Provides a detailed string representation of the Ticket object.
        """
        return (f"Ticket(tkt_id={self.tkt_id}, booked_seats={self.booked_seats}, validity='{self.validity}', "
                f"fare={self.fare}, date='{self.date}', bus_id={self.bus_id}, customer_id={self.customer_id})")