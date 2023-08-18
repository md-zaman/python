items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]
prices = list(map(lambda item: item[1], items))
prices = ([item[1] for item in items])

filtered = list((filter(lambda item: item[1] >= 10, items)))
print(filtered)
