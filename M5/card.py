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

class BusinessContact(BaseContact):
    def __init__(self, occupation, company_name, company_phone_number,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company_name = company_name
        self.company_phone_number = company_phone_number

    __str__ = lambda self: f"{self.first_name} {self.last_name} {self.phone_number} {self.email} {self.occupation} {self.company_name} {self.company_phone_number}"


    def contact(self):
        print(f"Wybieram numer {self.company_phone_number} i dzwonię do {self.first_name} {self.last_name}")



def create_contact(qty,type='basic'):
    contacts = []
    for i in range(qty):
        if type == 'basic':
            contact = BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        elif type == 'business':
            contact = BusinessContact(fake.job(), fake.company(), fake.phone_number(),
                 first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email()
)
        contacts.append(contact)
    return contacts

# Example usage
for c in create_contact(3, 'business'):
    print(c)
