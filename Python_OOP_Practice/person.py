class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def introduce(self):
         print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    def celebrate_birthday(self):
        self.age = self.age + 1
        print(f"Hi, I'm {self.name}. I Celebrated my Birthday today. Now my age is {self.age}")

    def greet(self, otherPerson):
        print(f"Hi, {otherPerson.name}! I'm {self.name}. Nice to meet you.")
    
    def age_diff(self, otherPerson):
        return self.age - otherPerson.age
    
    def eligible_toVote(self):
        return self.age >= 18
    
person1 = Person('Sukh', 23)
person2 = Person('Noor', 22)
person1.introduce()
print(f"is {person1.name} an adult: {person1.is_adult()}")

person2.introduce()
print(f"is {person2.name} an adult: {person2.is_adult()}")

person1.celebrate_birthday()

person1.greet(person2)
print(f"Age Difference is: {person1.age_diff(person2)} years")

print(f"is {person1.name} is eligible to vote ? {person1.eligible_toVote()}")