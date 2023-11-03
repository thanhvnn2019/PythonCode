import random


def generate_lottery_numbers():
    # Generate 6 random 2-digit numbers between 10 and 99
    numbers = [random.randint(1, 45) for _ in range(6)]

    # Remove duplicates
    numbers = list(set(numbers))

    # Sort the numbers in ascending order
    numbers.sort()

    return numbers


# Generate a list of 10,000 lottery numbers
lottery_numbers = [generate_lottery_numbers() for _ in range(101)]

# Print the generated lottery numbers
for i, numbers in enumerate(lottery_numbers):
    print(f"Lottery Numbers #{i + 1}: {numbers}")
