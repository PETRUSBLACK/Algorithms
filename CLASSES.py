# class Customer:
#     def __init__(self, name, membership_type):
#         self.name = name
#         self.membership_type = membership_type

# c = Customer("Petrus", "Gold")
# # print(c.name, c.membership_type)

# c2 = Customer("Brad", "Premium")
# # print( c2.name, c.membership_type)

# # list_customers = [c, c2 ]
# list_customers = [ Customer("Petrus", "Gold"), Customer("Brad", "Premium")]
# print(list_customers[0].name, list_customers[1].name)



# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'I am {self.name}')
#         return

# john = Person("JOHN")
# print(john.talk())


class Cricket:
    # teamName = None

    def setTeamName(self, name):
        self.teamName = name
    
    def getTeamName(self):
        return self.teamName

c = Cricket()
c.setTeamName('India')
print(c.getTeamName())