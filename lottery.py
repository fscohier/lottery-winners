import random

def generate_numbers(count, max):
    numbers = set()
    while len(numbers) < count:
        numbers.add(random.randint(1, max))
    return sorted(numbers)

def format_numbers(numbers):
    return ", ".join(map(str, numbers))

#Parameters
main_count = 5
main_max = 50
extra_count = 2
extra_max = 12

main_grid = generate_numbers(main_count, main_max)
extra_grid = generate_numbers(extra_count, extra_max)

sentence = (f"Winning numbers: {format_numbers(main_grid)}. "
            f"Extra numbers: {format_numbers(extra_grid)}.")

print(sentence)