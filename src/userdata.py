class UserData:
    data: {}

    def __init__(self, data):
        data = self.data

    def getData(self):
       return self.data

   def gainItem(self, itemId, amount):
       self.data["item"][str(itemId)] += amount
