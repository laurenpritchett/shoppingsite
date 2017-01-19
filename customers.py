"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password,
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s, %s, %s>" % (
            self.last_name, self.first_name, self.email)


def read_customer_from_file(file_name):
    """Instantiate customer objects from customer text file.

    "first-name | last-name | email | password"
    """

    customers = {}

    for line in open(file_name):
        (first_name, last_name, email, password) = line.rstrip().split('|')

    customers[email] = Customer(first_name,
                                last_name,
                                email,
                                password,
                                )

    return customers


def get_by_email(email):
    """Return customer object by email."""

    return customers[email]

customers = read_customer_from_file("customers.txt")
