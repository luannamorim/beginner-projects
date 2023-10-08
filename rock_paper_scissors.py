import random


def play():
    user = input(
        "What's yout choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 's', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost'


def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True


print(play())
