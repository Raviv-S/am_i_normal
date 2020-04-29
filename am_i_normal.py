from statistics import mean

# A. With import
get_above_avarage = lambda lst: list(filter(lambda num: num > mean(lst), lst))
print(get_above_avarage(range(10)))

# A. Without import
get_above_avarage = lambda lst: list(filter(lambda num: num > sum(lst) / len(lst), lst))
print(get_above_avarage(range(10)))
