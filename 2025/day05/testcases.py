import copy
from random import randint

from sol import *

#a simple version of the function to use a reference
def partB_naive(fresh_ranges):
    ingredients = set()
    for start, end in fresh_ranges:
        for i in range(start, end + 1):
            ingredients.add(i)
    return len(ingredients)


#compare the partB function with the reference one, under random testcases
def compare():
    for _ in range(10000):
        #generate testcase
        fresh_ranges = []
        for _ in range(100):
            start = randint(1, 100)
            end = start + randint(0, 100)
            fresh_ranges.append([start, end])

        naive = partB_naive(fresh_ranges)
        optimised = partB(fresh_ranges)

        assert naive == optimised, f"testcase: {fresh_ranges}\nnaive: {naive}, optimised: {optimised}"
        print("ok")


#remove elements from the testcase to get it down to the source of the discrepency
def minimise_testcase():
    #this was a randomly generated tescase that caused the discrepency
    testcase = [[41, 41], [17, 24], [17, 64], [39, 71], [6, 58], [22, 95], [57, 104], [86, 178], [75, 75], [64, 146], [85, 137], [48, 50], [56, 140], [46, 85], [44, 45], [95, 195], [78, 122], [93, 109], [50, 119], [22, 43], [32, 87], [79, 87], [9, 80], [3, 76], [93, 156], [34, 101], [80, 175], [32, 100], [17, 60], [39, 67], [37, 128], [14, 99], [3, 79], [98, 169], [9, 70], [68, 69], [22, 107], [58, 96], [46, 74], [14, 27], [1, 54], [5, 65], [67, 102], [57, 97], [87, 181], [50, 70], [81, 87], [85, 143], [24, 71], [15, 100], [79, 176], [53, 137], [15, 15], [61, 76], [43, 60], [45, 75], [74, 117], [52, 137], [83, 182], [60, 71], [44, 106], [94, 145], [88, 137], [39, 113], [60, 157], [33, 83], [13, 35], [9, 22], [78, 148], [5, 48], [32, 121], [76, 78], [34, 77], [58, 135], [58, 105], [67, 70], [40, 40], [28, 88], [3, 9], [83, 117], [7, 94], [6, 59], [56, 129], [71, 140], [70, 128], [74, 172], [18, 59], [81, 83], [38, 69], [1, 96], [36, 116], [9, 18], [77, 110], [88, 125], [84, 169], [87, 144], [82, 108], [53, 143], [87, 140], [4, 49]]
    #verify there is in fact a discrepency
    assert partB_naive(testcase) != partB(testcase), "there is no discrepency, cant minimise"

    while True:
        found = False
        for i in range(len(testcase)):
            new_testcase = copy.deepcopy(testcase)
            new_testcase.pop(i)

            naive = partB_naive(new_testcase)
            optimised = partB(new_testcase)

            if naive != optimised:
                testcase = copy.deepcopy(new_testcase)
                found = True
                break

        if not found:
            break

    
    print("minimused testcase: ", testcase)

#compare()
#minimise_testcase()
assert partB_naive([[82, 108], [53, 143]]) == partB([[82, 108], [53, 143]]), "there is a discrepency"
assert range_overlap_check([82, 108], [53, 143])
print("ok")