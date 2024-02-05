# class ParkingGarage:

    # def __init__(self, ticketsAvailable, parkingSpaceAvailable):
    #     self.tickets = list(range(1, ticketsAvailable + 1))
    #     self.parkingSpaces = list(range(1, parkingSpaceAvailable + 1))
    #     self.currentTicket = {}

    # def takeTicket(self):
    #     if self.tickets:
    #         ticketNumber = self.tickets.pop(0)
    #         parkingNumber = self.parkingSpaces.pop(0)
    #         self.currentTicket = {'ticket_number' : ticketNumber, 'parking_number': {parkingNumber}, 'paid': False}
    #         print(f"Ticket taken: {ticketNumber}. Park on {parkingNumber} ")
    #     else:
    #         print("Sorry, The Parking lot of full.")


    # def payForParking(self):
    #     if self.currentTicket and not self.currentTicket['paid']:
    #         payment = input("Enter the payment amount")
    #         if payment:
    #             print(f"Ticket {self.currentTicket['ticket_number']} has been paid. You have 15 minutes to leave ")
    #             self.currentTicket['paid'] = True
    #         else:
    #             print("Payment Not Recieved")
    #     else:
    #         print("Not a valid ticket to pay for")

    # def leaveGarage(self):
    #     if self.currentTicket:
    #         if self.currentTicket['paid']:
    #             print("Thank you! Have a nice day.")
    #         else:
    #             payment = input("Enter the payment amount")
    #             if payment:
    #                 print("Thank you! Have a nice day.")
    #                 self.currentTicket['paid'] = True
    #             else:
    #                 print("Payment not received")
    #         self.parkingSpaces.append(self.currentTicket['parking_number'])
    #         self.tickets.append(self.currentTicket['ticket_number'])
    #         self.currentTicket = {}
    #         print(self.tickets)
    #         print(self.parkingSpaces)
    #     else:
    #         print("No Valid Ticket To Leave")

# customer1 = ParkingGarage(10, 10)
# customer2 = ParkingGarage(10, 10)

# # Customer 1 actions
# customer1.takeTicket()
# customer1.payForParking()
# customer1.leaveGarage()

# # Customer 2 actions
# customer2.takeTicket()
# customer2.payForParking()
# customer2.leaveGarage()
            
class ParkingGarage:
    # Class variables shared among all instances
    total_tickets = 0
    total_parking_spaces = 0
    tickets = []
    parking_spaces = []

    def __init__(self):
        # Initialize instance-specific variables
        self.current_ticket = {}

    @classmethod
    def initialize(cls, total_tickets, total_parking_spaces):
        # Class method to initialize class variables
        cls.total_tickets = total_tickets
        cls.total_parking_spaces = total_parking_spaces
        cls.tickets = list(range(1, total_tickets + 1))
        cls.parking_spaces = list(range(1, total_parking_spaces + 1))

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket = {'ticket_number': ticket_number, 'paid': False, 'parking_space': parking_space}
            print(f"Ticket {ticket_number} taken. Park in space {parking_space}.")
        else:
            print("Sorry, the parking lot is full.")

    def payForParking(self):
        if self.current_ticket and not self.current_ticket['paid']:
            payment = input("Enter the payment amount: ")
            if payment:
                print(f"Ticket {self.current_ticket['ticket_number']} has been paid. You have 15 minutes to leave.")
                self.current_ticket['paid'] = True
            else:
                print("Payment not received.")
        else:
            print("No valid ticket to pay for.")

    def leaveGarage(self):
        if self.current_ticket:
            if self.current_ticket['paid']:
                print("Thank you! Have a nice day.")
            else:
                payment = input("Payment not received. Please enter the payment amount: ")
                if payment:
                    print("Thank you! Have a nice day.")
                    self.current_ticket['paid'] = True
                else:
                    print("Payment not received. Exiting garage.")
            self.parking_spaces.append(self.current_ticket['parking_space'])
            self.tickets.append(self.current_ticket['ticket_number'])
            self.current_ticket = {}
        else:
            print("No valid ticket to leave.")

# Initialize the parking garage with total tickets and parking spaces
ParkingGarage.initialize(total_tickets=10, total_parking_spaces=10)

# Create instances for different customers
customer1 = ParkingGarage()
customer2 = ParkingGarage()

# Customer 1 actions
customer1.takeTicket()
customer1.payForParking()
customer1.leaveGarage()

# Customer 2 actions
customer2.takeTicket()
customer2.payForParking()
customer2.leaveGarage()
