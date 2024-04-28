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


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        print("User login")

    def logout(self):
        print("User logout")
class Hotel:
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "password"
    USER_USERNAME = "user"
    USER_PASSWORD = "12345"
    

        
    def __init__(self):
        self._admin_logged_in = False
        self._user_logged_in = False
        self._db = connect_to_database()
        self._cursor = self._db.cursor()
        self._user_email = None

        print("\n\n*****WELCOME TO DIU HOTEL MANAGEMENT SYSTEM*****\n")
       
        self.customers = []
        self.bill = HotelBill()
       
    
    
    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.ADMIN_USERNAME and password == self.ADMIN_PASSWORD:
            print("Admin login successful.")
            self._admin_logged_in = True
        else:
            print("Invalid admin credentials. Please try again.")
    
    def user_login(self):
        username = input("Enter user email: ")
        password = input("Enter user password: ")
       
        try:
            self._cursor.execute("SELECT * FROM users WHERE email = %s AND pasword = %s", (username, password))
            user = self._cursor.fetchone()
            if user:
                print("User login successful.")
                self._user_logged_in = True
                self._user_email = username
            else:
                print("Invalid user credentials. Please try again.")
        except Error as e:
            print(f"Error authenticating user: {e}")
    
    
    def _add_new_user(self, username, password):
        if not self._admin_logged_in:
            print("You must be logged in as admin to add a new user.")
            return

        try:
            # Insert new user into the database
            sql = "INSERT INTO users (email, pasword) VALUES (%s, %s)"
            values = (username, password)
            self._cursor.execute(sql, values)
            self._db.commit()
            print("New user added successfully.")
        except Error as e:
            self._db.rollback()
            print(f"Error adding new user: {e}")
    
    
    
    def display_rooms(self):
        try:
            self._cursor.execute("SELECT room_number, price, is_booked FROM rooms")
            rooms = self._cursor.fetchall()
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
        room_no = input("\nEnter Room no : ")
        check_in_date = input("\nEnter your check in date: ")
        check_out_date = input("\nEnter your checkout date: ")
        print("Your room no.:", len(self.customers) + 101, "\n")
     
        # self.db.commit()
        # print("Customer Details added successfully.")
        try:
            # Query room price from rooms table
            room_price_sql = "SELECT price FROM rooms WHERE room_number = %s"
            self._cursor.execute(room_price_sql, (room_no,))
            room_price = self._cursor.fetchone()[0]  # Fetch the room price

            # Update booking table
            booking_sql = "INSERT INTO bookings (room_number, customer_name, customer_email, check_in_date, check_out_date, total_bill) VALUES (%s, %s, %s, %s, %s, %s)"
            booking_values = (room_no, name, useremail, check_in_date, check_out_date, room_price)
            self._cursor.execute(booking_sql, booking_values)

            # Update rooms table to mark room as booked
            update_room_sql = "UPDATE rooms SET is_booked = TRUE WHERE room_number = %s"
            self._cursor.execute(update_room_sql, (room_no,))
            
            sql = "INSERT INTO customers (name, address, check_in_date, check_out_date, room_no,user_email) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, address, check_in_date, check_out_date,room_no ,useremail)
            self._cursor.execute(sql, values)

            self._db.commit()
            print("Customer added successfully.")

            return Customer(name, address, check_in_date, check_out_date, room_no, useremail)
        except Error as e:
            self._db.rollback()
            print(f"Error adding customer: {e}")
        
        return Customer(name, address, check_in_date, check_out_date, room_no,useremail)

   
    def display_bookings(self):
        try:
            self._cursor.execute("SELECT * FROM bookings")
            bookings = self._cursor.fetchall()
            if not bookings:
                print("No bookings found.")
                return
            
            table = PrettyTable()
            table.field_names = ["Booking ID", "Room Number", "Customer Name", "User Email", "Check-in Date", "Check-out Date", "Total Bill "]
            for booking in bookings:
                table.add_row(booking)
            print(table)
        except Error as e:
            print(f"Error retrieving bookings: {e}")
            
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
            self._cursor.execute("SELECT * FROM customers")
            customers = self._cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Address", "Check-in Date", "Check-out Date", "Room No.","User Email"]
            for customer in customers:
                table.add_row(customer)
            print(table)
        except Error as e:
            print(f"Error retrieving customers: {e}")
    def _my_bookings(self):
        
        try:
            # Query bookings associated with the user's email
            self._cursor.execute("SELECT * FROM bookings WHERE customer_email = %s", (self._user_email,))
            bookings = self._cursor.fetchall()
            if not bookings:
                print("No bookings found for the provided email.")
                return
            table = PrettyTable()
            table.field_names = ["Booking ID", "Room Number", "Customer Name", "User Email", "Check-in Date", "Check-out Date", "Total Bill"]
            for booking in bookings:
                table.add_row(booking)
            print(table)
        except Error as e:
            print(f"Error retrieving bookings: {e}")
    
    def user_logout(self):
        self._user_logged_in = False
        self._user_email = None
        print("User logged out successfully.")

    def admin_logout(self):
        self._admin_logged_in = False
        print("Admin logged out successfully.")



    def main(self):
        while True:
            if not self._admin_logged_in and not self._user_logged_in:
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
            elif self._admin_logged_in:
                print("1. Enter Customer Data")
                print("2. Calculate room rent")
                print("3. Calculate restaurant bill")
                print("4. Calculate laundry bill")
                print("5. Calculate game bill")
                print("6. Show total cost")
                print("7. Online Booking")
                print("8. Display Customers")
                print("9. Display All Rooms")
                print("10. Display All bookings")
                print("11. Add New User")
                print("12. Logout")
                
            
                print("13. EXIT")
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
                     self.display_bookings()
                elif choice == 11:
                    useremil=input('Enter user Email address=')
                    password=input('Enter user password=')
                    self._add_new_user(useremil,password)
                
                elif choice==12:
                    self.admin_logout()
                    
                elif choice == 13:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif self._user_logged_in:

                # User functionalities
                print("1. Online Booking")
                print("2.Show My Bookings")
                print("3.Lougout")
                # Other user functionalities...
                print("4. EXIT")
                user_choice = int(input("\nEnter your choice: "))
                if user_choice == 1:
                    self.online_booking()
                elif user_choice == 2:
                    self._my_bookings()
                elif user_choice == 3:
                    self.user_logout()
# Other user choices...
                elif user_choice == 4:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    hotel = Hotel()
    hotel_management = HotelManagement()
    hotel.main()
