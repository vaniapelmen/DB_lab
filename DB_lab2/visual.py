class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1.Add line")
        self.show_message("2.Show table")
        self.show_message("3.Update line")
        self.show_message("4.Delete line")
        self.show_message("5.Exit")
        choice = input("Choose: ")
        return choice

    def show_tables(self):
        self.show_message("\nTables:")
        self.show_message("1.Customer")
        self.show_message("2.Trav_comp")
        self.show_message("3.Travel")
        self.show_message("4.Place")
        self.show_message("5.Back to menu")
        table = input("Choose table: ")
        return table

    def show_search(self):
        self.show_message("\nSearch:")
        self.show_message("1. Customer & Company")
        self.show_message("2. Travel type")
        self.show_message("3. Customer travel to list")
        self.show_message("4. Menu")
        choice = input("Choose: ")
        return choice

    @staticmethod
    def show_travels(travels):
        print("\nTravels:")
        for travel in travels:
            print(f"ID: {travel[0]}, Time: {travel[1]}, Form: {travel[2]}, Pay: {travel[3]}")

    @staticmethod
    def show_places(places):
        print("\nplaces:")
        for place in places:
            print(f"ID: {place[0]}, Country: {place[1]}, City: {place[2]}")

    @staticmethod
    def show_trcomps(trcomps):
        print("\ntrcomps:")
        for trcomp in trcomps:
            print(f"ID: {trcomp[0]}, Name: {trcomp[1]}, Address: {trcomp[2]}, Phone: {trcomp[3]}")

    @staticmethod
    def show_customers(customers):
        print("\ncustomer:")
        for customer in customers:
            print(
                f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}, Email: {customer[3]}, travel_id: {customer[4]}, comp_id: {customer[5]}, place_id: {customer[6]}")

    @staticmethod
    def Customer_Company12_Show(rows):
        print("\nSort by Trcomp_id:")
        for row in rows:
            print(f"TRcomp ID: {row[0]}, Customer name: {row[1]}, Company name:{row[2]}")

    @staticmethod
    def Travel_Type12_Show(rows):
        print("\nSorting by travel_id:")
        for row in rows:
            print(f"customer: {row[0]}, travel_id: {row[1]}")

    @staticmethod
    def Customer_Travel_To12_Show(rows):
        print("\nTravel-Name-Place:")
        for row in rows:
            print(f'Travel id: {row[0]} Name customer: {row[1]} Travel to: {row[2]}.')

    @staticmethod
    def get_customer_input():
        while True:
            try:
                name = input("Enter customer name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                phone = input("Enter customer phone: ")
                if phone.strip():
                    phone = float(phone)
                    break
                else:
                    print("Phone cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                email = input("Enter customer email: ")
                if email.strip():
                    break
                else:
                    print("Email cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                travel_id = int(input("Enter customer travel_id: "))
                break
            except ValueError:
                print("Travel_id must be a number.")
        while True:
            try:
                comp_id = int(input("Enter customer comp_id: "))
                break
            except ValueError:
                print("Comp_id must be a number.")
        while True:
            try:
                place_id = int(input("Enter customer place_id: "))
                break
            except ValueError:
                print("Place_id must be a number.")
        return name, phone, email, travel_id, comp_id, place_id

    @staticmethod
    def get_trcomp_input():
        while True:
            try:
                comp_name = input("Enter trcomp comp_name: ")
                if comp_name.strip():
                    break
                else:
                    print("Comp_name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                comp_address = input("Enter trcomp comp_address: ")
                if comp_address.strip():
                    break
                else:
                    print("Comp_address cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                comp_phone = input("Enter trcomp comp_phone: ")
                if comp_phone.strip():
                    break
                else:
                    print("Comp_phone cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return comp_name, comp_address, comp_phone

    @staticmethod
    def get_travel_input():
        while True:
            try:
                time = input("Enter travel time: ")
                if time.strip():
                    break
                else:
                    print("Time cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                form = input("Enter travel form: ")
                if form.strip():
                    break
                else:
                    print("Form cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                pay = input("Enter travel pay: ")
                if pay.strip():
                    break
                else:
                    print("Pay cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return time, form, pay

    @staticmethod
    def get_place_input():
        while True:
            try:
                country = input("Enter place country: ")
                if country.strip():
                    break
                else:
                    print("Country cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                city = input("Enter place city: ")
                if city.strip():
                    break
                else:
                    print("City cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return country, city

    @staticmethod
    def get_customer_id():
        while True:
            try:
                id = int(input("Enter customer ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_trcomp_id():
        while True:
            try:
                id = int(input("Enter trcomp ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_travel_id():
        while True:
            try:
                id = int(input("Enter travle ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_place_id():
        while True:
            try:
                id = int(input("Enter place ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_task_id():
        while True:
            try:
                id = int(input("Enter task ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def get_number():
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number
