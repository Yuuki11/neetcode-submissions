def remove_fourth_character(word: str) -> str:
    first_message = word[:3]
    second_message = word[4:]
    return first_message + second_message


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
