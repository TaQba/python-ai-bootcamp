import time
from faker import Faker
fake = Faker('pl_PL')


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

    __str__ = lambda self: f"{self.first_name} {self.last_name} {self.phone_number} {self.email}"

def count_time(func):
   def wrapper(qty):
       start_time = time.time()
       result = func(qty)

       end_time = time.time()
       return end_time - start_time
   return wrapper

@count_time
def create_contact(qty=1000):
    contacts = []
    for i in range(qty):
        contact = BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        contacts.append(contact)
    return contacts

print(create_contact(1000))
