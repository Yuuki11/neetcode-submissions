def add_two_numbers() -> int:
    user_input = input()
    sum = 0
    string_list = user_input.split(",")
    for i in string_list:
        sum += int(i)
    return sum
 



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
