# restaurant.py

class RestaurantMenu:
    def __init__(self):
        self.menu = {
            "1": {"name": "Regular Tea", "price": 20.00},
            "2": {"name": "Masala Tea", "price": 25.00},
            "3": {"name": "Coffee", "price": 25.00},
            "4": {"name": "Cold Drink", "price": 25.00},
            "5": {"name": "Bread Butter", "price": 30.00},
            "6": {"name": "Bread Jam", "price": 30.00},
            "7": {"name": "Veg. Sandwich", "price": 50.00},
            "8": {"name": "Veg. Toast Sandwich", "price": 50.00},
            "9": {"name": "Cheese Toast Sandwich", "price": 70.00},
            "10": {"name": "Grilled Sandwich", "price": 70.00},
            "11": {"name": "Tomato Soup", "price": 110.00},
            "12": {"name": "Hot & Sour", "price": 110.00},
            "13": {"name": "Veg. Noodle Soup", "price": 110.00},
            "14": {"name": "Sweet Corn", "price": 110.00},
            "15": {"name": "Veg. Munchow", "price": 110.00},
            "16": {"name": "Shahi Paneer", "price": 110.00},
            "17": {"name": "Kadai Paneer", "price": 110.00},
            "18": {"name": "Handi Paneer", "price": 120.00},
            "19": {"name": "Palak Paneer", "price": 120.00},
            "20": {"name": "Chilli Paneer", "price": 140.00},
            "21": {"name": "Matar Mushroom", "price": 140.00},
            "22": {"name": "Mix Veg", "price": 140.00},
            "23": {"name": "Jeera Aloo", "price": 140.00},
            "24": {"name": "Malai Kofta", "price": 140.00},
            "25": {"name": "Aloo Matar", "price": 140.00},
            "26": {"name": "Dal Fry", "price": 140.00},
            "27": {"name": "Dal Makhani", "price": 150.00},
            "28": {"name": "Dal Tadka", "price": 150.00},
            "29": {"name": "Plain Roti", "price": 15.00},
            "30": {"name": "Butter Roti", "price": 15.00},
            "31": {"name": "Tandoori Roti", "price": 20.00},
            "32": {"name": "Butter Naan", "price": 20.00},
            "33": {"name": "Plain Rice", "price": 90.00},
            "34": {"name": "Jeera Rice", "price": 90.00},
            "35": {"name": "Veg Pulao", "price": 110.00},
            "36": {"name": "Peas Pulao", "price": 110.00},
            "37": {"name": "Plain Dosa", "price": 100.00},
            "38": {"name": "Onion Dosa", "price": 110.00},
            "39": {"name": "Masala Dosa", "price": 130.00},
            "40": {"name": "Paneer Dosa", "price": 130.00},
            "41": {"name": "Rice Idli", "price": 130.00},
            "42": {"name": "Sambhar Vada", "price": 140.00},
            "43": {"name": "Vanilla Ice Cream", "price": 60.00},
            "44": {"name": "Strawberry Ice Cream", "price": 60.00},
            "45": {"name": "Pineapple Ice Cream", "price": 60.00},
            "46": {"name": "Butter Scotch Ice Cream", "price": 60.00},
        }

    def display_menu(self):
        print("-------------------------------------------------------------------------")
        print("                           Hotel AnCasa")
        print("-------------------------------------------------------------------------")
        print("                            Menu Card")
        print("-------------------------------------------------------------------------")
        print("\n BEVARAGES                              26 Dal Fry................ 140.00")
        print("----------------------------------      27 Dal Makhani............ 150.00")
        print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
        print(" 2  Masala Tea.............. 25.00")
        print(" 3  Coffee.................. 25.00      ROTI")
        print(" 4  Cold Drink.............. 25.00     ----------------------------------")
        print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
        print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
        print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
        print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
        print(" 9  Cheese Toast Sandwich... 70.00")
        print(" 10 Grilled Sandwich........ 70.00      RICE") 
        print("                                       ----------------------------------")
        print(" SOUPS                                  33 Plain Rice.............. 90.00")
        print("----------------------------------      34 Jeera Rice.............. 90.00")
        print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
        print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
        print(" 13 Veg. Noodle Soup....... 110.00")
        print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
        print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
        print("                                        37 Plain Dosa............. 100.00")
        print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
        print("----------------------------------      39 Masala Dosa............ 130.00")
        print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
        print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
        print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00")
        print(" 19 Palak Paneer........... 120.00")
        print(" 20 Chilli Paneer.......... 140.00      ICE CREAM")
        print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
        print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
        print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
        print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00")
        print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
    
    def place_order(self, item_id):
        menu_item = self.menu.get(item_id)
        if not menu_item:
            print("Invalid item ID. Please try again.")
            return
        print(f"Ordered: {menu_item['name']} - Price: {menu_item['price']}")
