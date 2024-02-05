class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces + 1))
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets and self.parking_spaces:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket = {"ticket_number": ticket_number, "parking_space": parking_space, "paid": False}
            print(f"Ticket {ticket_number} issued. Park in space {parking_space}.")
        else:
            print("Sorry, the parking garage is full.")

    def pay_for_parking(self):
        if self.current_ticket:
            payment = input("Enter the payment amount: ")
            if payment:
                print("Ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket["paid"] = True
                self.leave_garage()
            else:
                print("Payment cannot be empty.")
                self.pay_for_parking()
        else:
            print("No active ticket. Please take a ticket first.")

    def leave_garage(self):
        if self.current_ticket:
            if self.current_ticket["paid"]:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.current_ticket["parking_space"])
                self.tickets.append(self.current_ticket["ticket_number"])
                self.current_ticket = {}
                add_cust()
            else:
                self.pay_for_parking()
        else:
            print("No active ticket. Please take a ticket first.")


class Customer:
    def __init__(self, name, car_number):
        self.name = name
        self.car_number = car_number

    def park_car(self, garage):
        print(f"\nAvailable parking garages for {self.name}:")
        for i, parking_garage in enumerate(garage):
            print(f"{i + 1}. Parking Garage - {len(parking_garage.parking_spaces)} empty parking spaces")

        selected_garage_index = int(input("Enter the number of the parking garage you want to park in: ")) - 1

        if 0 <= selected_garage_index < len(garage):
            selected_garage = garage[selected_garage_index]
            selected_garage.take_ticket()
            print(f"\nRemaining parking spaces in Parking Garage - {len(selected_garage.parking_spaces)}\n")
        else:
            print("Invalid garage selection. Please choose a valid parking garage.")


    def leave_garage(self):
        leave_garage_option = input("Do you want to leave the garage? (yes/no): ").lower()
        if leave_garage_option == 'yes':
            customer_name_to_leave = input("What's your name? ")
            customer_to_leave = next((c for c in customers if c.name == customer_name_to_leave), None)
            if customer_to_leave:
                garage_to_leave = int(input("Enter the number of the garage you want to leave: ")) - 1
                garages[garage_to_leave].leave_garage()
                customers.remove(customer_to_leave)  # Remove the customer from the list
            else:
                print("Customer not found in the list.")
                self.leave_garage()
        else:
            print("Goodbye! Have a nice day.")


# Example Usage
garage1 = ParkingGarage(total_tickets=10, total_parking_spaces=10)
garage2 = ParkingGarage(total_tickets=15, total_parking_spaces=15)
garage3 = ParkingGarage(total_tickets=8, total_parking_spaces=8)

garages = [garage1, garage2, garage3]

customers = []


def add_cust():
    new_customer_option = input("Do you want to park your car? (yes/no): ").lower()

    if new_customer_option == 'yes':
        customer_name = input("Enter customer name: ")
        customer_car_number = input("Enter customer car number: ")
        customer = Customer(customer_name, customer_car_number)
        customers.append(customer)
        customer.park_car(garages)
        add_cust()
    elif new_customer_option == 'no':
        for customer in customers:
            customer.leave_garage()
    else:
        print("Invalid option. Please enter 'yes' or 'no'.")
        add_cust()

add_cust()