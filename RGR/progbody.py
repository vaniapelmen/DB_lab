import time
from dbcon import Model
from visual import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()


    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")


    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()
            if table == '6':
                break
            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)


    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding customer:")
            self.add_customer()
        elif table == '2':
            self.view.show_message("\nAdding trcomp:")
            self.add_trcomp()
        elif table == '3':
            self.view.show_message("\nAdding travel:")
            self.add_travel()
        elif table == '4':
            self.view.show_message("\nAdding place:")
            self.add_place()
        else:
            self.view.show_message("Wrong choice. Try again.")


    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random customer:")
            self.add_random_fields()
        else:
            self.view.show_message("Wrong choice. Try again.")


    def process_view_option(self, table):
        if table == '1':
            self.view_customers()
        elif table == '2':
            self.view_trcomps()
        elif table == '3':
            self.view_travels()
        elif table == '4':
            self.view_places()
        elif table == '5':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")


    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating customer:")
            self.update_customer()
        elif table == '2':
            self.view.show_message("\nUpdating trcomp:")
            self.update_trcomp()
        elif table == '3':
            self.view.show_message("\nUpdating travel:")
            self.update_travel()
        elif table == '4':
            self.view.show_message("\nUpdating place:")
            self.update_place()
        else:
            self.view.show_message("Wrong choice. Try again.")


    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting customer:")
            self.delete_customer()
        elif table == '2':
            self.view.show_message("\nDeleting trcomp:")
            self.delete_trcomp()
        elif table == '3':
            self.view.show_message("\nDeleting travel:")
            self.delete_travel()
        elif table == '4':
            self.view.show_message("\nDeleting place:")
            self.delete_place()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_search_option(self):
        option = self.view.show_search()
        if option == '1':
            start_time = time.time()
            self.Customer_Company12_Show()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Time: {elapsed_time:.2f} мс")
        elif option == '2':
            start_time = time.time()
            self.Travel_Type12_Show()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Time: {elapsed_time:.2f} мс")
        elif option == '3':
            start_time = time.time()
            self.Customer_Travel_To12_Show()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Time: {elapsed_time:.2f} мс")
        else:
            self.view.show_menu()

    def add_customer(self):
        try:
            name, phone, email, travel_id, comp_id, place_id = self.view.get_customer_input()
            self.model.add_customer(name, phone, email, travel_id, comp_id, place_id)
            self.view.show_message("Customer added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def add_trcomp(self):
        try:
            comp_name, comp_address, comp_phone = self.view.get_trcomp_input()
            self.model.add_trcomp(comp_name, comp_address, comp_phone)
            self.view.show_message("Trcomp added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def add_travel(self):
        try:
            time, form, pay = self.view.get_travel_input()
            self.model.add_travel(time, form, pay)
            self.view.show_message("Travel added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def add_place(self):
        try:
            country, city = self.view.get_place_input()
            self.model.add_place(country, city)
            self.view.show_message("Place added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def view_customers(self):
        try:
            customers = self.model.get_all_customers()
            self.view.show_customers(customers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def view_trcomps(self):
        try:
            trcomps = self.model.get_all_trcomps()
            self.view.show_trcomps(trcomps)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def view_travels(self):
        try:
            travels = self.model.get_all_travels()
            self.view.show_travels(travels)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def view_places(self):
        try:
            places = self.model.get_all_places()
            self.view.show_places(places)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def Customer_Company12_Show(self):
        try:
            rows = self.model.Customer_Company12()
            self.view.Customer_Company12_Show(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def Travel_Type12_Show(self):
        try:
            self.view.show_message("\nYou need to enter the travel_id.")
            number = self.view.get_number()
            rows = self.model.Travel_Type12(number)
            self.view.Travel_Type12_Show(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def Customer_Travel_To12_Show(self):
        try:
            rows = self.model.Customer_Travel_To12()
            self.view.Customer_Travel_To12_Show(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_customer(self):
        try:
            customer_id = self.view.get_customer_id()
            name, phone, email, travel_id, comp_id, place_id = self.view.get_customer_input()
            self.model.update_customer(customer_id, name, phone, email, travel_id, comp_id, place_id)
            self.view.show_message("Customer updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def update_trcomp(self):
        try:
            comp_id = self.view.get_trcomp_id()
            comp_name, comp_address, comp_phone = self.view.get_trcomp_input()
            self.model.update_trcomp(comp_id, comp_name, comp_address, comp_phone)
            self.view.show_message("Trcomp updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def update_travel(self):
        try:
            travel_id = self.view.get_travel_id()
            time, form, pay = self.view.get_travel_input()
            self.model.update_travel(travel_id, time, form, pay)
            self.view.show_message("Travel updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def update_place(self):
        try:
            place_id = self.view.get_place_id()
            country, city = self.view.get_place_input()
            self.model.update_place(place_id, country, city)
            self.view.show_message("Place updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def delete_customer(self):
        try:
            customer_id = self.view.get_customer_id()
            self.model.delete_customer(customer_id)
            self.view.show_message("Customer deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def delete_trcomp(self):
        try:
            trcomp_id = self.view.get_trcomp_id()
            self.model.delete_trcomp(trcomp_id)
            self.view.show_message("Trcomp deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def delete_travel(self):
        try:
            travel_id = self.view.get_travel_id()
            self.model.delete_travel(travel_id)
            self.view.show_message("Travel deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def delete_place(self):
        try:
            place_id = self.view.get_place_id()
            self.model.delete_place(place_id)
            self.view.show_message("Place deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")


    def add_random_fields(self):
        try:
            number = self.view.get_number()
            self.model.add_random_fields(number)
            self.view.show_message("Random fields added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")
