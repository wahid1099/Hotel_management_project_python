from db_connection import connect_to_database
from prettytable import PrettyTable
from mysql.connector import Error
from restaurant import RestaurantMenu

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

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    @classmethod
    def display_info(cls):
        print("User information")
    

class Admin(User):
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "password"

    def __init__(self):
        super().__init__(self.ADMIN_USERNAME, self.ADMIN_PASSWORD)

    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.email and password == self.password:
            print("Admin login successful.")
            return True
        else:
            print("Invalid admin credentials. Please try again.")
            return False

class HotelUser(User):
    
    def __init__(self, email, password):
        super().__init__(email, password)
        self._db = connect_to_database()
        self._cursor = self._db.cursor()

    def user_login(self,username,password):
        
        try:
            self._cursor.execute("SELECT * FROM users WHERE email = %s AND pasword = %s", (username, password))
            user = self._cursor.fetchone()
            if user:
                print("User login successful.")
                self._user_logged_in = True
                self._user_email = username
                return True 
            else:
                print("Invalid user credentials. Please try again.")
        except Error as e:
            print(f"Error authenticating user: {e}")
            return False


class BookingDisplay:
    def __init__(self, cursor):
        self._cursor = cursor

    def display_bookings(self, email=None):
        query = "SELECT * FROM bookings"
        if email:
            query += " WHERE customer_email = %s"
            params = (email,)
        else:
            params = None

        try:
            self._cursor.execute(query, params)
            bookings = self._cursor.fetchall()
            if not bookings:
                print("No bookings found.")
                return
            
            table = PrettyTable()
            table.field_names = ["Booking ID", "Room Number", "Customer Name", "User Email", "Check-in Date", "Check-out Date", "Total Bill"]
            for booking in bookings:
                table.add_row(booking)
            print(table)
        except Error as e:
            print(f"Error retrieving bookings: {e}")
            
class Room:
    def __init__(self, room_type, amenities):
        self.room_type = room_type
        self.amenities = amenities
class Hotel(BookingDisplay):
   
    

        
    def __init__(self):
        self._admin_logged_in = False
        self._user_logged_in = False
        self._db = connect_to_database()
        self._cursor = self._db.cursor()
        self._user_email = None
        super().__init__(self._cursor)


        print("\n\n*****WELCOME TO DIU HOTEL MANAGEMENT SYSTEM*****\n")
       
        self.customers = []
        self.admin = Admin()
        self.restaurant_menu = RestaurantMenu()
        
    
    def display_restaurant_menu(self):
        self.restaurant_menu.display_menu()
    
    def place_order(self):
        self.display_restaurant_menu()
        item_id = input("Enter the ID of the item you want to order: ")
        self.restaurant_menu.place_order(item_id)
    
        

        
       
    
    
    def admin_login(self):
        self._admin_logged_in = self.admin.admin_login()
    
    def user_login(self):
        email = input("Enter your email: ")
        self._user_email=email
        password = input("Enter your password: ")
        user = HotelUser(email,password)

        self._user_logged_in = user.user_login(email, password)
       
       
    
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
       super().display_bookings()
    
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
        
       super().display_bookings(email=self._user_email)
    def user_logout(self):
        self._user_logged_in = False
        self._user_email = None
        print("User logged out successfully.")

    def admin_logout(self):
        self._admin_logged_in = False
        print("Admin logged out successfully.")
    
    def rooms_info(self):
        
        rooms = [
            Room("STANDARD NON-AC", "1 Double Bed, Television, Telephone, Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony, attached washroom with hot/cold water."),
            Room("STANDARD AC", "1 Double Bed, Television, Telephone, Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony, attached washroom with hot/cold water + Window/Split AC."),
            Room("3-Bed NON-AC", "1 Double Bed + 1 Single Bed, Television, Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table, Balcony with an Accent table with 2 Chair, attached washroom with hot/cold water."),
            Room("3-Bed AC", "1 Double Bed + 1 Single Bed, Television, Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table, Balcony with an Accent table with 2 Chair, attached washroom with hot/cold water + Window/Split AC.")
        ]

        print("         ------ HOTEL ROOMS INFO ------\n")
        for room in rooms:
            print(room.room_type)
            print("---------------------------------------------------------------")
            print(f"Room amenities include: {room.amenities}\n")



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
               
                print("2. Display Customers")
                print("3. Display All Rooms")
                print("4. Display All bookings")
                print("5. Add New User")
                print("6. Room Info")
                print("7. Logout")
                
            
                print("8. EXIT")
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    customer = self.input_customer_data()
                    
               
                elif choice == 2:
                    self.display_customers()
                
                elif choice == 3:
                    self.display_rooms()
                elif choice == 4:
                     self.display_bookings()
                elif choice == 5:
                    useremil=input('Enter user Email address=')
                    password=input('Enter user password=')
                    self._add_new_user(useremil,password)
                
                elif choice==6:
                    self.rooms_info()
                
                elif choice==7:
                    self.admin_logout()
                    
                elif choice == 8:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            elif self._user_logged_in:

                # User functionalities
                print("1. Online Booking")
                print("2.Show My Bookings")
                print("3.Show Food Menu")
                print("4.Lougout")
                # Other user functionalities...
                print("5. EXIT")
                user_choice = int(input("\nEnter your choice: "))
                if user_choice == 1:
                    self.online_booking()
                elif user_choice == 2:
                    self._my_bookings()
                elif user_choice == 3:
                    self.place_order()
                   # self.place_order_confirm()
                
                elif user_choice == 4:
                    self.user_logout()
                    
# Other user choices...
                elif user_choice == 5:
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    hotel = Hotel()
    # hotel_management = HotelManagement()
    hotel.main()
