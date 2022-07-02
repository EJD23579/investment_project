import yfinance as yf
import pandas
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine

#Define connection string (if being pushed to github create a config.py file to hold variables!!!)
DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost:5432/Investment Analysis Project'

# SQL Engine
engine = create_engine(DATABASE_URI)


