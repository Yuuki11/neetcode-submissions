from typing import List

def read_integers() -> List[int]:
    list = []
    user_input = input()
    string_list = user_input.split(",")
    for i in string_list:
        list.append(int(i))
    return list 


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
