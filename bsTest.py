import bs4
import requests
def main(url):
    

    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.status_code

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    doc = soup.get_text()
   
    soup.find_all('div', {"class" : "rw-expnded"})


    if 'rw-expnded' in soup:
        print("Desired item is in list")
    else: print ('Not shown')

url = ('https://finance.yahoo.com/quote/AAPL/financials?p=AAPL')

main(url)
