import random


LOTTERY_POT = [i for i in range(1, 51)]


def get_random_choices():
    return random.choices(LOTTERY_POT, k=10)


def get_winner_list():
    current_pot = get_random_choices()
    return sorted(current_pot)


if __name__ == '__main__':
    print(get_winner_list())
    """
        for testing get_winner_list, as random.choices return random values,
        we need to mock the get_random_choices function
    """
