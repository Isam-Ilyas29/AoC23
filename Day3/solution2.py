file = open("Day3/engine.txt")
lines = file.read().split()

gear_sum = 0

i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if (not lines[i][j].isdigit()) and lines[i][j] != '.':            
            count = 0
            nums = []

            # Top left
            buffer = ''

            if lines[i-1][j-1].isdigit():
                count += 1
                
                k = j - 1
                while lines[i-1][k].isdigit():
                    k -= 1
                k += 1
                while lines[i-1][k].isdigit():
                    buffer += lines[i-1][k]
                    k += 1

                nums.append(int(buffer))

            # Top middle
            buffer = ''

            if lines[i-1][j-1].isdigit():
                pass # when left character is digit
            elif lines[i-1][j].isdigit(): 
                count += 1

                k = j
                while lines[i-1][k].isdigit():
                    buffer += lines[i-1][k]
                    k += 1
                
                nums.append(int(buffer))

            # Top right
            buffer = ''

            if (j + 1) != len(lines[i-1]):
                if lines[i-1][j].isdigit():
                    pass # when left character is digit
                elif lines[i-1][j+1].isdigit(): 
                    count += 1

                    k = j + 1
                    while k != len(lines[i-1]) and lines[i-1][k].isdigit():
                        buffer += lines[i-1][k]
                        k += 1
                        
                    nums.append(int(buffer))

            # Middle left
            buffer = ''

            if lines[i][j-1].isdigit():
                count += 1

                k = j - 1
                while lines[i][k].isdigit():
                    k -= 1
                k += 1
                while lines[i][k].isdigit():
                    buffer += lines[i][k]
                    k += 1

                nums.append(int(buffer))

            # Middle right
            buffer = ''

            if (j + 1) != len(lines[i]):
                if lines[i][j+1].isdigit():
                    count += 1

                    k = j + 1
                    while k != len(lines[i+1]) and lines[i][k].isdigit():
                        buffer += lines[i][k]
                        k += 1

                    nums.append(int(buffer))

            # Bottom left
            buffer = ''

            if lines[i+1][j-1].isdigit():
                count += 1

                k = j - 1
                while lines[i+1][k].isdigit():
                    k -= 1
                k += 1
                while lines[i+1][k].isdigit():
                    buffer += lines[i+1][k]
                    k += 1

                nums.append(int(buffer))

            # Bottom middle
            buffer = ''

            if lines[i+1][j-1].isdigit():
                pass # when left character is digit
            elif lines[i+1][j].isdigit(): 
                count += 1

                k = j
                while lines[i+1][k].isdigit():
                    buffer += lines[i+1][k]
                    k += 1
                
                nums.append(int(buffer))

            # Bottom right
            buffer = ''

            if (j + 1) != len(lines[i+1]):
                if lines[i+1][j].isdigit():
                    pass # when left character is digit
                elif lines[i+1][j+1].isdigit(): 
                    count += 1
                    
                    k = j + 1
                    while k != len(lines[i+1]) and lines[i+1][k].isdigit():
                        buffer += lines[i+1][k]
                        k += 1
                        
                    nums.append(int(buffer))

            if count == 2:
                total = 1
                for n in nums:
                    total *= n
                gear_sum += total

        j += 1
    i += 1

print(gear_sum)
