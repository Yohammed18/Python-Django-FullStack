# Regular expressions (often abbreviated as regex or regexp) are powerful tools for pattern matching and text manipulation in programming languages. In Python, the re module provides support for regular expressions.

import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not not the other!'

# for pattern in patterns:
#     print("I'm searching for: {}".format(pattern))

#     if re.search(pattern, text):
#         print("MATCH")
#     else:
#         print("NO MATCH")

match = re.search(patterns[0], text)
print(match.string)

# print("Attributes and Methods: {}".format(dir(match)))


split_term = '@'

email = 'user@gmail.com'

email_match = re.split(split_term, email)
print(email_match)


# finding all instances of a pattern

num_match = re.findall('match','Test phrase match in middle of match explains why the match is important. Match yourself and don\'t reck yourself match.')
print("Number of found match: {}. {}".format(len(num_match), num_match))