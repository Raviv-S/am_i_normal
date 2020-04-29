from statistics import mean
from string import ascii_letters

# A.
get_above_avarage = lambda numbers: [a_num for a_num in numbers if a_num > mean(numbers)]
print(get_above_avarage(range(10)))

# B.
remove_patrick = lambda sentence: ''.join([letter for letter in sentence if letter not in 'patrickPATRICK'])
print(remove_patrick('patrickRavivSchafferStar'))

# C.
remove_generic_numbers = lambda inp_nums: [int(str_rmv_num) if str_rmv_num != '' else 0 for str_rmv_num in
                                           [str_num.replace('5', '').replace('7', '') for str_num in
                                            [str(num) for num in inp_nums]]]
print(remove_generic_numbers([75, 745, 3575753]))

# D.
remove_returning_letter = lambda inp_words: [good_word for good_word in inp_words if good_word not in
                                             [bad_word for bad_word in inp_words for ltr in
                                              [ltr_count[0] for ltr_count in
                                               [(letter, ''.join(inp_words).count(letter)) for letter in ascii_letters]
                                               if ltr_count[1] > 3] if ltr in bad_word]]
print(remove_returning_letter(['bla', 'bloop', 'kkabb', 'ting', 'tang']))
