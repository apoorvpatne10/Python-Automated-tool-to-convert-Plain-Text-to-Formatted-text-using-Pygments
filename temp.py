# sample class

class Sum:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        print('Sum of numbers is:{}'.format(self.num1+self.num2))


if __name__=='__main__':

    # Number 1
    num1 = int(input('Enter First Number : '))
    # Number 2
    num2 = int(input('Enter Second Number : '))
    obj = Sum(num1,num2)
    obj.sum()





