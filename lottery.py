import random


def generate_quick_pick():
    quick_pick = random.sample(range(1, 56), 6)
    quick_pick.sort()
    return quick_pick


def display_quick_pick(quick_pick):
    print("Your lottery quick pick for tonight is:")
    for i in range(6):
        print(f"{i + 1}. {quick_pick[i]}")


if __name__ == "__main__":
    quick_pick = generate_quick_pick()
    display_quick_pick(quick_pick)
