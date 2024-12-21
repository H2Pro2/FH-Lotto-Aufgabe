# Koncsik Michael

import random
import sys

def main():
#    name = "Koncsik Michael"
#    print(name)
    print(generate_lotto_numbers(6, 45))

def generate_lotto_numbers(count_of_numbers, max_numbers):
    x = 0
    list_of_numbers = []
    while x < count_of_numbers:
        pull = random.randint(1, max_numbers)
        if pull in list_of_numbers:
            continue
        else:
            x += 1
            list_of_numbers.append(pull)
    return sorted(list_of_numbers)

main()