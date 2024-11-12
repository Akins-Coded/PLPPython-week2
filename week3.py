def calculate_discount(price, discount_percent):
    if discount >= 20:
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return f"You product Cost ${final_price} with ${discount_amount} Discount"

    else: 
        return f"Your product costs {price}"

price = float(input("Enter The Original price of the Product: "))
discount = float(input("Enter The Discount Percentage: "))
