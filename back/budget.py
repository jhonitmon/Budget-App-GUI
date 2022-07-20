
from datetime import datetime
import pandas as pd
import calendar
from pathlib import Path

# class declaration
class Budget:
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
                        date = date.split(".")
                        newdate = datetime(int(date[2]),int(date[1]),int(date[0]))
                        break
                    except:
                        print("Please enter a valid date.")
                        pass
                date = input("Please enter the date in the [\"dd.mm.yyyy\"] format: ")
                
                try:
                    newdate = datetime(int(date[2]),int(date[1]),int(date[0]))
                except:
                    print("Please enter a valid date.")
                    continue
                break
            
            # check if break or continue
            if skip == 0: print("Data succesfully added!")
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
            self.tally = pd.concat([self.tally,added_data], ignore_index=True).sort_values("date")
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
                date = datetime(int(date[2]),int(date[1]),int(date[0]))
                break
            except:
                print("Please enter a valid date.")
                date = input("Please enter the desired date in the [\"dd.mm.yyyy\"] format: ")
                continue
        new_df = self.tally[self.tally["date"] == date]
        sum = new_df["amount"].sum()
        return sum
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
        return sum

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
        return sum

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
            return sum
    
    # summarize method
    def summarize(self):
        year_dict = dict()
        year_df = self.tally
        month_names = list(calendar.month_name)
        year_df["year"] = self.tally["date"].dt.year
        date_today = datetime.today()
        for i in year_df.year.unique():
            year_dict[str(i)] = {
                "max_i": 0,
                "max_e": 0,

                "avg_d_i": 0,
                "avg_d_e": 0,
                "avg_d_t": 0,
                
                
                "avg_m_i": 0,
                "avg_m_e": 0,
                "avg_m_t": 0,
                
                "i_year": 0,
                "e_year": 0,
                "total": 0,

                "max_i_type": 0,
                "max_e_type": 0,

                "best_m": 0,
                "worst_m": 0,
                "months" : {}
                }
            year_items = self.tally[self.tally.date.dt.year == i]
            year_incomes = year_items[year_items.amount > 0]
            year_expenses = year_items[year_items.amount < 0]

            max_iitem = year_items[year_items.amount == year_items.amount.max()].iloc[0,:]
            max_eitem = year_items[year_items.amount == year_items.amount.min()].iloc[0,:]

            if i == date_today.year:
                n_days = (date_today - date_today.replace(month=1, day=1)).days
                n_months = date_today.month

            else:
                n_days = 365
                n_months = 12
            
            avg_d_t = year_items.amount.sum() / n_days
            avg_d_i = year_incomes.amount.sum() / n_days
            avg_d_e = year_expenses.amount.sum() / n_days
            avg_m_t = year_items.amount.sum() / n_months
            avg_m_i = year_incomes.amount.sum() / n_months
            avg_m_e = year_expenses.amount.sum() / n_months
            month_list = year_df[["date","amount"]]
            month_list["month"] = month_list.date.dt.month
            month_group = month_list.groupby("month",as_index=False).sum()
            for j in range(1,n_months + 1):
                name = month_names[j]
                iter_list = month_list[month_list.month == j]
                iter_incomes = iter_list[iter_list.amount > 0]
                iter_expenses = iter_list[iter_list.amount < 0]
                year_dict[str(i)]["months"][name]= {
                    "total": iter_list.amount.sum(),
                    "e_month": iter_incomes.amount.sum(),
                    "i_month": iter_expenses.amount.sum()}
            year_dict[str(i)]["max_i"] = max_iitem.amount
            year_dict[str(i)]["max_e"] = max_eitem.amount
            year_dict[str(i)]["max_i_type"] = max_iitem.type
            year_dict[str(i)]["max_e_type"] = max_eitem.type
            year_dict[str(i)]["i_year"] = year_incomes.amount.sum()
            year_dict[str(i)]["e_year"] = year_expenses.amount.sum()
            year_dict[str(i)]["total"] = year_items.amount.sum()
            year_dict[str(i)]["avg_d_t"] = round(avg_d_t,2)
            year_dict[str(i)]["avg_d_i"] = round(avg_d_i,2)
            year_dict[str(i)]["avg_d_e"] = round(avg_d_e,2)
            year_dict[str(i)]["avg_m_t"] = round(avg_m_t,2)
            year_dict[str(i)]["avg_m_i"] = round(avg_m_i,2)
            year_dict[str(i)]["avg_m_e"] = round(avg_m_e,2)
            best_m = month_group[month_group.amount == month_group.amount.max()].month.iloc[0]
            worst_m = month_group[month_group.amount == month_group.amount.min()].month.iloc[0]
            year_dict[str(i)]["best_m"] = month_names[best_m]
            year_dict[str(i)]["worst_m"] = month_names[worst_m]
        
        return year_dict
