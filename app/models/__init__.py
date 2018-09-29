"""This file contains the database class that contains all database related methods"""
from pprint import pprint
from urllib.parse import urlparse

import psycopg2
import os


class Database:
    def __init__(self):
        try:
            if os.environ['FLASK_ENV'] == 'development':
                result = urlparse("postgresql://localhost/test")
            else:
                result = urlparse("postgresql://localhost/fastfood")
            username = 'postgres'
            password = 'asP2#fMe'
            database = result.path[1:]
            hostname = result.hostname
            portno = 5432
            self.connection = psycopg2.connect(
                database=database,
                user=username,
                password=password,
                host=hostname,
                port=portno
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database")

    def create_table(self, table_name, table_columns):
        """method creates a single table"""
        create_table_command = "CREATE TABLE IF NOT EXISTS %s(%s);" % (
            table_name, table_columns)
        self.cursor.execute(create_table_command)

    def drop_table(self, table_name):
        """method drops a single table from the database"""
        drop_table_command = "DROP TABLE %s" % (table_name)
        self.cursor.execute(drop_table_command)

    def create_all_tables(self):
        """method creates the tables needed for the application"""
        self.create_table('users', "user_id SERIAL PRIMARY KEY, email text " +
                          " NOT NULL UNIQUE, name text NOT NULL, password text NOT NULL, role boolean NOT NULL")
        self.create_table('menu', "menu_id SERIAL PRIMARY KEY, name text " +
                          " NOT NULL UNIQUE, description text NOT NULL, price int NOT NULL")

    def drop_all_tables(self):
        self.drop_table('users')
        self.drop_table('menu')

    def check_tables(self):
        self.cursor.execute(
            "select exists(select * from information_schema.tables where table_name=%s)", ('users',))
        return self.cursor.fetchone()[0]

    def query_single(self, email):
        """returns a user given the user's email"""
        self.cursor.execute("SELECT * FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def query_entire_table(self, table_name):
        """returns all records in table"""
        self.cursor.execute("SELECT row_to_json(row) FROM (SELECT * FROM %s) row" %
                            (table_name))
        items = self.cursor.fetchall()
        return items

    def query_single_row(self, table_name, table_column, row_id):
        """returns a single row from table_name where table_column = row_id"""
        self.cursor.execute("SELECT row_to_json(row) FROM (SELECT * FROM %s WHERE %s = '%s') row" %
                            (table_name, table_column, row_id))
        item = self.cursor.fetchone()
        return item

    def return_id(self, email):
        """method returns users's id from databse"""
        self.cursor.execute(
            "SELECT user_id FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def return_password(self, email):
        """method returns uers's hashed password from database"""
        self.cursor.execute(
            "SELECT password FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def return_role(self, email):
        """method returns uers's hashed password from database"""
        self.cursor.execute(
            "SELECT role FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

#db = Database()
# db.create_all_tables()
# if not db.check_tables():
#     db.create_all_tables()

#item = db.return_password("arthur@truit.com")
# print(item[0])
# print(db.return_user_id_question(2))
