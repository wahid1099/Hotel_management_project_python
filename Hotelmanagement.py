from db_connection import connect_to_database
from prettytable import PrettyTable
from mysql.connector import Error


class HotelManagement:
    def __init__(self):
        self.db = connect_to_database()
        self.cursor = self.db.cursor()
        
class Room:
    def __init__(self, room_type, rate_per_night):
        self.room_type = room_type
        self.rate_per_night = rate_per_night

    def __str__(self):
        return f"Room Type: {self.room_type}, Rate per Night: Rs {self.rate_per_night}"

class Customer:
    def __init__(self, name, address, check_in_date, check_out_date, room_no,user_mail):
        self.name = name
        self.address = address
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_no = room_no
        self.user_mail = room_no

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Check-in Date: {self.check_in_date}, Check-out Date: {self.check_out_date}, Room No.: {self.room_no}, User_email.: {self.user_mail}"

class HotelBill:
    def __init__(self, additional_service_charge=1800):
        self.room_rent = 0
        self.restaurant_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        self.total_bill = 0
        self.additional_service_charge = additional_service_charge

    def calculate_total_bill(self):
        self.total_bill = self.room_rent + self.restaurant_bill + self.laundry_bill + self.game_bill + self.additional_service_charge

    def display_bill(self, customer):
        print("\n******HOTEL BILL******")
        print("Customer details:")
        print(customer)
        print("Your Room rent is:", self.room_rent)
        print("Your Food bill is:", self.restaurant_bill)
        print("Your laundry bill is:", self.laundry_bill)
        print("Your Game bill is:", self.game_bill)
        print("Your sub total bill is:", self.total_bill - self.additional_service_charge)
        print("Additional Service Charges is", self.additional_service_charge)
        print("Your grand total bill is:", self.total_bill)

class Hotel:
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "password"
    USER_USERNAME = "user"
    USER_PASSWORD = "12345"

        
    def __init__(self):
        self.admin_logged_in = False
        
        self.user_logged_in = False
        print("\n\n*****WELCOME TO DIU HOTEL MANAGEMENT SYSTEM*****\n")
       
        self.customers = []
        self.bill = HotelBill()
        self.db = connect_to_database()
        self.cursor = self.db.cursor()
    
    
    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.ADMIN_USERNAME and password == self.ADMIN_PASSWORD:
            print("Admin login successful.")
            self.admin_logged_in = True
        else:
            print("Invalid admin credentials. Please try again.")
    
    def user_login(self):
        username = input("Enter user username: ")
        password = input("Enter user password: ")
        if username == self.USER_USERNAME and password == self.USER_PASSWORD:
            print("User login successful.")
            self.user_logged_in = True
        else:
            print("Invalid user credentials. Please try again.")
    
    
    
    def display_rooms(self):
        try:
            self.cursor.execute("SELECT room_number, price, is_booked FROM rooms")
            rooms = self.cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["Room Number", "Rate per Night", "Availability"]
            for room in rooms:
                availability = "Available" if room[2] == 0 else "Booked"
                table.add_row([room[0], room[1], availability])
            print(table)
        except Error as e:
            print(f"Error retrieving rooms: {e}")



    def input_customer_data(self):
        name = input("\nEnter your name: ")
        useremail = input("\nEnter your email: ")
        address = input("\nEnter your address: ")
        roomno = input("\nEnter Room no : ")
        check_in_date = input("\nEnter your check in date: ")
        check_out_date = input("\nEnter your checkout date: ")
        print("Your room no.:", len(self.customers) + 101, "\n")
        sql = "INSERT INTO customers (name, address, check_in_date, check_out_date, room_no,user_email) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, address, check_in_date, check_out_date,roomno ,useremail)
        self.cursor.execute(sql, values)
        self.db.commit()
        print("Customer added successfully.")
        
        return Customer(name, address, check_in_date, check_out_date, roomno,useremail)

   

    def restaurant_bill(self):
        print("*****RESTAURANT MENU*****")
        menu = {
            1: ("water", 20),
            2: ("tea", 10),
            3: ("breakfast combo", 90),
            4: ("lunch", 110),
            5: ("dinner", 150)
        }
        while True:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                break
            if choice in menu:
                quantity = int(input("Enter the quantity: "))
                self.bill.restaurant_bill += menu[choice][1] * quantity
            else:
                print("Invalid option")

    def laundry_bill(self):
        print("******LAUNDRY MENU*******")
        menu = {
            1: ("Shorts", 3),
            2: ("Trousers", 4),
            3: ("Shirt", 5),
            4: ("Jeans", 6),
            5: ("Girl suit", 8)
        }
        while True:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                break
            if choice in menu:
                quantity = int(input("Enter the quantity: "))
                self.bill.laundry_bill += menu[choice][1] * quantity
            else:
                print("Invalid option")

    def game_bill(self):
        print("******GAME MENU*******")
        menu = {
            1: ("Table tennis", 60),
            2: ("Bowling", 80),
            3: ("Snooker", 70),
            4: ("Video games", 90),
            5: ("Pool", 50)
        }
        while True:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                break
            if choice in menu:
                hours = int(input("No. of hours: "))
                self.bill.game_bill += menu[choice][1] * hours
            else:
                print("Invalid option")

    def online_booking(self):
        print("*****ONLINE BOOKING*****")
        # Implement online booking system here
        pass
    
    def display_customers(self):
        try:
            self.cursor.execute("SELECT * FROM customers")
            customers = self.cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Address", "Check-in Date", "Check-out Date", "Room No."]
            for customer in customers:
                table.add_row(customer)
            print(table)
        except Error as e:
            print(f"Error retrieving customers: {e}")


    def main(self):
        while True:
            if not self.admin_logged_in and not self.user_logged_in:
                print("1. Admin Login")
                print("2. User Login")
                print("3. EXIT")
                login_choice = int(input("\nEnter your choice: "))
                if login_choice == 1:
                    self.admin_login()
                elif login_choice == 2:
                    self.user_login()
                elif login_choice == 3:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif self.admin_logged_in:
                print("1. Enter Customer Data")
                print("2. Calculate room rent")
                print("3. Calculate restaurant bill")
                print("4. Calculate laundry bill")
                print("5. Calculate game bill")
                print("6. Show total cost")
                print("7. Online Booking")
                print("8. Display Customers")
                print("9. Display All Rooms")
            
                print("10. EXIT")
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    customer = self.input_customer_data()
                    
                elif choice == 2:
                    self.room_rent()
                elif choice == 3:
                    self.restaurant_bill()
                elif choice == 4:
                    self.laundry_bill()
                elif choice == 5:
                    self.game_bill()
                elif choice == 6:
                    self.bill.calculate_total_bill()
                    customer = self.customers[-1]  # Get the last added customer
                    self.bill.display_bill(customer)
                elif choice == 7:
                    self.online_booking()
                elif choice == 8:
                    self.display_customers()
                
                elif choice == 9:
                    self.display_rooms()
                    
                elif choice == 10:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif self.user_logged_in:
                # User functionalities
                print("1. Online Booking")
                # Other user functionalities...
                print("9. EXIT")
                user_choice = int(input("\nEnter your choice: "))
                if user_choice == 1:
                    self.online_booking()
                # Other user choices...
                elif user_choice == 9:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    hotel = Hotel()
    hotel_management = HotelManagement()
    hotel.main()
