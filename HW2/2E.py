
#Problem E

def average(some_scores):
    'Accepts a list of scores and returns their average'
    print("hello")
    return sum(some_scores) / len(some_scores)

help(average)

num_scores = eval(input('Enter number of scores: '))

score_list = []
for num in range(num_scores):   # num_scores被eval过，此时是个数字
    score = eval(input('Enter score value: '))
    score_list.append(score)

results = average(score_list)

print("Average:", results)

