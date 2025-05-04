import pandas as pd
import os
import yfinance as yf

def create_alert_file(ticker, high, low):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d").Close.iloc[0]
    if current_price >= high:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "ALERT.txt")
        with open(file_path, "w") as file:
            file.write(f"This is an alert that {ticker} hit the upper limit, sell now to cash in!")
    if current_price <= low:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "ALERT.txt")
        with open(file_path, "w") as file:
            file.write(f"This is an alert that {ticker} hit the lower limit, sell now to avoid more losses!")

create_alert_file('XOM', 114 , 92)
create_alert_file('MSFT', 457 , 367)
create_alert_file('WBD', 12.32 , 6)
create_alert_file('HOG', 48 , 22)
create_alert_file('SCHG', 28 , 22)
create_alert_file('ITOT', 134 , 108)
create_alert_file('SCHB', 22 , 18)
create_alert_file('SPLG', 73 , 59)
create_alert_file('SPYV', 55 , 45)
create_alert_file('IJH', 65 , 52)
create_alert_file('SWPPX', 97 , 79)
