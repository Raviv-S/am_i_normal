from statistics import mean
from string import ascii_letters


# A.
def get_above_average(numbers):
    return [num for num in numbers if num > mean(numbers)]


# B.
def remove_patrick(sentence):
    return ''.join([letter for letter in sentence if letter.lower() not in 'patrick'])


# C.
def remove_generic_numbers(inp_nums):
    return list(map(int, ['0' + rmv_num.replace('5', '').replace('7', '') for rmv_num in map(str, inp_nums)]))


# D.
def remove_returning_letter(inp_words):
    return list(set(inp_words)
                .difference([word for word in inp_words for letter in word if ''.join(inp_words).count(letter) > 3]))


def main():
    print(get_above_average(range(10)))
    print(remove_patrick('patrickRavivSchafferStar'))
    print(remove_generic_numbers([75, 745, 6307, 73575753]))
    print(remove_returning_letter(['test', 'toast', 'not printed', 'yes!', 'xyz']))


if __name__ == '__main__':
    main()