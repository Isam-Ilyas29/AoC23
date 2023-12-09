file = open("Day4/scratchcards.txt", 'r')
points = 0

for game in file:
    count = -1

    game = game[game.find(':')+1:]
    game = [d.lstrip().rstrip().split() for d in game.split('|')]

    for num in game[1]:
        if num in game[0]:
            count += 1

    points += 2**count if count != -1 else 0

print(points)
