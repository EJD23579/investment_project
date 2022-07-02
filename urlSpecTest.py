#url specificity test


ticker = input('Enter the stock ticker here as it appears on yahoo finance; the programme will do the rest: ')
#Input ticker only
baseURL = f'https://finance.yahoo.com/quote/{ticker}'

#O helped me out with f strings and simplifying the code down from slices.
#This was useful and I am learning ways to streamline programmes.

tickerURL = f'?p={ticker}'
SummURL = baseURL + tickerURL

#SummURL = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'


#Summary:
#https://finance.yahoo.com/quote/AAPL?p=AAPL


#Financials Page,Income Statement:
#https://finance.yahoo.com/quote/AAPL/financials?p=AAPL
IncomeURL = baseURL + r'/financials' + tickerURL

#Balance Sheet:
#https://finance.yahoo.com/quote/AAPL/balance-sheet?p=AAPL
BalanceURL = baseURL + r'/balance-sheet' + tickerURL

#Cash Flow:
#https://finance.yahoo.com/quote/AAPL/cash-flow?p=AAPL
CashURL = baseURL + r'/cash-flow' + tickerURL



print('\n' + 'Stock Summary URL: ' + SummURL + '\n')

print ('Income Statement URL: ' + IncomeURL + '\n')

print ('Balance Sheet URL: ' + BalanceURL+ '\n')

print ('Cash Flow URL: ' + CashURL+ '\n')






