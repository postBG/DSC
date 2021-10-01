from P1 import Company  # Do Not Modify


class Industry:
    def __init__(self, type, companies):
        super().__init__()
        self.type = type
        self.companies = companies

    def average_stock_price(self):
        stock_prices = [company.stock_price for company in self.companies]
        return sum(stock_prices) / len(stock_prices)
