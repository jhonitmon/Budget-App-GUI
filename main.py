# importing libraries
# import re
import datetime
import calendar
from pprint import pprint
from pandas import array
import numpy as np

# constants
regdate = r"([0-9]{2})\.([0-9]{2})\.([0-9]{4})"
ylist = list()

# year class creation
class year:
    # constructor
    def __init__(self,yearnr):
        # attributes
        self.yearnr = yearnr
        self.months = list()
        pass

# month class declaration
class month:
    # constructor
    def __init__(self, monthnr):
        # attributes
        self.monthname = calendar.month_name[monthnr]
        self.monthnumber = monthnr
        self.days = list()
        pass
# day class declaration
class day:
    # constructor
    def __init__(self,daynr):
        # attributes
        self.daynnumber = daynr
        self.items = list()
        pass
    def sum(self):
        lsum = np.array([])
        print(len(self.items))
        for i in range(len(self.items)):
            print(self.items[i].amount)
            lsum = np.append(lsum,self.items[i].amount)
        print(lsum)
        sum = np.sum(lsum)
        return sum

# item class creation
class item:
    # constructor
    def __init__(self, type, amount, date, subclass):
        # attributes
        if type == 0:
            self.type = "income"
        else:
            self.type = "expense"
        if self.type == "expense":
            self.amount = -1 * int(amount)
        else:
            self.amount = int(amount)
        self.date = date
        self.subclass = subclass
        pass    

    
while True:
    while True:
        # date = input("Please enter the date in the [dd.mm.yyyy] format: ")
        date = "20.10.2020"
        date = date.split(".",3)
        try:
            newdate = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
        except:
            print("Please enter a valid date.")
        break
    yact = year(int(date[0]))
    mact = month(int(date[1]))
    dact = day(int(date[2]))
    while True:
        type = int(input("Please enter the type:\n0: Income \n1: Expense\n"))
        # type = 1
        if type != 0 and type != 1:
            print("Please enter a correct input.")
            pass
        break

    while True:
        try:
            # amount = 2000
            amount = int(input("Please enter the amount: "))
        except:
            print("Please give a correct number:")
            pass
        break

    1

    while True:
        # sclass = input("Please enter the expense type: ")
        sclass = "pepepepepe"
        break

    while True:
        ans = input("Would you like to add another item? [y or n]: ")
        if ans.lower() != "y" and ans.lower() != "n":
            print("Please enter a correct input.")
            pass
        break
    dact.items.append(item(type,amount,newdate,sclass))
    mact.days.append(dact)
    yact.months.append(mact)
    ylist.append(yact)
    if ans.lower() == "n":    
        print("Proceeding...")
        break
    pass
for i in range(len(ylist)):
    pprint(vars(ylist[i]))
    for j in range(len(ylist[i].months)):
        pprint(vars(ylist[i].months[j]))
        for k in range(len(ylist[i].months[j].days)):
            pprint(vars(ylist[i].months[j].days[k]))
            for l in range(len(ylist[i].months[j].days[k].items)):
                pprint(vars(ylist[i].months[j].days[k].items[l]))
    print("---------------")
print(ylist[0].months[0].days[0].sum())

## resolver problema creacion de nuevos meses iguales