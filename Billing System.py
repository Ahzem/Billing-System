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
        self.total_bill_price=0 #creating an empty list for total price
        self.total_quantity=0 #creating an empty list for total quantity
        
        
    #asking the user to add more items        
    def Addmore(self):
        self.choice=input("Do you want to add more items? (Y/N): ") #asking the user to add more items
        self.choice=self.choice.upper() #converting the input to uppercase
        if self.choice=='Y':
            self.add_items()            
        elif self.choice=='N':
            self.discount()
        elif self.choice!='Y' or self.choice!='N':
            print("Invalid Input!")
            self.Addmore() #again asking the user to add more items
        
    #adding items to the list
    def add_items(self):
        
        self.item_list.append(input("Enter Item Name: ")) #asking the user to enter the item name
        self.check_quantity() #calling the check_quantity function
        
        
            
    def check_quantity(self):
            try:
                quantity = int(input("Enter Quantity: ")) # Convert input to integer
                self.quantity_list.append(quantity) # Add the quantity to the quantity list
                self.check_price() # Call the check_price function
            except ValueError:
                print("Invalid Input!")
                self.check_quantity() # Ask the user to enter the quantity again



    def check_price(self):
            try:
                price = float(input("Enter Price: ")) # Convert input to float
                self.price_list.append(price) # Add the price to the price list
                self.summery() # Call the summery function
            except ValueError:
                print("Invalid Input!")
                self.check_price()
    
    
    
            
    def summery(self):
            self.total_price_list=[a*b for a,b in zip(self.quantity_list,self.price_list)] #calculating the total price
            self.Addmore() #again asking the user to add more items
                
                



    #calculating the discount
    def discount(self):
        self.add_discount=input("Do you want to add discount? (Y/N): ") #asking the user to add discount
        self.add_discount=self.add_discount.upper() #converting the input to uppercase
        if self.add_discount == "Y": 
            self.discount_percentage=float(input("Enter Discount Percentage: ")) #asking the user to enter the discount percentage
            self.discount_added() #calling the discount_added function
            
        elif self.add_discount == "N":
            self.discount_not_added()
            
        elif self.add_discount != "Y" or self.add_discount != "N":
            print("Invalid Input!")
            self.discount()
            
            
            
        
    #displaying the bill
    def display_bill(self):
        print("Item Name".ljust(30),"Quantity".ljust(15),"Price".ljust(15),"Total".ljust(15)) #printing the headings
        
        for item,quantity,price,total in zip(self.item_list, self.quantity_list, self.price_list, self.total_price_list): #using for loop to print the items
            align1=item.ljust(33)
            align2=str(quantity).ljust(12)
            align3=str(price).ljust(12)
            align4=str(total).ljust(15)
            print(align1,align2,align3,align4)
            
        print((75*"-").center(75))
        
        self.total_bill_price= sum(self.total_price_list) #calculating the total price
        self.total_bill_price=round(self.total_bill_price,2) #rounding the total price to 2 decimal places
        self.total_quantity= sum(self.quantity_list) #calculating the total quantity
        
        
        
    def discount_added(self):
        self.display_bill() #calling the display_bill function
        result=self.total_bill_price-(self.total_bill_price*(self.discount_percentage/100)) #calculating the total price after discount
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print("Congratulations! You got a discount of ",self.discount_percentage,"%") #printing the discount percentage
        print(("Total Price before Discount: ").ljust(20),self.total_bill_price) #printing the total price before discount
        print(("Total Price after Discount: ").ljust(20),result) #printing the total price after discount
        
        self.ComeAgain()
        
        
        
    def discount_not_added(self):
        self.display_bill() #calling the display_bill function
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items")
        print(("Total Price: ").ljust(20),self.total_bill_price)
            
        self.ComeAgain()
        
                
                
                
            
    #come again        
    def ComeAgain(self):
        print((75*"=").center(75))
        print(("Thank you for shopping with us!").center(75)) #printing the thank you message
        print(("If you want to exchange or return any item,").center(75))
        print(("please bring the bill with you.").center(75)) #printing the exchange or return message
        print(("Please come again!").center(75)) #printing the come again message
        print((5*"*").center(75))



obj = Billing_System() #creating an object
obj.empty_lists() #calling the empty_lists function
obj.add_items() #calling the add_items function
