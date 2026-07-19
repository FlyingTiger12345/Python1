class person:
    def __init__(self,name,id,):
        self.name = name
        self.id = id
        
        
    def display(self):
        print(self.name)
        print(self.id)

class employee(person):
    def __init__(self, name, id, wage):
        self.wage = wage

        person.__init__(self,name,id)
p = employee("John",12345678910,67)
p.display()






