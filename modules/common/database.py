import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"D:/PrometheusGitHub/Anastasiia-Buriakova-QA-Automation"
            + r"/become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)  
        record = self.cursor.fetchall() 
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"  # read
        self.cursor.execute(query)  # request to DB
        record = self.cursor.fetchall()  #assigning the result of execution
        return record

    def get_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"  
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()  # confirmation of changes in the database so as not to accidentally change data that you did not want

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_customer_name_by_id(self, customer_id, name):
        query = f"UPDATE customers SET name = '{name}' WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit() 

    def select_customer_name_by_id(self, customer_id):
        query = f"SELECT name FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchone() #to get a single record
        return record[0] if record else None 
    
    def get_address_by_the_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"  
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record
    
    def select_product_name_by_id(self, product_id):
        query = f"SELECT name FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record[0] if record else None 
    
        #negative testing if database accept letters instead of numbers:
    def insert_quantity_as_letters(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}','{qnt}')"
        self.cursor.execute(query)
        self.connection.commit()

        
