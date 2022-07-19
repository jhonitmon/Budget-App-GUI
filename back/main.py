# library imports
import datetime
import pandas as pd
from pathlib import Path

# class declaration
class budget:
    # constructor
    def __init__(self) -> None:

        # check if there is a budget
        check_file = Path("data/budget.csv")
        if check_file.is_file():
            self.tally = pd.read_csv(check_file)
        else:
            self.tally = pd.DataFrame(data = {"reference" : [], "amount" : [], "type" : [], "date" : []})
        
        # transform column data types to fit data
        self.tally["amount"] = pd.to_numeric(self.tally["amount"])
        self.tally["date"] = pd.to_datetime(self.tally["date"])
        
        # income types
        self.itypes = ["Salary","Tips","Other"]
        # expenses types
        self.etypes = ["Groceries","Health Insurance","Leisure","Subscriptions","Food","Investments"]
    
    # add data method declaration
    def add_data(self, ref = None,amount = None, type = None, date = None, skip = 0):
        while True:
            # reference input
            while True:
                if ref != None:
                    break
                ref = input("Please enter a reference: ")
                break    

            # amount input
            while True:
                if amount != None:
                    try:
                        float(amount)
                        break
                    except:
                        print("Please enter a correct number.")
                        pass
                try:
                    amount = float(input("Please enter the amount: "))
                except:
                    print("Please enter a correct number.")
                    continue
                break

            # type selection
            while True:
                if type != None:
                    try:
                        index = type
                        if amount > 0:
                            sclass = self.itypes[int(index)-1]
                        else:
                            sclass = self.etypes[int(index)-1]
                    except:
                        print("Please enter a correct class.")
                        
                        if amount > 0:
                            for i in range(len(self.itypes)):
                                print(i + 1,":",self.itypes[i])   
                            index = input("Please select a type: ")       
                            try:
                                sclass = self.itypes[int(index)-1]
                            except:
                                continue
                        else:
                            for i in range(len(self.etypes)):
                                print(i + 1,":",self.etypes[i])
                            index = input("Please select a type: ")
                            try:
                                sclass = self.etypes[int(index)-1]
                            except:
                                continue
                        
                break
            
            # date input
            while True:
                if date != None:
                    try:
                        date = date.split(".",3)
                        newdate = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
                        break
                    except:
                        print("Please enter a valid date.")
                        pass
                date = input("Please enter the date in the [\"dd.mm.yyyy\"] format: ")
                
                try:
                    newdate = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
                except:
                    print("Please enter a valid date.")
                    continue
                break
            
            # check if break or continue
            print("Data succesfully added!")
            while True:
                if skip == 1:
                    ans = "n"
                    break
                ans = input("Would you like to add another item? [y or n]: ")
                if ans.lower() != "y" and ans.lower() != "n":
                    print("Please enter a correct input.")
                    continue
                break

            # dataframe update
            added_data = pd.DataFrame(data={"reference" : [ref], "date" : [newdate], "amount" : [amount], "type" : [sclass]})
            self.tally = pd.concat([self.tally,added_data], ignore_index=True)
            if ans.lower() != "n":    
                continue
            break
    
    # sum per day method implementation
    def sum_day(self, date = None):
        while True:
            if date == None:
                date = input("Please enter the desired date in the [\"dd.mm.yyyy\"] format: ")
            try:
                date = date.split(".",3)
                date = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
                break
            except:
                print("Please enter a valid date.")
                date = input("Please enter the desired date in the [\"dd.mm.yyyy\"] format: ")
                continue
        new_df = self.tally[self.tally["date"] == date]
        sum = new_df["amount"].sum()
        print(sum, "day")
        pass

    # sum per month method implementation
    def sum_month(self, date = None):
 
        while True:
            if date == None:
                date = input("Please enter the desired month in the [\"mm.yyyy\"] format: ")
            try:
                date = date.split(".",2)
                break
            except:
                print("Please enter a valid date.")
                date = input("Please enter the desired month in the [\"mm.yyyy\"] format: ")
                continue
        new_df = self.tally[self.tally["date"].dt.month == int(date[0])]
        new_df = new_df[self.tally["date"].dt.year == int(date[1])]
        sum = new_df["amount"].sum()
        print(sum, "month")
        pass

    # sum per vear method implementation
    def sum_year(self, date = None):
        while True:
            if date == None:
                date = input("Please enter the desired year in the [\"yyyy\"] format: ")
            try:
                date = date.split(".",1)
                break
            except:
                print("Please enter a valid date.")
                date = input("Please enter the desired year in the [\"yyyy\"] format: ")
                continue
        new_df = self.tally[self.tally["date"].dt.year == int(date[0])]
        sum = new_df["amount"].sum()
        print(sum, "year")
        pass

    # sum per type method implementation
    def sum_type(self, type = None, mode = None):
        while True:
            if mode == None:
                print("Please specify: ")
                mode = int(input("1. Income\n2.Expense"))
                if mode != 1 and mode != 2:
                    print("Please enter a valid option.")
                    continue
            break

        while True:
            if type == None:
                print("Please select a type: ")
                for i in range(len(self.itypes)):
                    print(i + 1,":",self.itypes[i])
                index = input("Please select a type: ")          
                try:
                    sclass = self.itypes[int(index)-1]
                except:
                    continue
            else:
                sclass = self.itypes[int(type)-1]
            new_df = self.tally[self.tally["type"] == sclass]
            sum = new_df["amount"].sum()
            print(sum, "type")
            break


budget = budget()
budget.add_data("Trattoria",800,1,"20.11.2022",1)
budget.add_data("Burger king",-15,5,"20.11.2022",1)
budget.add_data("Tips",100,2,"22.11.2022",1)
budget.sum_day("20.11.2022")
budget.sum_month("11.2022")
budget.sum_year("2022")
budget.sum_type(1,1)

# save data in csv
budget.tally.to_csv("data/budget.csv", index=False)