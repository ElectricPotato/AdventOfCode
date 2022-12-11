class Monkey:
    def __init__(self, startItems, operation, divisionTest, ifTrueDest, ifFalseDest) -> None:
        self.items = startItems
        self.operation = operation
        self.divisionTest = divisionTest
        self.ifTrueDest = ifTrueDest
        self.ifFalseDest = ifFalseDest
        self.inspectN = 0

monkeysExample = [
    Monkey(
        [79, 98],
        lambda old: old * 19,
        23,
        2,
        3
    ),
    Monkey(
        [54, 65, 75, 74],
        lambda old: old + 6,
        19,
        2,
        0
    ),
    Monkey(
        [79, 60, 97],
        lambda old: old * old,
        13,
        1,
        3
    ),
    Monkey(
        [74],
        lambda old: old + 3,
        17,
        0,
        1
    )
]

monkeysProblem = [
  Monkey(
      [98, 89, 52],
      lambda old: old * 2,
      5,
      6,
      1
  ),
  Monkey(
      [57, 95, 80, 92, 57, 78],
      lambda old: old * 13,
      2,
      2,
      6
  ),
  Monkey(
      [82, 74, 97, 75, 51, 92, 83],
      lambda old: old + 5,
      19,
      7,
      5
  ),
  Monkey(
      [97, 88, 51, 68, 76],
      lambda old: old + 6,
      7,
      0,
      4
  ),
  Monkey(
      [63],
      lambda old: old + 1,
      17,
      0,
      1
  ),
  Monkey(
      [94, 91, 51, 63],
      lambda old: old + 4,
      13,
      4,
      3
  ),
  Monkey(
      [61, 54, 94, 71, 74, 68, 98, 83],
      lambda old: old + 2,
      3,
      2,
      7
  ),
  Monkey(
      [90, 56],
      lambda old: old * old,
      11,
      3,
      5
  )
]

from typing import List

def partA(monkeys: List[Monkey]):
    for roundN in range(20):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                monkey.items[0] = monkey.operation(monkey.items[0])
                monkey.inspectN += 1
                monkey.items[0] = monkey.items[0] // 3
                test = monkey.items[0] % monkey.divisionTest == 0
                destination = [monkey.ifFalseDest, monkey.ifTrueDest][test]
                monkeys[destination].items += [monkey.items.pop(0)]

    inspectStats = sorted(monkey.inspectN for monkey in monkeys)

    return inspectStats[-1] * inspectStats[-2]


from functools import reduce
def product(xs):
    return reduce(lambda x, y: x * y, xs, 1)

def partB(monkeys):
    modulo = product(monkey.divisionTest for monkey in monkeys)

    for roundN in range(10000):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                monkey.items[0] = monkey.operation(monkey.items[0]) % modulo
                monkey.inspectN += 1
                test = monkey.items[0] % monkey.divisionTest == 0
                destination = [monkey.ifFalseDest, monkey.ifTrueDest][test]
                monkeys[destination].items += [monkey.items.pop(0)]

    inspectStats = sorted(monkey.inspectN for monkey in monkeys)

    return inspectStats[-1] * inspectStats[-2]



import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

from copy import deepcopy

print("Example partA", partA(deepcopy(monkeysExample)))
print("Example partB", partB(deepcopy(monkeysExample)))

print("partA", partA(deepcopy(monkeysProblem)))
print("partB", partB(deepcopy(monkeysProblem)))
