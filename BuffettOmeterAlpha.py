import bs4
import requests
def main(url):
    

    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.status_code

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(2) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')
    #cost of revenue: 215,572,000

    print (elems)
    print ('cost of revenue is ' + (elems[0].text))
    
    test = soup.select('#Col1-1-Financials-Proxy > section > div.Pos\(r\) > div.W\(100\%\).Whs\(nw\).Ovx\(a\).BdT.Bdtc\(\$seperatorColor\) > div > div.D\(tbrg\) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div.D\(tbr\).fi-row.Bgc\(\$hoverBgColor\)\:h > div:nth-child(2) > span')

    print ('the test value is: ' + str(test))

#convo with oli:    if __name__ == "__ main__":
url = ('https://finance.yahoo.com/quote/AAPL/financials?p=AAPL')
#url = input('Enter URL Here: ')
#https://finance.yahoo.com/quote/AAPL/financials?p=AAPL
main(url)


