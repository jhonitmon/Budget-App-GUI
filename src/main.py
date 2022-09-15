# importing sys
import sys

# adding lib to PATH
sys.path.insert(0,"/Users/jonathan/Documents/Python Projects/Budget-App/lib")

# importing libraries
import budget
import json
from pprint import pprint

budget = budget.Budget()
budget.add_data()