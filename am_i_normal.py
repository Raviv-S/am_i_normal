from statistics import mean

# A. With import
get_above_avarage = lambda numbers: [a_num for a_num in numbers if a_num > mean(numbers)]
print(get_above_avarage(range(10)))

# A. Without import
get_above_avarage = lambda numbers: [a_num for a_num in numbers if a_num > sum(numbers) / len(numbers)]
print(get_above_avarage(range(10)))

# B.
remove_patrick = lambda sentence: ''.join([letter for letter in sentence if letter not in 'patrickPATRICK'])
print(remove_patrick('patrickRavivSchafferStar'))



