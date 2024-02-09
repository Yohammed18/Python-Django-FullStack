import re

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print('Searching for patter {}'.format(pat))
        print(re.findall(pat,phrase))
        print('\n')


test_phrase = 'sdsd...ssssdddd..sdddsddd..dsds...dsssssssssssss...sddddddd'

# I want to find an s follow by zero or more d
# test_pattern = ['sd*']
# I want to find an s follow by 1 or more ds
# test_pattern = ['sd+']
# I want to find an s follow by 0 or 1 d
# test_pattern = ['sd?']
# # specific count
test_pattern = ['sd{1,3}']

multi_re_find(test_pattern, test_phrase)