price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

discount_amount = (price * discount_percent) / 100
final_price = price - discount_amount

print("Discount Amount =", discount_amount)
print("Final Price =", final_price)