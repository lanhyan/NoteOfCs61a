"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    "*** REPLACE THIS LINE ***"
    sum, flag = 0, False
    for i in range(num_rolls):
        num = dice()
        if num == 1:
            flag = True
        sum += num
    return 0 if flag else sum
    # END Question 1

# 判断是否为质数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True;

# 获取下个质数
def next_prime(num):
    while not is_prime(num + 1):
        num += 1
    return num + 1

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    "*** REPLACE THIS LINE ***"
    score = 0
    if num_rolls == 0:
        score = max(opponent_score % 10, opponent_score // 10 % 10) + 1
    else:
        score = roll_dice(num_rolls, dice)
    if is_prime(score):
        score = next_prime(score)
    return score
    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    "*** REPLACE THIS LINE ***"
    if (score + opponent_score) % 7 == 0:
        return four_sided
    return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    "*** REPLACE THIS LINE ***"
    return score0 % 10 == score1 // 10 % 10 and score0 // 10 % 10 == score1 % 10
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    "*** REPLACE THIS LINE ***"
    while score0 < goal and score1 < goal:
        dice = select_dice(score0, score1)
        if who == 0:
            roll_num = strategy0(score0, score1)
            score_tmp =  take_turn(roll_num, score1, dice)
            if score_tmp == 0:
                score1 += roll_num
            score0 += score_tmp
        else:
            roll_num = strategy1(score1, score0)
            score_tmp =  take_turn(roll_num, score0, dice)
            if score_tmp == 0:
                score0 += roll_num
            score1 += score_tmp
        who = other(who)
        if is_swap(score0, score1):
            score0, score1 = score1, score0
    # END Question 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    "*** REPLACE THIS LINE ***"
    def aver_return(*args):
        sum = 0;
        for i in range(num_samples):
            sum += fn(*args)
        return sum / num_samples
    return aver_return
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    "*** REPLACE THIS LINE ***"
    result, index = 0, 1
    for i in range(10):
        sum = make_averaged(roll_dice, num_samples)(i + 1, dice)
        if sum > result:
            result, index = sum, i + 1
    return index
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    "*** REPLACE THIS LINE ***"
    result = take_turn(0, opponent_score)
    return 0 if result >= margin else num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    "*** REPLACE THIS LINE ***"
    result = score + take_turn(0, opponent_score)
    if (is_swap(result, opponent_score) and opponent_score > result):
        return 0
    return num_rolls
    # return 5  # Replace this statement
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN Question 10
    "*** REPLACE THIS LINE ***"

    roll_num, margin = 4, 6
    if (score + opponent_score) % 7 == 0:
        roll_num, margin = 4, 3
        # if 100 - score < 2:
        #     margin += 1
    # if 100 - score < margin:
    #     margin = 100 - score
    if 100 - score < 2:
        margin += 1
        roll_num -= 1
    if score < 92 and score > 84:
        roll_num += 1
    if score < 85 and score > 70:
        roll_num -= 1
    if score < 69 and score > 66:
        roll_num -= 1
    if score < 60 and score > 55:
        roll_num += 1
    if score < 50 and score > 40:
        margin += 1
        roll_num -= 1
    if score < 30 and score > 20:
        margin += 1

    arg1 = swap_strategy(score, opponent_score, roll_num)
    arg2 = bacon_strategy(score, opponent_score, margin, roll_num)
    return min(arg1, arg2)
    #return bacon_strategy(score, opponent_score, 6, 4)
    # return 5  # Replace this statement
    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
