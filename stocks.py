# Create a simple dictionary with ticker symbols and company names.

stockDict = {
    'GM': 'General Motors',
    'CAT':'Caterpillar',
    'EK':"Eastman Kodak"
}

#  Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 )
]

#  Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

new_company_dict = {}

def compute_purchase_price(company):
    total_price = company[1] * company[3]
    stock_ticker = company[0]
    full_company_name = stockDict[stock_ticker]
    print('I purchased {0} stocks from {1} at ${2} per share for a total cost of ${3}.'.format(company[1], full_company_name, company[3], '{0:.0f}'.format(total_price)))
    try:
        new_company_dict[stock_ticker].append(purchase)
    except KeyError:
        new_company_dict[stock_ticker] = list()
        new_company_dict[stock_ticker].append(purchase)

for purchase in purchases:
    compute_purchase_price(purchase)

# Create a second purchase summary that accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

print(new_company_dict)

for stock_ticker, purchases in new_company_dict.items():
    total_portfolio_stock_value = 0
    if len(purchases) > 1:
        total_stocks = purchases[0][1] + purchases[1][1]
        avg_price = (purchases[0][3] + purchases[1][3])/len(purchases)
        for item in purchases:
            total_portfolio_stock_value += item[1] * item[3]
            print(item)
        print('There were {0} stocks purchased from {1} at an average price of ${2}. The total value of the portfolio is ${3}'.format(total_stocks, purchases[0][0], '{0:.2f}'.format(avg_price), '{0:.2f}'.format(total_portfolio_stock_value)))
    else:
        total_portfolio_stock_value = purchases[0][1] * purchases[0][3]
        print('There were {0} stocks purchased from {1} at an average price of ${2}. The total value of the portfolio is ${3}'.format(purchases[0][1], purchases[0][0], '{0:.2f}'.format(purchases[0][3]), '{0:.2f}'.format(total_portfolio_stock_value)))

