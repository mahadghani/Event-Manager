# Python program to demonstrate single inheritance
# single inheritance

# author: Mahad Ghani
# instructor: Karla (CS-302)


from balancedTree import *


# Base class
class Event:
    def __init__(self, time, size, description, tools):
        self.time = time
        self.size = size
        self.description = description
        self.tools = tools

    def getData(self):
        self.time = input("Time description: ")
        self.size = input("Description of people here: ")
        self.description = input("Event description: ")
        self.tools = input("Things to bring: ")

    def display(self):
        print("Time:", self.time)
        print("People:", self.size)
        print("Description:", self.description)
        print("What to bring:", self.tools)

    def __str__(self):
        self.display()
        return ""

#################################################################################################
# Derived classes
#################################################################################################

# Dinner Class
class Dinner (Event):
    def __init__(self):
        self.getData()

    def display(self):
        print("Dinner Event:")
        super().display()
        print("Food:", self.food)
        print("Drinks:", self.drinks)
        print("Vegetarian Options:", self.vegetarianOptions)

    def getData(self):
        print("Event Type: Dinner")
        super().getData()
        self.food = input("Food description: ")
        self.drinks = input("Drinks description: ")
        self.vegetarianOptions = input("Describe availability of vegetarian options: ")

    def __str__(self):
        self.display()
        return ""

#################################################################################################

# Snowboard Class
class Snowboarding (Event):
    def __init__(self):
        self.getData()

    def display(self):
        print("Snowboarding Event:")
        super().display()
        print("Lifts:", self.lifts)
        print("Weather:", self.weather)
        print("Costs:", self.cost)

    def getData(self):
        print("Event Type: Snowboarding")
        super().getData()
        self.lifts = input("Description of available lifts: ")
        self.weather = input("Weather description: ")
        self.cost = input("Costs of Snowboarding: ")

    def __str__(self):
        self.display()
        return ""

#################################################################################################

# Volunteer Class
class Volunteer (Event):
    def __init__(self):
        self.getData()

    def display(self):
        print("Volunteer Event:")
        super().display()
        print("Equipment:", self.equipment)
        print("Location:", self.location)
        print("Number of Volunteers:", self.numVolunteers)

    def getData(self):
        print("Event Type: Volunteer")
        super().getData()
        self.equipment = input("Description of equipment needed: ")
        self.location = input("Location description: ")
        self.numVolunteers = input("Number of Volunteers: ")

    def __str__(self):
        self.display()
        return ""

#################################################################################################

# Node and LLL class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __str__(self):
        print(self.data)
        return ""

class LLL:
    def __init__(self):
        self.head = None
   
    def insert(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        empty = self.head
        while(empty.next):
            empty = empty.next
        empty.next=NewNode
        return self.head

    def display(self):
        toShow = self.head
        while toShow is not None:
            print (toShow.data)
            toShow = toShow.next
    
    def __str__(self):
        if (self.head is None):
            print("Empty list")
        self.display()
        return ""

#################################################################################################

class ManageEvent:
    def __init__(self):
        dinnerList  = LLL()
        snowboardingList = LLL()
        volunteerList = LLL()
        self.array = [dinnerList, snowboardingList, volunteerList]
        self.treeRoot = treeNode("0", "0")

    def loadGame(self):
        gameOn = True
        while gameOn:
            choice = input("Please enter:\n1 for event entry\n2 for event display\n3 to see ratings\n4 to leave\n: ")
            if (choice == '1'):
                self.newEntry()
            if (choice == '2'):
                self.displayEvent()
            if (choice == '3'):
                inorder(self.treeRoot)
            if (choice == '4'):
                gameOn = False

    def newEntry(self):
        print("\nWhat event would you like to add?")
        choice = input("1 for Dinner event\n2 for Snowboarding event\n3 for Volunteering event\n: ")
        print("")
        if (choice == '1'):
            self.array[0].insert(Dinner())
            rating = input("Please give a rating from 1 to 10 for this event: ") 
            self.treeRoot = insert(self.treeRoot, rating, "Dinner")
        elif (choice == '2'):
            self.array[1].insert(Snowboarding())
            rating = input("Please give a rating from 1 to 10 for this event: ")
            self.treeRoot = insert(self.treeRoot, rating, "Dinner")
        elif (choice == '3'):
            self.array[2].insert(Volunteer())
            rating = input("Please give a rating from 1 to 10 for this event: ")
            self.treeRoot = insert(self.treeRoot, rating, "Dinner")
        print("")

    def displayEvent(self):
        print("\nWhat event list would you like to display?")
        choice = input("1 for Dinner events\n2 for Snowboarding events\n3 for Volunteering events\n4 for all\n: ")
        if (choice == '1'):
            print(self.array[0])
        elif (choice == '2'):
            print(self.array[1])
        elif (choice == '3'):
            print(self.array[2])
        elif (choice == '4'):
            print("")
            for events in self.array:
                print(events)
        print("")
        
#################################################################################################

#newManager = ManageEvent()
#newManager.loadGame()