from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    length1 = len(words)
    length2 = len(my_set)
    return length1 != length2

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
