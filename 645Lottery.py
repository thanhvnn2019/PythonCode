import random
import collections
import matplotlib.pyplot as plt

# Constants
TOTAL_DRAWS = 6
WINNING_NUMBERS = set(range(1, 46))


# Helper functions
def generate_draw(winning_numbers):
    return random.sample(winning_numbers, TOTAL_DRAWS)


def draw_simulator(draw, trials):
    wins = 0
    for _ in range(trials):
        if set(draw).issubset(generate_draw(WINNING_NUMBERS)):
            wins += 1
    return wins / trials


def main():
    draw = generate_draw(WINNING_NUMBERS)
    draw_win_chance = draw_simulator(draw, 100000)

    print("Predicted winning lottery numbers:")
    print(draw)
    print(f"Estimated win chance: {draw_win_chance:.2%}")

    # Histogram of the number of wins for each draw
    wins_distribution = [0] * 11
    for _ in range(10000):
        wins = sum(1 for _ in range(TOTAL_DRAWS) if random.randint(1, 45) in draw)
        wins_distribution[wins] += 1

    plt.bar(range(11), wins_distribution)
    plt.title("Histogram of wins for each draw")
    plt.xlabel("Number of wins")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    main()
