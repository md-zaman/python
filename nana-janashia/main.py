from helper import validate_and_execute, user_input_msg

user_input = ""
while user_input != "exit":
    user_input = input(user_input_msg)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()