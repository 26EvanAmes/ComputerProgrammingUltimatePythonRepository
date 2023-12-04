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
    if divisor == 0:
        return None
    else:
        return average / divisor
inputlist = [0, 5, 10, 15, 20, 25, 30, 35, 40]
result = average_act_score(inputlist)
print("Average ACT Scores => ", result)

def all_true(booleans):
    falses = 0
    for boolean in booleans:
        if boolean == False:
            falses = falses+1
    if falses > 0:
        return False
    else:
        return True
inputlist = [True, True, True, True]
result = all_true(inputlist)
print("All True? => ", result)

def any_true(booleans):
    trues = 0
    for boolean in booleans:
        if boolean == True:
            trues = trues + 1
    if trues > 0:
        return True
    else:
        return False
inputlist = [False, False, False, True]
result = any_true(inputlist)
print("Any True? => ", result)

def mostly_true(booleans):
    trues = 0
    falses = 0
    for boolean in booleans:
        if boolean == True:
            trues = trues + 1
        else:
            falses = falses + 1
    if trues > falses:
        return True
    else:
        return False
inputlist = [False, False, False, True, True]
result = mostly_true(inputlist)
print("Mostly True? => ", result)

def has_vowel(chars):
    vowels = 0
    for char in chars:
        if char in ["a", "e", "i", "o", "u"]:
            vowels = vowels + 1
    if vowels > 0:
        return True
    else: 
        return False
inputlist = ["x", "b", "c", "d", "x", "f"]
result = has_vowel(inputlist)
print("Has a Vowel? => ", result)

def all_the_same(nums):
    same = True
    first = nums[0]
    for num in nums:
        if num == first:
            pass
        else:
            same = False
    return same
inputlist = ["2", "1", "1", "1", "1"]
result = all_the_same(inputlist)
print("All the Same? => ", result)

def increasing(nums):
    previous = -99999
    increasing = True
    for num in nums:
        if num > previous:
            previous = num
        else:
            increasing = False
    return increasing
inputlist = [2, 3, 5, 9, 2]
result = increasing(inputlist)
print("Increasing? => ", result)

def is_incrementing(nums):
    incrementing = True
    previous = nums[0] - 1
    for num in nums:
        if num == previous + 1:
            previous = num
        else:
            incrementing = False
    return incrementing
inputlist = [2, 3, 4, 5, 6]
result = is_incrementing(inputlist)
print("Incrementing? => ", result)

def has_adjacent_repeat(nums):
    previous = 0.32771
    adjacent_repeat = False
    for num in nums:
        if num == previous:
            adjacent_repeat = True
        else:
            previous = num
    return adjacent_repeat
inputlist = ["4", "3", "4", "3", "4"]
result = has_adjacent_repeat(inputlist)
print("Has Adjacent Repeat? => ", result)

def sum_with_skips(nums):
    ignoring = False
    sum = 0
    for num in nums:
        if ignoring == False and num == -1:
            ignoring = True
        elif ignoring == True and num == -1:
            ignoring = False
        elif ignoring == True:
            pass
        else:
            sum = sum + num
    return sum
inputlist = [4, -1, 4, -1, 4]
result = sum_with_skips(inputlist)
print("Sum With Skips => ", result)