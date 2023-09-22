"""
Pseudo Code:
Get amount of items
for i in range(0, amount of items, 1)
    Ask for price
    Add price to running total
end
if running total > 100
    final price = running total*1.10
else
    final price = running total
"""

item_amount = int(input("Number of Items: "))
running_total = 0
while item_amount < 0:
    print("Invalid number of items!")
    item_amount = int(input("Number of Items: "))
else:
    for i in range(0, item_amount, 1):
        item_price = float(input("Price of item: "))
        running_total = item_price + running_total


if running_total > 100:
    final_price = running_total * 0.9
else:
    final_price = running_total
print(f"Total Price for {item_amount} items is ${final_price:.2f}.")
