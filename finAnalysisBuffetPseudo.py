# import modules:
#   - panda for dataframe
import pandas
#   - requests for scraping html page
import requests
#   - bs4 (beatiful soup) for identification of variable on yahoo
import bs4

#EXISTING CODE

def main(url):

    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.status_code

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    costOfRev = soup.select('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(2) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')
    #cost of revenue: 215,572,000

    print (costOfRev)
    print ('cost of revenue is ' + (costOfRev[0].text))

#convo with oli:    if __name__ == "__ main__":
url = input('Enter URL Here: ')


#url = input('Enter URL Here: ')
#https://finance.yahoo.com/quote/AAPL/financials?p=AAPL
main(url)


#EXISTING CODE

#PSEUDO CODE


#Add Ticker Search Code

#Find individual class types for each variable
#!!!Check O's suggestion code!!!

#Selenium to open dropdowns for each webpage
#Close Selenium

#Store variables from webpage

#Conditionals/Analysis from WB Book for each variable; put in individual programmes to simplify

#Combine Data as per WB Book for analysis of variables compared, i.e. p/e and cost of rev

#Provide numerical value for each variable and comparision of variables (as items themselves)

#Output a rank for the stock based on ??? Chess ??? Ranking algo/other algo
#Elo equation to rank stocks in stock list
#TrueSkill equation? or later

#

#Check Stock Price & Return Value

#Conditional for if stock is a buy

#Output variables in formatted table

#Store variables in a database in PostgreSQL
#Sector variable?
#Use Profile tab to see sector and industry to scrape info
#provide stock tables, sector tables

# TrueSkill to compare stocks in a sector based on rank




#PSEUDO CODE
