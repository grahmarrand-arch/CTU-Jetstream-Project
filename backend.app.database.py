"""
database.py
Creates and returns a connection to the Jetstream MySQL database.
This file is intentionally isolated so the UI team or other backend
modules can reuse the same connection logic without rewriting anything.

"""

import mysql.connector

def get_connection():
    """
    Returns a MySQL connection object.
    This allows the search module to run independently OR be imported
    into a larger backend system without modification.
    """
    return mysql.connector.connect(
        host="localhost",              # Local DB for development
        user="your_mysql_user",        # Replace with your MySQL username
        password="your_mysql_password",# Replace with your MySQL password
        database="jetstream"           # Database containing the flights table
    )