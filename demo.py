class Customer:
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type
        print("customer created")
        
c = Customer("edgar","gold")
print(c.name,c.membership_type)

c2 = Customer("maate","bronze")
print(c2.name,c2.membership_type)
