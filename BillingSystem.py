'''
This is a billing system for a supermarket. 
This system will ask the user to enter the item name, quantity and the price. 
Then it will calculate the total price and display the bill. 
If the user wants to add discount for the total bill, 
the system will ask the user to enter the discount percentage and calculate the total price after discount. 
If the user doesn't want to add discount, the system will display the total price without discount. 
At the end, the system will display the thank you message, exchange messege and ask the user to come again.
'''

#importing modules
from datetime import date

#main class
class Billing_System:

    #constructor
    def __init__(self):
        print(("Welcome to the 'Building Better Bills'!").center(75)) #printing the welcome message
        print(("Please enter the following details:").center(75)) #printing the please enter the following details message
        print((75*"-").center(75)) #printing 75 '-' in the center of 75 characters
        self.cashierName=input("Enter Cashier Name: ") #getting the cashier name
        self.customerName=input("Enter Customer Name: ") #getting the customer name
        print((75*"-").center(75)) #printing 75 '-' in the center of 75 characters
        print(("You can now continue with the billing process.").center(75)) #printing the you can now continue with the billing process message
        print((75*"-").center(75)) #printing 75 '-' in the center of 75 characters

        
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
            self.add_items() #calling the add_items function        
        elif self.choice=='N':
            self.discount() #calling the discount function
        elif self.choice!='Y' or self.choice!='N':
            print("Invalid Input!") #printing the invalid input message
            self.Addmore() #again asking the user to add more items

        
    #adding items to the list
    def add_items(self):
        itemName=str(input("Enter Item Name: ")) #asking the user to enter the item name
        if itemName is None or itemName == "": #if the input is null
            print("Invalid Input!") #printing the invalid input message
            self.add_items() #calling the add_items function
        else:
            self.item_list.append(itemName) #asking the user to enter the item name
            self.check_quantity() #calling the check_quantity function

            
    #checking the quantity and getting the price        
    def check_quantity(self):
        try: 
            quantity = int(input("Enter Quantity: ")) # Convert input to integer
            self.quantity_list.append(quantity) # Add the quantity to the quantity list
            self.check_price() # Call the check_price function
        except ValueError: # If the input is not an integer
            print("Invalid Input!") #printing the invalid input message
            self.check_quantity() # Ask the user to enter the quantity again


    #checking the price and getting the total price
    def check_price(self):
        try: 
            price = float(input("Enter Price: ")) # Convert input to float
            self.price_list.append(price) # Add the price to the price list
            self.total_price() # Call the summery function
        except ValueError: # If the input is not a float
            print("Invalid Input!") #printing the invalid input message
            self.check_price() # Ask the user to enter the price again


    #calculating the total price       
    def total_price(self):
        '''
        Calculates the total price of the items by multiplying the quantity and price of each item.
        Adds the total price to the total_price_list.
        Calls the Addmore function to ask the user if they want to add more items.
        '''
        self.total_price_list=[a*b for a,b in zip(self.quantity_list,self.price_list)] #calculating the total price
        self.Addmore() #again asking the user to add more items

                        
    #calculating the discount
    def discount(self):
        self.add_discount=input("Do you want to add discount for total bill? (Y/N): ") #asking the user to add discount
        self.add_discount=self.add_discount.upper() #converting the input to uppercase
        if self.add_discount == "Y": 
            self.discount_percentage=float(input("Enter Discount Percentage: ")) #asking the user to enter the discount percentage
            print("Generating the bill...") #printing the generating the bill message
            print((75*"_").center(75)) #printing 75 '_' in the center of 75 characters
            self.discount_added() #calling the discount_added function
            
        elif self.add_discount == "N":
            print("Generating the bill...") #printing the generating the bill message
            print((75*"_").center(75)) #printing 75 '_' in the center of 75 characters
            self.discount_not_added() #calling the discount_not_added function
            
        elif self.add_discount != "Y" or self.add_discount != "N":
            print("Invalid Input!") #printing the invalid input message
            self.discount() #again asking the user to add discount                 


#displaying the bill
    def display_bill(self):
        
        import datetime #importing datetime module for this class

        shopName=("***Welcome to the [Shop name] Supermarket***") #shop name
        shopaddress=("123, [Street], [City1], [city2]") #shop address
        shopcontact=("011-1234567") #shop contact number

        print((45*'=').center(75)) #printing 45 '=' in the center of 75 characters
        print(shopName.center(75)) #printing the shop name in the center of 75 characters
        print((45*'=').center(75)) 
        
        print(shopaddress.center(75)) #printing the shop address in the center of 75 characters
        print(shopcontact.center(75)) #printing the shop contact number in the center of 75 characters
        print(len(shopName.center(75))*"-") #printing the length of the shop name in the center of 75 characters

        TodayDate = date.today() #getting the current date
        NowTime = datetime.datetime.now() #getting the current time
        
        print(f"Date: {TodayDate}".ljust(50), f"Cashier: {self.cashierName[:14].strip()}") #printing the date and the cashier name
        print(f"Time: {NowTime.strftime('%H:%M:%S')}".ljust(50), f"Customer: {self.customerName[:14].strip()}") #printing the time and the customer name

        print(len(shopName.center(75))*"-") 
        

        
        print("Item Name".ljust(27),"Quantity".ljust(18),"Price".ljust(15),"Total".ljust(15)) #printing the headings
        
        for item,quantity,price,total in zip(self.item_list, self.quantity_list, self.price_list, self.total_price_list): #using for loop to print the items
            align1=item.ljust(30) #aligning the item name
            align2=str(quantity).ljust(15)
            align3=str(price).ljust(15)
            align4=str(total).ljust(15)
            print(align1,align2,align3,align4) #printing the items
            
        print((75*"-").center(75)) #printing 75 '-' in the center of 75 characters
        
        self.total_bill_price= sum(self.total_price_list) #calculating the total price
        self.total_bill_price=round(self.total_bill_price,2) #rounding the total price to 2 decimal places
        self.total_quantity= sum(self.quantity_list) #calculating the total quantity

       
    #calculating the total price after discount   
    def discount_added(self):
        self.display_bill() #calling the display_bill function
        result=self.total_bill_price-(self.total_bill_price*(self.discount_percentage/100)) #calculating the total price after discount
        
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print(("Total Price: ").ljust(20),self.total_bill_price) #printing the total price before discount
        print((45*".").center(75))
        
        greet=(f"Congratulations! You got a discount of {self.discount_percentage}%")
        print(greet.center(75))#printing the discount percentage
        print((45*".").center(75))
        print(("Total Price after Discount: ").ljust(20),result) #printing the total price after discount
        
        self.ComeAgain()
        
        
    #calculating the total price without discount    
    def discount_not_added(self):
        self.display_bill() #calling the display_bill function
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print(("Total Price: ").ljust(20),self.total_bill_price) #printing the total price
            
        self.ComeAgain() #calling the ComeAgain function
        

    #come again        
    def ComeAgain(self):
        print((75*"=").center(75))
        print(("Thank you for shopping with us!").center(75)) #printing the thank you message
        print(("If you want to exchange or return any item,").center(75)) #printing the exchange or return message
        print(("please bring the bill with you.").center(75)) #printing the exchange or return message
        print(("Please come again!").center(75)) #printing the come again message
        print((6*"*").center(75))
        
        print((75*"-").center(75)) #printing 75 '-' in the center of 75 characters
        self.Anotherbill() #calling the Anotherbill function
        
    def Anotherbill(self):
        another_bill = input("Do you want to provide another bill? (Y/N): ") #asking the user to provide another bill
        another_bill = another_bill.upper() #converting the input to uppercase
        if another_bill == "Y":
            print((75*".").center(75)) #printing 75 ',' in the center of 75 characters
            print(("You can now continue with the billing process.").center(75)) #printing the you can now continue with the billing process message
            print((75*".").center(75)) #printing 75 '.' in the center of 75 characters

            class_call.empty_lists() #calling the empty_lists function
            class_call.add_items() #calling the add_items function
            
        elif another_bill == "N":
            print("Thank you for using the Building Better Bills!") #printing the thank you message
        elif another_bill != "Y" or another_bill != "N":
            print("Invalid Input!") #printing the invalid input message
            self.Anotherbill() #again asking the user to provide another bill

#creating an object for the class
class_call=Billing_System() #creating an object for the class
class_call.empty_lists() #calling the empty_lists function
class_call.add_items() #calling the add_items function
