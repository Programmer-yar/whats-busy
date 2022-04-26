def compress(input_string):
    compressed_string = str()
    count = ''
    counted_letter = ''
    string_length = len(input_string)
    for index, letter in enumerate(input_string):
        if counted_letter != letter:
            compressed_string += f'{counted_letter}{count}'
            print("compressed_string: ", compressed_string)
            counted_letter = letter
            print("changed letter: ", counted_letter)
            count = 1
        # elif string_length == index + 1:
        #     count += 1
        #     compressed_string += f'{counted_letter}{count}'

        else:
            count += 1
            print(f"count of {counted_letter} is {count}")
    return compressed_string

# assert compress('bbcceeee') == 'b2c2e4'
# assert compress('a') == 'a'
# test = 'aafggiII'
# test1 = 'aaabbbcccaaa'
# assert compress('aaabbbcccaaa') == 'a3b3c3a3'
print(compress('bbcceeeeb'))

