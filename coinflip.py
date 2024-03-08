def funk(rng, bet):

    min_bet = bet
    summary = 0

    for i in range(rng):

        summary += min_bet
        min_bet *= 2

    chanse_to_loose = 0.5

    for x in range(rng - 1):

        chanse_to_loose *= 0.5

    chanse_to_win = 100 - chanse_to_loose

    print(f'I need {summary} dollars, to win {bet} dollars with {chanse_to_win}% chance')


funk(int(input('Enter amount of steps: ')), int(input('How much you want to win: ')))















