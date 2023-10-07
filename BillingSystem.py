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
        print(("Welcome to the 'Building Better Bills'!").center(60)) #printing the welcome message
        print(("Please enter the following details:").center(60)) #printing the please enter the following details message
        print((60*"-").center(60)) #printing 60 '-' in the center of 75 characters
        self.cashierName=input("Enter Cashier Name: ") #getting the cashier name
        self.customerName=input("Enter Customer Name: ") #getting the customer name
        print((60*"-").center(60)) #printing 60 '-' in the center of 75 characters
        print(("You can now continue with the billing process.").center(60)) #printing the you can now continue with the billing process message
        print((60*"-").center(60)) #printing 60 '-' in the center of 75 characters
        self.empty_lists() #calling the empty_lists function
        
        
    #creating empty lists
    def empty_lists(self): 
        self.item_list=[] #creating an empty list for items
        self.quantity_list=[] #creating an empty list for quantity
        self.price_list=[] #creating an empty list for price
        self.total_bill_price=0 #creating an empty list for total price
        self.total_quantity=0 #creating an empty list for total quantity
        self.add_items() #calling the add_items function
           
    #asking the user to add more items        
    def Addmore(self):
        self.choice=input("Do you want to add more items? (Y/N): ").strip().upper() #asking the user to add more items
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
            if quantity <= 0: # Check if the input is positive
                print("Invalid Input! Quantity should be a positive integer.")
                self.check_quantity() # Ask the user to enter the quantity again
            else:
                self.quantity_list.append(quantity) # Add the quantity to the quantity list
                self.check_price() # Call the check_price function
        except (ValueError, TypeError, ZeroDivisionError): # If the input is not an integer or negative
            print("Invalid Input! Quantity should be a positive integer.") #printing the invalid input message
            self.check_quantity() # Ask the user to enter the quantity again


    #checking the price and getting the total price
    def check_price(self):
        try: 
            price = float(input("Enter Price: ")) # Convert input to float
            if price < 0: # Check if the input is positive
                print("Invalid Input! Price should be a positive number.")
                self.check_price() # Ask the user to enter the price again
            else:
                self.price_list.append(price) # Add the price to the price list
                self.total_price() # Call the summery function
        except (ValueError, TypeError, ZeroDivisionError): # If the input is not a float or negative
            print("Invalid Input! Price should be a positive number.") #printing the invalid input message
            self.check_price() # Ask the user to enter the price again
            
    def price_zero(self):
        for price in self.price_list:
            if price == 0:
                item_name=self.item_list[self.price_list.index(price)]
                greet_for_free=(f"Congratulations! You got {self.quantity_list[self.price_list.index(price)]} {item_name.title()} for free!")
                print(greet_for_free.center(60))
            else:
                pass
    
    
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
        self.add_discount=input("Do you want to add discount for total bill? (Y/N): ").strip().upper() #asking the user if they want to add discount for total bill
        if self.add_discount == "Y": 
            self.discount_percentage=float(input("Enter Discount Percentage: ")) #asking the user to enter the discount percentage
            self.loyalty_for_discount() #calling the loyalty_for_discount function
            
        elif self.add_discount == "N":
            self.loyalty_for_not_discount() #calling the loyalty_for_not_discount function
            
        elif self.add_discount != "Y" or self.add_discount != "N":
            print("Invalid Input!") #printing the invalid input message
            self.discount() #again asking the user to add discount                 

    #checking the loyalty card holder
    def loyalty_for_discount(self):
        self.loyalty_card=input("Is the customer a loyalty card holder? (Y/N): ") #asking the user if the customer is a loyalty card holder
        self.loyalty_card=self.loyalty_card.strip().upper() #converting the input to uppercase
        if self.loyalty_card == "Y":
            self.loyalty_card_id=input("Enter Loyalty Card ID: ") #asking the user to enter the loyalty card id
            self.loyalty_card = round((self.total_bill_price*0.02),2) #calculating the points earned
            self.discount_added_for_loyalty() #calling the discount_added function
        elif self.loyalty_card == "N":
            self.discount_added_for_not_loyalty() #calling the discount_added function
        elif self.loyalty_card != "Y" or self.loyalty_card != "N":
            print("Invalid Input!")
            self.loyalty_for_discount() #again asking the user if the customer is a loyalty card holder

    def loyalty_for_not_discount(self):
        self.loyalty_card=input("Is the customer a loyalty card holder? (Y/N): ")
        self.loyalty_card=self.loyalty_card.strip().upper()
        if self.loyalty_card == "Y":
            self.loyalty_card_id=input("Enter Loyalty Card ID: ")
            self.loyalty_card = round((self.total_bill_price*0.02),2)
            self.discount_not_added_for_loyalty() #calling the discount_not_added function
        elif self.loyalty_card == "N":
            self.discount_not_added_for_not_loyalty() #calling the discount_not_added function
        elif self.loyalty_card != "Y" or self.loyalty_card != "N":
            print("Invalid Input!")
            self.loyalty_for_not_discount() #again asking the user if the customer is a loyalty card holder
            

#displaying the bill
    def display_bill(self):
        
        import datetime #importing datetime module for this class
        TodayDate = date.today() #getting the current date
        NowTime = datetime.datetime.now() #getting the current time

        shopName=("***Welcome to the [Shop name] Supermarket***") #shop name
        shopaddress=("123, [Street], [City1], [city2]") #shop address
        shopcontact=("011-1234567") #shop contact number

        print((45*'=').center(60)) #printing 45 '=' in the center of 60 characters
        print(shopName.center(60)) #printing the shop name in the center of 60 characters
        print((45*'=').center(60)) 
        
        print(shopaddress.center(60)) #printing the shop address in the center of 60 characters
        print(shopcontact.center(60)) #printing the shop contact number in the center of 60 characters
        print(len(shopName.center(60))*"-") #printing the length of the shop name in the center of 60 characters
        
        print(f"Date: {TodayDate}".ljust(38), f"Cashier: {self.cashierName[:14].strip().title()}") #printing the date and the cashier name
        print(f"Time: {NowTime.strftime('%H:%M:%S')}".ljust(38), f"Customer: {self.customerName[:11].strip().title()}") #printing the time and the customer name

        print(len(shopName.center(60))*"-") 
        

        print("Item Name".ljust(22),"Quantity".ljust(15),"Price".ljust(12),"Total".ljust(12)) #printing the headings
        
        for item,quantity,price,total in zip(self.item_list, self.quantity_list, self.price_list, self.total_price_list): #using for loop to print the items
            align1= item.title().ljust(24) #aligning the item name
            align2=str(quantity).ljust(13)
            align3=str(price).ljust(12)
            align4=str(total).ljust(12)
            print(align1,align2,align3,align4) #printing the items
            
        print((60*"-").center(60)) #printing 60 '-' in the center of 75 characters
        
        self.total_bill_price= sum(self.total_price_list) #calculating the total price
        self.total_bill_price=round(self.total_bill_price,2) #rounding the total price to 2 decimal places
        self.total_quantity= sum(self.quantity_list) #calculating the total quantity

       
    #calculating the total price after discount   
    def discount_added_for_loyalty(self):
        self.display_bill() #calling the display_bill function
        result=self.total_bill_price-(self.total_bill_price*(self.discount_percentage/100)) #calculating the total price after discount
        
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print(("Total Price: ").ljust(20),self.total_bill_price) #printing the total price before discount
        print((45*".").center(60))
        
        self.price_zero()
        
        greet=(f"Congratulations! You got a discount of {self.discount_percentage}%")
        print(greet.center(60))#printing the discount percentage
        print((45*".").center(60))
        print(("Total Price after Discount: ").ljust(20),result) #printing the total price after discount
        
        print((60*"-").center(60)) #printing 60 '_' in the center of 75 characters
        print(("Loyalty Card Holder").center(60)) #printing the loyalty card holder message
        print((10*"*").center(60))
        print("Loyalty Card ID: ",self.loyalty_card_id) #printing the loyalty card id
        print(("Points Earned for this Bill:").ljust(20),round(self.total_bill_price*0.02,2)) #printing the points earned for this bill
        print((60*"=").center(60)) #printing 60 '=' in the center of 60 characters

        self.ComeAgain()
        
    def discount_added_for_not_loyalty(self):
        self.display_bill() #calling the display_bill function
        result=self.total_bill_price-(self.total_bill_price*(self.discount_percentage/100))
        
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print(("Total Price: ").ljust(20),self.total_bill_price) #printing the total price before discount
        print((45*".").center(60))
        
        self.price_zero()
        
        greet=(f"Congratulations! You got a discount of {self.discount_percentage}%")
        print(greet.center(60))#printing the discount percentage
        print((45*".").center(60))
        print(("Total Price after Discount: ").ljust(20),result) #printing the total price after discount
        print((60*"=").center(60)) #printing 60 '=' in the center of 60 characters
        
        
    #calculating the total price without discount    
    def discount_not_added_for_loyalty(self):
        self.display_bill() #calling the display_bill function
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print(("Total Price: ").ljust(20),self.total_bill_price) #printing the total price
        print((60*"-").center(60)) #printing 60 '_' in the center of 75 characters
        
        self.price_zero()
        
        print(("Loyalty Card Holder").center(60))
        print((10*"*").center(60))
        print("Loyalty Card ID: ",self.loyalty_card_id) #printing the loyalty card id
        print(("Points Earned for this Bill:").ljust(20),round(self.total_bill_price*0.02,2))
        print((60*"=").center(60)) #printing 60 '=' in the center of 60 characters

        self.ComeAgain() #calling the ComeAgain function
        
        
    def discount_not_added_for_not_loyalty(self):
        self.display_bill()
        print(("Total Quantity: ").ljust(20),self.total_quantity,"Items") #printing the total quantity
        print(("Total Price: ").ljust(20),self.total_bill_price) #printing the total price
        print((60*"_").center(60))
        
        self.price_zero()
        print((60*"=").center(60)) #printing 60 '=' in the center of 60 characters
        
        self.ComeAgain() #calling the ComeAgain function
        

    #come again        
    def ComeAgain(self):
        print(("Thank you for shopping with us!").center(60)) #printing the thank you message
        print(("If you want to exchange or return any item,").center(60)) #printing the exchange or return message
        print(("please bring the bill with you.").center(60)) #printing the exchange or return message
        print(("Please come again!").center(60)) #printing the come again message
        print((6*"*").center(60))
        
        print((60*"_").center(60)) #printing 60 '_' in the center of 75 characters
        self.Anotherbill() #calling the Anotherbill function
        
    def Anotherbill(self):
        another_bill = input("Do you want to provide another bill? (Y/N): ").strip().upper() #asking the user if they want to provide another bill
        if another_bill == "Y":
            self.customerName=input("Enter Customer Name: ") #getting the customer name
            print((60*".").center(60)) #printing 60 ',' in the center of 60 characters
            print(("You can now continue with the billing process.").center(75)) #printing the you can now continue with the billing process message
            print((60*".").center(60)) #printing 60 '.' in the center of 60 characters
            self.empty_lists() #calling the empty_lists function
            
        elif another_bill == "N":
            print("Thank you for using the Building Better Bills!") #printing the thank you message
        elif another_bill != "Y" or another_bill != "N":
            print("Invalid Input!") #printing the invalid input message
            self.Anotherbill() #again asking the user to provide another bill

#creating an object for the class
Billing_System() #creating an object for the class