import datetime
# Create a class named Building in the building.py file and define
# the following fields, properties, and methods.

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories

# Methods
# Define a construct() method. The method's logic should set 
# the date_constructed field's value to datetime.datetime.now().
#  You will need to have import datetime at the top of your file.

# Define a purchase() method. The method should accept a single string
# argument of the name of the person purchasing a building. 
# The method should take that string and assign it to the owner property.

# Constructor
# Define your __init__ method to accept two arguments
# address
# stories

# Once defined this way, you can send those values as 
# parameters when you create each instance
#  eight_hundred_eighth = Building("800 8th Street", 12)


class Building:

    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
        self.owner = name
    
    def printBuildingDetails(self):
        print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')

# Creating Your Buildings
# Create 5 building instances
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print 
# the address, owner, stories, and date constructed to the terminal
#  for each one.
# example - 800 8th Street was purchased by Bob Builder on 03/14/2018
#  and has 12 stories.

rolling_hills1 = Building("123 Rolling Hills", 1)
rolling_hills1.purchase("bob")
rolling_hills1.construct()
rolling_hills1.printBuildingDetails()


rolling_hills2 = Building("124 Rolling Hills", 2)
rolling_hills2.purchase("tom")
rolling_hills2.construct()
rolling_hills2.printBuildingDetails()



rolling_hills3 = Building("125 Rolling Hills ", 3)
rolling_hills3.purchase("jon")
rolling_hills3.construct()
rolling_hills3.printBuildingDetails()



rolling_hills4 = Building("126 Rolling Hills", 4)
rolling_hills4.purchase("rob")
rolling_hills4.construct()
rolling_hills4.printBuildingDetails()



rolling_hills5 = Building("127 Rolling Hills", 5)
rolling_hills5.purchase("guy")
rolling_hills5.construct()
rolling_hills5.printBuildingDetails()


