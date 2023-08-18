items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]
filtered = list((filter(lambda item: item[1] >= 10, items)))
print(filtered)