file = open("Day4/scratchcards.txt", 'r')
points = 0

games = []

for game in file:
    game = game.replace(':', '')
    game = [int(n) for n in game.split() if n.isdigit()]
    game = [game[0], game[1:11], game[11:]]
    games.append(game)

original_games = games[:]

i = 0
while i < len(games):
    count = 0
    game_code = games[i][0]

    for num in games[i][2]:
        if num in games[i][1]:
            count += 1

    for j in range(1, count+1):
        for game in original_games:
            if game[0] == game_code + j:
                games.insert(i+1, game)
                break

    i += 1
    
    
print(len(games))
