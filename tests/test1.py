# importing sys
import sys

# adding lib to PATH
sys.path.insert(0,"/Users/jonathan/Documents/Python Projects/Budget-App/lib")

# importing other libs
from datetime import datetime
import pandas as pd
import budget
import random as rand
from random import randrange
from datetime import timedelta
import json

# random date function
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

budget = budget.Budget()

d1 = datetime.strptime('1/1/2000 1:30 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.today()
for i in range(1,10000):
    ramount = rand.randint(-10000,10000)
    if ramount > 0:
        rtype = rand.randint(1,len(budget.itypes))
    else:
        rtype = rand.randint(1,len(budget.etypes))
    rref = str(i)
    rdate = random_date(d1,d2).replace(hour=0,minute=0,second=0)
    rdate = rdate.strftime("%d.%m.%Y")
    budget.add_data(ref=rref,amount=ramount,type=rtype,date = rdate,skip=1)

# print(budget.sum_year("2021"))
# print(budget.sum_type(1,1))
dict = budget.summarize()
# save data in csv
budget.save_data_csv()

# # create json of summary
# with open("data/jsontest.json","w", encoding="utf-8") as f:
#     json.dump(dict,f,ensure_ascii=False, indent= 4)