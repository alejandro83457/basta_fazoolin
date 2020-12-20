class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        """String representation of object"""
        return '{name} menu will be available form {start_time} to {end_time}'.format(name=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        """Calculates the amount depending on items purchased"""
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        """String representation of object"""
        return 'Franchise at {address}.'.format(address)

    def available_menus(self, time):
        """Prints out the menu depending on the time"""
        # Brunch conditional
        if menus[0].start_time <= time < menus[0].end_time:
            print('Brunch Menu:')
            for item, price in self.menus[0].items.items():
                print(item, price)
            print()
        # Early Bird conditionl
        if menus[1].start_time <= time < menus[1].end_time:
            print('Early Bird Menu:')
            for item, price in self.menus[1].items.items():
                print(item, price)
            print()
        # Dinner conditional
        if menus[2].start_time <= time < menus[2].end_time:
            print('Dinner Menu:')
            for item, price in self.menus[2].items.items():
                print(item, price)
            print()
        # Kids conditional
        if menus[3].start_time <= time < menus[3].end_time:
            print('Kids Menu:')
            for item, price in self.menus[3].items.items():
                print(item, price)
            print()


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Menu items
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

# Menu objects
brunch = Menu('brunch', brunch_items, 1100, 1600)
early_bird = Menu('early bird', early_bird_items, 1500, 1800)
dinner = Menu('dinner', dinner_items, 1700, 2300)
kids = Menu('kids', kids_items, 1100, 2100)

# Franchise addresses
west_end_road_address = '1232 West End Road'
east_mulberry_street_address = '12 East Mulberry Street'

# All menu objects in a list
menus = [brunch, early_bird, dinner, kids]

# Franchise objects
west_end_road = Franchise(west_end_road_address, menus)
east_mulberry_street = Franchise(east_mulberry_street_address, menus)

# TEST
# print(brunch)

# TESTING calculate_bill()
brunch_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
early_bird_bill = early_bird.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)'])
# print(brunch_bill)
# print(early_bird_bill)

# TESTING available_menus
# west_end_road.available_menus(1200)

# Take a' Arepa Menu Items
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# Take a' Arepa Menu Object
arepas_menu = Menu('arepas', arepas_items, 1000, 2000)

# Take a' Arepa address
arepas_address = '189 Fitzgerald Avenue'

# Take a' Arepa franchise object
arepas_place = Franchise(arepas_address, [arepas_items])

# Take a' Arepad business object
arepas_business = Business("Take a' Arepa", [arepas_place])

# Update test
