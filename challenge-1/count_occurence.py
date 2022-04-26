def compress(input_string):
    compressed_string, count, tracked_letter = ['' for _ in range(3)]
    string_length = len(input_string)
    for index, letter in enumerate(input_string):
        if tracked_letter != letter:
            # if letter is changed from tracked letter, it will put it
            # in compressed string alongwith count
            # change the pointer to next letter and re initilize count
            compressed_string += f'{tracked_letter}{count}'
            tracked_letter = letter
            count = 1
        else:
            count += 1

        if string_length == index + 1:
            # adds the letter and count at the end of string
            compressed_string += f'{tracked_letter}{count}'

    return compressed_string.replace('1', '')

assert compress('bbcceeee') == 'b2c2e4'
assert compress('a') == 'a'
assert compress('aaabbbcccaaa') == 'a3b3c3a3'


