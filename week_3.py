#questiin 1

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:                      discount = price * (discount_percent / 100)                                             return price - discount                 return price


#question 2

price=float(input("Enter price: "))
discount_percent=float(input("Enter discount percent: "))
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price
print(calculate_discount(price,discount_percent))
