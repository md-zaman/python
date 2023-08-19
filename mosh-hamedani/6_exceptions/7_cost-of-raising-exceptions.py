#raise exeption only when you have to because this affects the performance

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


calculate_xfactor(-1)

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

"""
print("first code=", timeit(code1, number=10000))