def puzzleReader(file_name):
    file = open(file_name, 'r')

    arr = []    

    for line in file:
        line = line[line.find(':')+1:]
        line = line.replace(';', ',')
        line = line.split(',')

        draw = {'Red': 0, 'Green': 0, 'Blue': 0}

        for group in line:
            if 'red' in group:
                num = int(''.join(filter(str.isdigit, group)))
                draw['Red'] = num if num > draw['Red'] else draw['Red']
            if 'green' in group:
                num = int(''.join(filter(str.isdigit, group)))
                draw['Green'] = num if num > draw['Green'] else draw['Green']
            if 'blue' in group:
                num = int(''.join(filter(str.isdigit, group)))
                draw['Blue'] = num if num > draw['Blue'] else draw['Blue']

        arr.append(draw)

    file.close()

    return arr

def findIDsums():
    games = puzzleReader("Day2/puzzles.txt")
    games_sum = 0

    i = 0
    while i < len(games):
        if (games[i]['Red'] <= 12) and (games[i]['Green'] <= 13) and (games[i]['Blue'] <= 14):
            games_sum += i+1
        i += 1

    print(games_sum)

def findPowerSums():
    games = puzzleReader("Day2/puzzles.txt")
    power_sum = 0

    for game in games:
        power_sum += game['Red'] * game['Green'] * game['Blue']

    print(power_sum)

findIDsums()
findPowerSums()
