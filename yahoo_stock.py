from urllib import request

symbol = input("Please enter a valid stock symbol :")

stock_url = "http://real-chart.finance.yahoo.com/table.csv?s=" + symbol + "&d=0&e=31&f=2016&g=d&a=2&b=13&c=1986&ignore=.csv"
print (stock_url)

# stock_url="http://real-chart.finance.yahoo.com/table.csv?s=MSFT&d=0&e=31&f=2016&g=d&a=2&b=13&c=1986&ignore=.csv"

def download_stock_data(stock_url):
    response = request.urlopen(stock_url)
    csv=response.read()
    csv_str = str(csv)
    print (csv_str)
    lines = csv_str.split("\\n")
    print (lines)
    stock_file=open(symbol + '_prices.csv', 'w')
    for line in lines:
        stock_file.write(line + "\n")
    stock_file.close()


download_stock_data(stock_url)

