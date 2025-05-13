class Customer:
    """
    Represents a customer.
    """

    def __init__(self, cust_id: int = None, cust_name: str = None, cust_cnic: int = None, cust_phno: int = None):
        """
        Initializes a new Customer object.

        Args:
            cust_id (int, optional): The unique identifier for the customer. Defaults to None for new customers.
            cust_name (str, optional): The name of the customer. Defaults to None.
            cust_cnic (int, optional): The customer's CNIC (Computerized National Identity Card) number. Defaults to None.
            cust_phno (int, optional): The customer's phone number. Defaults to None.
        """
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.cust_cnic = cust_cnic
        self.cust_phno = cust_phno

    def __repr__(self):
        """
        Provides a detailed string representation of the Customer object.
        """
        return (f"Customer(cust_id={self.cust_id}, cust_name='{self.cust_name}', "
                f"cust_cnic={self.cust_cnic}, cust_phno={self.cust_phno})")
