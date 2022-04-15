import requests
from bs4 import BeautifulSoup

URL = 'https://coinmarketcap.com/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
           'accept': '*/*'}


def get_html(url):
    r = requests.get(url=url, headers=HEADERS)
    return r


def get_content(html, currency_list):
    soup = BeautifulSoup(html, "html.parser")
    coins = soup.find("tbody").find_all("tr")
    for coin in coins:
        name = coin.find(class_="cmc-link").get("href").replace("/currencies/", "")[:-1]
        price = coin.find(class_="sc-131di3y-0 cLgOOr")
        market_cap = coin.find(class_="sc-1ow4cwt-1 ieFnWP")
        if price:
            currency_list.append({
                'Name': name,
                'Price': price.text,
                'Market-Cap': market_cap.text
            })

           # print(f"{name}: {price.text}  {market_cap.text}")
        else:
            break
    print_list(currency_list)


def find_by_name_in_list(lst, key):
    for str in lst:
        if (str['Name'] == key):
            print(str['Name'] + ":  " + str['Price'] + "   " + str['Market-Cap'])


def print_list(lst):
    print('Name\t Price\t Market-Cap')
    for str in lst:
        print(str['Name'] + ":  " + str['Price'] + "   " + str['Market-Cap'])


def parse(currency_list):
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text, currency_list)
    else:
        print("")

if __name__ == '__main__':
    currency_list = []
    parse(currency_list)
    key = input('Enter F to find crypto coin by name, Q to quit\nInput: ')
    while key!= 'Q':
        if key == 'F':
            crypto_coin_name = input('Enter a crypto coin name to get info\nInput: ')
            find_by_name_in_list(currency_list, crypto_coin_name)

        key = input('Enter F to find crypto coin by name, Q to quit\nInput: ')
