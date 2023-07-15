#importing modules
import os
import sys
import time
import datetime
import math
from datetime import date
from datetime import datetime
from datetime import timedelta




#main class
class Billing_System:

    def __init__(self):
        import datetime

        shopName=("***Welcome to the ITUM Supermarket***")
        shopaddress=("123, Horana Road, Diyagama, Homagama")
        shopcontact=("011-1234567")

        print((45*'=').center(75))
        print(shopName.center(75))
        print((45*'=').center(75))
        print(shopaddress.center(75))
        print(shopcontact.center(75))
        print(len(shopName.center(75))*"-")

        TodayDate = date.today()
        NowTime = datetime.datetime.now()

        cashierName=input("Enter Cashier Name: ")
        customerName=input("Enter Customer Name: ")

        print(f"Date: {TodayDate}".ljust(50), f"Cashier: {cashierName[:14].strip()}")
        print(f"Time: {NowTime.strftime('%H:%M:%S')}".ljust(50), f"Customer: {customerName[:14].strip()}")

        print(len(shopName.center(75))*"-")
        
    #creating empty lists
    def empty_lists(self):
        self.item_list=[]
        self.quantity_list=[]
        self.price_list=[]
        self.total_price=0
        self.total_quantity=0
        
    #asking the user to add more items        
    def Addmore(self):
        self.choice=input("Do you want to add more items? (Y/N): ")
        self.choice=self.choice.upper()
        if self.choice=='Y':
            self.add_items()            
        elif self.choice=='N':
            self.display_bill()
        elif self.choice!='Y' or self.choice!='N':
            print("Invalid Input!")
            self.Addmore()
        
    #adding items to the list
    def add_items(self):
        while True:
            self.item_list.append(input("Enter Item Name: "))
            self.quantity_list.append(int(input("Enter Quantity: ")))
            self.price_list.append(float(input("Enter Price: ")))
            self.total_price_list=[a*b for a,b in zip(self.quantity_list,self.price_list)]
            self.Addmore()
                
    #displaying the bill
    def display_bill(self):
        print("-Item Name-".ljust(30),"-Quantity-".ljust(15),"-Price-".ljust(15),"-Total-".ljust(15))
        
        for item,quantity,price,total in zip(self.item_list, self.quantity_list, self.price_list, self.total_price_list):
            align1=item.ljust(30)
            align2=str(quantity).ljust(15)
            align3=str(price).ljust(15)
            align4=str(total).ljust(15)
            print(align1,align2,align3,align4)
            
        print((75*"-").center(75))
        
        self.total_quantity= sum(self.quantity_list)
        print("Total Quantity: ",self.total_quantity,"Items")
        
        self.total_price= sum(self.price_list)
        self.total_price=round(self.total_price,2)
        print("Total Price: ",self.total_price)
        
        print((75*"-").center(75))
        self.ComeAgain()
        
        
    #calculating the discount
    print("Discounts")
            
            
            
    #come again        
    def ComeAgain(self):
        print((75*"=").center(75))
        print(("Thank you for shopping with us!").center(75))
        
        print(("Please come again!").center(75))
        print((5*"*").center(75))



obj = Billing_System()
obj.empty_lists()
obj.add_items()
obj.display_bill()
