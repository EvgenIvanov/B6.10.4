from classes.person import Person

class Guest(Person):

    def __init__(self, first_name, last_name, address, status):
        Person.__init__(self, first_name, last_name)
        self.address = address
        self.status = status
    
    def __str__(self):
        return  Person.__str__(self) + ', ' + self.address + ', статус "' + self.status + '"'