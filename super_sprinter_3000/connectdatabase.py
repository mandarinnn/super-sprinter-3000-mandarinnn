from peewee import *


class ConnectDatabase:

    def get_connect_string():
        with open('connect_str.txt', "r") as db_name:
            return db_name.readline().strip()

    db = PostgresqlDatabase(get_connect_string())
