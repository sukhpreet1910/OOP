class Animal:
    IN_DANGER_COUNT = 500
    def __init__(self, name, species, feed):
        self.name = name
        self.species = species
        self.feed = feed
    def make_sound(self):
        pass
    

    def increment_feed(self):
        increment = float(input(f"By how much kgs you want to increase {self.name}'s feed: "))
        if increment > 0 :
            self.feed += increment
            print(f"{self.name}'s Daily Feed is now {self.feed}Kgs. ")
        else:
            print('Enter Valid Amount')


    def health_status(self):
        print(f"Enter 1. If {self.name} is in Super Healthy State. ")
        print(f"Enter 2. If {self.name} Needs Increment in daily Feed. ")
        print(f"Enter 3. If {self.name} Needs a to see a Doctor. ")

        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                print(f'\n{self.name} is super Healthy')
            elif choice == 2:
                self.increment_feed()
            elif choice == 3:
                self.call_doc()
            else:
                print("Enter a valid input. \n")
                self.health_status()
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
            self.health_status()

    def call_doc(self):
        print(f'I am here to help {self.name}')

    def get_species_count(self):
        self.speacies_count = int(input(f'Enter {self.species} speacies count: \n'))
        return self.speacies_count

    def in_danger(self):
        if self.get_species_count() < Animal.IN_DANGER_COUNT:
            return True 
        else:
            return False
    
    

    

class Lion(Animal):
    def __init__(self, name, species, feed, color):
        super().__init__(name, species, feed)
        self.color = color
        

    def make_sound(self):
        print(f'{self.name} Roars Loudly')


class Elephant(Animal):
    def __init__(self, name, species, feed, trump):
        super().__init__(name, species, feed)
        self.trump = float(trump)


    def make_sound(self):
        print(f'{self.name} Trumpets Using his trump')


class Zoo:
    def __init__(self):
        self.animals = []

    
    def add_animal(self, animal):
        self.animals.append(animal)

    def display_info(self):

        for animal in self.animals:
            print(f'{animal.name} - {animal.species}')
            animal.make_sound()
            animal.health_status()
            if animal.in_danger():
                print("These speacies are in Danger of extinction\n")
            else:
                print("Species are not in Danger zone\n")



zoo1 = Zoo()
lion1 = Lion('Simba', 'African Lion', 15, color = 'Golden')
elephant1 = Elephant('Dumbo', 'African Elephant', 12, 2.5)

zoo1.add_animal(lion1)
zoo1.add_animal(elephant1)

zoo1.display_info()