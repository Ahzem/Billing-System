#importing modules
from datetime import date


#main class
class Billing_System:

    def __init__(self):
        import datetime #importing datetime module for this class

        shopName=("***Welcome to the ITUM Supermarket***") #shop name
        shopaddress=("123, Horana Road, Diyagama, Homagama") #shop address
        shopcontact=("011-1234567") #shop contact number

        print((45*'=').center(75)) #printing 45 '=' in the center of 75 characters
        print(shopName.center(75)) #printing the shop name in the center of 75 characters
        print((45*'=').center(75)) 
        
        print(shopaddress.center(75)) #printing the shop address in the center of 75 characters
        print(shopcontact.center(75)) #printing the shop contact number in the center of 75 characters
        print(len(shopName.center(75))*"-") #printing the length of the shop name in the center of 75 characters

        TodayDate = date.today() #getting the current date
        NowTime = datetime.datetime.now() #getting the current time

        cashierName=input("Enter Cashier Name: ") #getting the cashier name
        customerName=input("Enter Customer Name: ") #getting the customer name

        print(f"Date: {TodayDate}".ljust(50), f"Cashier: {cashierName[:14].strip()}") #printing the date and the cashier name
        print(f"Time: {NowTime.strftime('%H:%M:%S')}".ljust(50), f"Customer: {customerName[:14].strip()}") #printing the time and the customer name

        print(len(shopName.center(75))*"-") 
        
    #creating empty lists
    def empty_lists(self): 
        self.item_list=[] #creating an empty list for items
        self.quantity_list=[] #creating an empty list for quantity
        self.price_list=[] #creating an empty list for price
        self.total_price=0 #creating an empty list for total price
        self.total_quantity=0 #creating an empty list for total quantity
        
    #asking the user to add more items        
    def Addmore(self):
        self.choice=input("Do you want to add more items? (Y/N): ") #asking the user to add more items
        self.choice=self.choice.upper() #converting the input to uppercase
        if self.choice=='Y':
            self.add_items()            
        elif self.choice=='N':
            self.display_bill()
        elif self.choice!='Y' or self.choice!='N':
            print("Invalid Input!")
            self.Addmore() #again asking the user to add more items
        
    #adding items to the list
    def add_items(self):
        while True: #using while loop to add more items
            self.item_list.append(input("Enter Item Name: ")) #asking the user to enter the item name
            self.quantity_list.append(int(input("Enter Quantity: "))) #asking the user to enter the quantity
            self.price_list.append(float(input("Enter Price: "))) #asking the user to enter the price
            self.total_price_list=[a*b for a,b in zip(self.quantity_list,self.price_list)] #calculating the total price
            self.Addmore() #again asking the user to add more items
                
    #displaying the bill
    def display_bill(self):
        print("Item Name".ljust(30),"Quantity".ljust(15),"Price".ljust(15),"Total".ljust(15))
        
        for item,quantity,price,total in zip(self.item_list, self.quantity_list, self.price_list, self.total_price_list): #using for loop to print the items
            align1=item.ljust(30)
            align2=str(quantity).ljust(15)
            align3=str(price).ljust(15)
            align4=str(total).ljust(15)
            print(align1,align2,align3,align4)
            
        print((75*"-").center(75))
        
        self.total_quantity= sum(self.quantity_list) #calculating the total quantity
        print("Total Quantity: ",self.total_quantity,"Items") #printing the total quantity
        
        self.total_price= sum(self.price_list) #calculating the total price
        self.total_price=round(self.total_price,2) #rounding the total price to 2 decimal places
        print("Total Price: ",self.total_price) #printing the total price
         
        print((75*"-").center(75))
        self.ComeAgain()
        
        
    #calculating the discount
    def discount(self):
            
            
            
    #come again        
    def ComeAgain(self):
        print((75*"=").center(75))
        print(("Thank you for shopping with us!").center(75)) #printing the thank you message
        
        print(("Please come again!").center(75)) #printing the come again message
        print((5*"*").center(75))



obj = Billing_System() #creating an object
obj.empty_lists() #calling the empty_lists function
obj.add_items() #calling the add_items function
obj.display_bill()  #calling the display_bill function
