import pandas
import urllib.parse
from sqlalchemy import text
from sqlalchemy import create_engine as engine

class MainClass:
    def __init__(self, database_name: str, database_password: str, database_user_name: str = 'root',
                 database_connection_type: str = 'localhost'):
        self.database_name = database_name
        self.database_user_name = database_user_name
        self.database_connection_type = database_connection_type
        self.__password = urllib.parse.quote_plus(database_password)
        self.__database_connection = engine(
            F"mysql+pymysql://{self.database_user_name}:{self.__password}@{self.database_connection_type}/{self.database_name}"
        )

    def show_database_tables(self, database_name: str, table_name: str):
        with self.__database_connection.connect() as connection:
            # todo: right the SQL query to get all data from the specified table
            code = F"SELECT * FROM {database_name}.{table_name}"
            # todo: read sql query result into a pandas DataFrame and print it
            table = pandas.read_sql(sql=code, con=connection)
        # todo: print the retrieved table data
        print(table)

    def appending_data_to_table_employees(self, users_main_name: str, users_secondary_name: str,
                                          users_company_position: str, users_salary: float):
        # todo: right the SQL query to insert data in the employees table
        code = text(
            F"""CALL INSERT_NEW_EMPLOYEES_PROCEDURE(:users_main_name, :users_secondary_name, :users_company_position, :users_salary)""")
        # todo: execute the SQL query to insert data into the employees table using the provided parameters
        with self.__database_connection.connect() as connection:
            connection.execute(
                code,
                {
                    'users_main_name': users_main_name,
                    'users_secondary_name': users_secondary_name,
                    'users_company_position': users_company_position,
                    'users_salary': users_salary
                }
            )
            connection.commit()

    def appending_data_to_table_products(self, products_name: str, products_category: str, products_price: float):
        # todo: right the SQL query to insert data in the employees table
        code = text(
            F"""CALL INSERT_NEW_PRODUCTS_PROCEDURE(:products_name, :products_category, :products_price)""")
        # todo: execute the SQL query to insert data into the employees table using the provided parameters
        with self.__database_connection.connect() as connection:
            connection.execute(
                code,
                {
                    'products_name': products_name,
                    'products_category': products_category,
                    'products_price': products_price,
                }
            )
            connection.commit()
