'''def is_pangram(input_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {letter : False for letter in alphabet}


    input_string - input_string.lower()
    for char in input_string:
        if char in alphabet_dict:
            alphabet_dict[char] = True

    return all (alphabet_dict.values())

input_string = input("Enter a string -")
print(f"Is the string a panagram - {is_pangram(input_string)}")'''


def is_pangram(input_string):
    numbers = '0123456789'
    numbers_dict = {number : False for number in numbers}

    for num in input_string:
        if num in numbers_dict:
            numbers_dict[num] = True

    return all (numbers_dict.values())

input_string = input("Enter a number - ")
print(f"Is the number a pangram - {is_pangram(input_string)}")