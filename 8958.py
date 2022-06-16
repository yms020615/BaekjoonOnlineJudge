for i in range(int(input())):
    case = input()
    score = 0
    combo = 0
    for j in case:
        if j == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)
