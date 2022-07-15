#Importing libraries

# sheet class creation
class sheet:
    # constructor
    def __init__(self,month):
        # attributes
        self.month = month
        pass
    # inner class item creation
    class item:
        # constructor
        def __init__(self, type, amount, date, subclass):
            # attributes
            self.type = type
            self.amount = amount
            self.date = date
            self.subclass = subclass
            pass


