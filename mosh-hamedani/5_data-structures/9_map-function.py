items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]
prices = []
for item in items:
    prices.append(item[1]) #basic way to printing list of the prices of the items

print(prices)

#----
print("\n----Separator\n")

prices = list(map(lambda item: item[1], items))
print(prices)
