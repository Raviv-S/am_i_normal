from statistics import mean
from string import ascii_letters

# A.
def get_above_average(numbers):
    return [a_num for a_num in numbers if a_num > mean(numbers)]


# B.
def remove_patrick(sentence):
    return ''.join([letter for letter in sentence if letter not in 'patrickPATRICK'])


# C.
def remove_generic_numbers(inp_nums):
    return [int(str_rmv_num) if str_rmv_num != '' else 0 for str_rmv_num in
                                           [str_num.replace('5', '').replace('7', '') for str_num in
                                            [str(num) for num in inp_nums]]]


# D.
def remove_returning_letter(inp_words):
    return [good_word for good_word in inp_words if good_word not in
                                             [bad_word for bad_word in inp_words for ltr in
                                              [ltr_count[0] for ltr_count in
                                               [(letter, ''.join(inp_words).count(letter)) for letter in ascii_letters]
                                               if ltr_count[1] > 3] if ltr in bad_word]]



def main():
    print(get_above_average(range(10)))
    print(remove_patrick('patrickRavivSchafferStar'))
    print(remove_generic_numbers([75, 745, 3575753]))
    print(remove_returning_letter(['bla', 'bloop', 'kkabb', 'ting', 'tang']))


if __name__ == '__main__':
    main()