def compress(input_string):
   compressed_string = ""     # 1 time
   count = 1                  # 1 time
   for i in range(1, len(input_string)):  # n time
      if input_string[i - 1] == input_string[i]: # n time
         count += 1
      else: # n time
         compressed_string = compressed_string + input_string[i - 1] # n time
         if count > 1:  # n time
            compressed_string += str(count)  # n time
         count = 1   # n time
   compressed_string = compressed_string + input_string[-1] # 1 time
   if count > 1:  # 1 time
      compressed_string += str(count)  # 1 time
   return compressed_string   # 1 time

assert compress('bbcceeee') == 'b2c2e4'
assert compress('a') == 'a'
assert compress('aaabbbcccaaa') == 'a3b3c3a3'

# Time Complexity
# O(7n + 6) approximates to O(n)
# Linear Time Complexity

"""
'n' being the length of input string
'for' loop in line 4 will run n times
In worst case, each alphabet will be repeated once so 
'if' & 'else' will run n times and statements under else
will also run n 'times'
"""