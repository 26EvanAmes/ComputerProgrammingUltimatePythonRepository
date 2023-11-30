def count_failing_grades(scores):
    failing = 0
    for score in scores:
        if score < 60:
            failing = failing + 1
    return failing
inputlist = [20, 40, 60, 80, 100]
result = count_failing_grades(inputlist)
print("Failing grades => ", result)

def count_act_scores(scores):
    valid = 0
    for score in scores:
        if score >= 1 and score <= 36:
            valid = valid + 1
    return valid
inputlist = [0, 5, 10, 15, 20, 25, 30, 35, 40]
result = count_act_scores(inputlist)
print("Valid act scores => ", result)

def number_sum(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum
inputlist = [1, 2, 3, 4, 5]
result = number_sum(inputlist)
print("Number Sum => ", result)

def average_act_score(scores):
    average = 0
    divisor = 0
    for score in scores:
        if score >= 1 and score <= 36:
            average = average + score
            divisor = divisor + 1
    return average / divisor
inputlist = [0, 5, 10, 15, 20, 25, 30, 35, 40]
result = average_act_score(inputlist)
print("Average ACT Scores => ", result)