class Company:
    def __init__(self, name, employees, year, stock_price, revenue):
        super().__init__()
        self.name = name
        self.employees = employees
        self.year = year
        self.stock_price = stock_price
        self.revenue = revenue

    def is_older(self, other):
        return self.year < other.year

    def revenue_per_employee(self):
        return self.revenue / self.employees
