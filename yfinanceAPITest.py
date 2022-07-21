import yfinance as yf
import pandas
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
#Below user/password/Port No. edited out for privacy
#from sqlalchemy import create_engine
#engine = sqlalchemy.create_engine('postgresql://USER:PASSWORD@localhost:PORT_NO./Investment Analysis Project')

#df.to_sql('table_name', engine)

aapl = yf.Ticker("AAPL")

income = aapl.financials

balanceSheet = aapl.balance_sheet

cashFlow = aapl.cashflow

earnings = aapl.earnings
# username/password and port no. edited out for privacy
#Define connection string (if being pushed to github create a config.py file to hold variables!!!)
DATABASE_URI = 'postgresql+psycopg2://USERNAME:PASSWORD@PORT_NO./Investment Analysis Project'

# SQL Engine
engine = create_engine(DATABASE_URI)



def showInfo():
    pandas.set_option('display.max_columns',4)
    print (income)
    print (balanceSheet)
    print (cashFlow)
    print (earnings)

showInfo()

income.to_sql('investment_data_income',engine)

# add this? sqlalchemy.engine.Connection.close()





          





