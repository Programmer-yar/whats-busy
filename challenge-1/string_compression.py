def compress(input_string):
   compressed_string = ""
   count = 1
   for i in range(1, len(input_string)):
      if input_string[i - 1] == input_string[i]:
         count += 1
      else:
         compressed_string = compressed_string + input_string[i - 1]
         if count > 1:
            compressed_string += str(count)
         count = 1
   compressed_string = compressed_string + input_string[-1]
   if count > 1:
      compressed_string += str(count)
   return compressed_string

assert compress('bbcceeee') == 'b2c2e4'
assert compress('a') == 'a'
assert compress('aaabbbcccaaa') == 'a3b3c3a3'


