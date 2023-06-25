class RentalPropertyCalculator:
    def __init__(self, purchase_price, rehab_cost, monthly_rent, expenses):
        self.purchase_price = purchase_price
        self.rehab_cost = rehab_cost
        self.montly_rent = monthly_rent
        self.expenses = expenses

    def calculate_roi(self):
        total_investment = self.purchase_price + self.rehab_cost
        annual_rent = self.montly_rent * 12
        annual_expenses = self.expenses * 12

        net_income = annual_rent - annual_expenses
        roi = (net_income / total_investment) * 100

        return roi
    
purchase_price = 200000
rehab_cost = 5000
monthly_rent = 1500
expenses = 1000

calculator = RentalPropertyCalculator(purchase_price, rehab_cost, monthly_rent, expenses)
roi = calculator.calculate_roi()

print(f"The ROI for the rental property is: {roi:.2f}%")