import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='123qwertyuiop',
            host='localhost',
            port=5432
        )


    def add_customer(self, name, phone, email, travel_id, comp_id, place_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO customer (name, phone, email, travel_id, comp_id, place_id) VALUES (%s, %s, %s, %s, %s, %s)',(name, phone, email, travel_id, comp_id, place_id))
        self.conn.commit()


    def add_trcomp(self, comp_name, comp_address, comp_phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO trcomp (comp_name, comp_address, comp_phone)VALUES (%s, %s, %s)',(comp_name, comp_address, comp_phone))
        self.conn.commit()


    def add_travel(self, time, form, pay):
        c = self.conn.cursor()
        c.execute('INSERT INTO travel (time, form, pay) VALUES (%s, %s, %s)', (time, form, pay))
        self.conn.commit()


    def add_place(self, country, city):
        c = self.conn.cursor()
        c.execute('INSERT INTO place (country, city) VALUES (%s, %s)', (country, city))
        self.conn.commit()


    def get_all_customers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM customer')
        return c.fetchall()


    def get_all_trcomps(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM trcomp')
        return c.fetchall()


    def get_all_travels(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM travel')
        return c.fetchall()


    def get_all_places(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM place')
        return c.fetchall()


    def update_customer(self, customer_id, name, phone, email, travel_id, comp_id, place_id):
        c = self.conn.cursor()
        c.execute('UPDATE customer SET name=%s, phone=%s, email=%s, travel_id=%s, comp_id=%s, place_id=%s WHERE customer_id=%s',(name, phone, email, travel_id, comp_id, place_id, customer_id))
        self.conn.commit()


    def update_trcomp(self, comp_id, comp_name, comp_address, comp_phone):
        c = self.conn.cursor()
        c.execute('UPDATE trcomp SET comp_name=%s, comp_address=%s, comp_phone=%s WHERE comp_id=%s',(comp_name, comp_address, comp_phone, comp_id))
        self.conn.commit()


    def update_travel(self, travel_id, time, form, pay):
        c = self.conn.cursor()
        c.execute('UPDATE travel SET time=%s, form=%s, pay=%s WHERE travel_id=%s', (time, form, pay, travel_id))
        self.conn.commit()


    def update_place(self, place_id, country, city):
        c = self.conn.cursor()
        c.execute('UPDATE place SET country=%s, city=%s WHERE place_id=%s', (country, city, place_id))
        self.conn.commit()


    def delete_customer(self, customer_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM customer WHERE customer_id=%s', (customer_id,))
        self.conn.commit()


    def delete_trcomp(self, trcomp_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM trcomp WHERE trcomp_id=%s', (trcomp_id,))
        self.conn.commit()


    def delete_travel(self, travel_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM travel WHERE travel_id=%s', (travel_id,))
        self.conn.commit()


    def delete_place(self, place_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM place WHERE place_id=%s', (place_id,))
        self.conn.commit()


    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute(
            'INSERT INTO customer (name, phone, email, travel_id, comp_id, place_id) SELECT chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), trunc(random() * 1000000000), chr(trunc(65 + random() * 25)::int) || trunc(random() * 100) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), trunc(random() * 5) + 1, trunc(random() * 4) + 1, trunc(random() * 7) + 1 FROM generate_series(1, %s)',(number,))
        self.conn.commit()

    def Customer_Company12(self):
        c = self.conn.cursor()
        c.execute('SELECT customer.comp_id, customer.name AS customer_name, trcomp.comp_name AS trcomp_name FROM customer LEFT JOIN trcomp ON trcomp.comp_id = customer.comp_id ORDER BY comp_id;')
        return c.fetchall()


    def Travel_Type12(self, number):
        c = self.conn.cursor()
        c.execute('SELECT customer.name AS customer_name, customer.travel_id FROM customer WHERE customer.travel_id = %s;', (number,))
        return c.fetchall()


    def Customer_Travel_To12(self):
        c = self.conn.cursor()
        c.execute('SELECT customer.place_id, customer.name AS customer_name, place.city AS place_city FROM customer LEFT JOIN place ON place.place_id = customer.place_id GROUP BY customer.place_id, place.place_id, customer.name ORDER BY place_id;')
        return c.fetchall()