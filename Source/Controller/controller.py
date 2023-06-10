import sqlite3 as sql
import requests as http
import pandas as pd
import threading
import xlwt


def get_quotation():
    # Makes an HTTP request to get real-time quotes
    res = http.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    data = res.json()
    dolar = data['USDBRL']["bid"]
    euro = data['EURBRL']["bid"]
    bitcoin = data['BTCBRL']["bid"]
    
    # Store quotes in a dictionary
    quotations = {
        'USD': float(dolar),
        'EUR': float(euro),
        'BTC': float(bitcoin)
    }
    
    return quotations


def create_database():
    # Creates a connection to the SQLite database and creates the "transactions" table
    with sql.connect('./Source/Cache/data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS transações (
                Título TEXT,
                Valor REAL,
                Categoria TEXT
            )
            '''
        )


def add_transaction(title, value, category, func_clear):
    # Adds a transaction to the SQLite database
    with sql.connect('./Source/Cache/data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(" INSERT INTO transações VALUES (:Título, :Valor, :Categoria)", 
                {
                    'Título' : title,
                    'Valor' : value,
                    'Categoria' : category
                }
            )
    func_clear()


def export_transaction():
    # Exports recorded transactions to an Excel file
    with sql.connect('./Source/Cache/data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT *, oid FROM transações")
        transaction_registed = cursor.fetchall()
    
    # Creates a pandas DataFrame with the recorded transactions
    transaction_registed = pd.DataFrame(transaction_registed, columns=['Título', 'Valor', 'Categoria', 'Items'])
    
    # Save the DataFrame as an Excel file using the xlwt package
    transaction_registed.to_excel('./Files/transactions.xlsx', index=False)
