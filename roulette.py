def funk(total, min_bet):

    bet = min_bet
    counter = 0
    summary = 1

    while total > summary:

            summary += bet
            bet *= 2
            counter += 1

    chance_to_loose = 0.5135

    for x in range(counter - 1):
        chance_to_loose *= 0.5135

    chance = (1 - chance_to_loose) * 100

    print(f'You will win with {chance}% chance, taking {counter} steps')

# print(funk(700, 100))
funk(int(input('Enter your amount of money: ')), int(input('Enter desirable win: ')))
