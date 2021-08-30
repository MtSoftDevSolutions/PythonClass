from abc import ABC, abstractmethod
class employeePay (ABC):
    def pay (self, amount):
        print ("Your check is : ", amount)
#this function is telling us to pass in an argument, but we won't tell what kind of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class cashPay (employeePay):
#here we've defined how to implement the payment function from its parent pay class
    def payment (self, amount):
        print("You have received a cash payment of {}, thank you for your hard work".format(amount))

class checkPay (employeePay):
#attempting to do one more class if an employee was to get paid by check
    def payment (self, amount):
        print("We have mailed you a check for {}, thank you for your hard work.".format(amount))

if __name__ == "__main__":
    obj = cashPay () #This makes the cashPay class show up 
    obj.payment("$1500") #This gives the value in the sentence and correctly works with the .format
    obj = checkPay() 
    obj.payment("$1500")
    
    
