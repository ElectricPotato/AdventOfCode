class Monkey:
    def __init__(self, startItems, operation, testOp, ifTrueDest, ifFalseDest) -> None:
        self.items = startItems
        self.operation = operation
        self.testOp = testOp
        self.ifTrueDest = ifTrueDest
        self.ifFalseDest = ifFalseDest
        self.inspectN = 0

monkeysExample = [
    Monkey(
        [79, 98],
        lambda old: old * 19,
        lambda x: x % 23 == 0,
        2,
        3
    ),
    Monkey(
        [54, 65, 75, 74],
        lambda old: old + 6,
        lambda x: x % 19 == 0,
        2,
        0
    ),
    Monkey(
        [79, 60, 97],
        lambda old: old * old,
        lambda x: x % 13 == 0,
        1,
        3
    ),
    Monkey(
        [74],
        lambda old: old + 3,
        lambda x: x % 17 == 0,
        0,
        1
    )
]

monkeysProblem = [
  Monkey(
      [98, 89, 52],
      lambda old: old * 2,
      lambda x: x % 5 == 0,
      6,
      1
  ),
  Monkey(
      [57, 95, 80, 92, 57, 78],
      lambda old: old * 13,
      lambda x: x % 2 == 0,
      2,
      6
  ),
  Monkey(
      [82, 74, 97, 75, 51, 92, 83],
      lambda old: old + 5,
      lambda x: x % 19 == 0,
      7,
      5
  ),
  Monkey(
      [97, 88, 51, 68, 76],
      lambda old: old + 6,
      lambda x: x % 7 == 0,
      0,
      4
  ),
  Monkey(
      [63],
      lambda old: old + 1,
      lambda x: x % 17 == 0,
      0,
      1
  ),
  Monkey(
      [94, 91, 51, 63],
      lambda old: old + 4,
      lambda x: x % 13 == 0,
      4,
      3
  ),
  Monkey(
      [61, 54, 94, 71, 74, 68, 98, 83],
      lambda old: old + 2,
      lambda x: x % 3 == 0,
      2,
      7
  ),
  Monkey(
      [90, 56],
      lambda old: old * old,
      lambda x: x % 11 == 0,
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
                destination = [monkey.ifFalseDest, monkey.ifTrueDest][monkey.testOp(monkey.items[0])]
                monkeys[destination].items += [monkey.items.pop(0)]

    inspectStats = sorted(monkey.inspectN for monkey in monkeys)

    return inspectStats[-1] * inspectStats[-2]

def partB(monkeys, modulo):
    for roundN in range(10000):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                monkey.items[0] = monkey.operation(monkey.items[0]) % modulo
                monkey.inspectN += 1
                destination = [monkey.ifFalseDest, monkey.ifTrueDest][monkey.testOp(monkey.items[0])]
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

#print("Example partA", partA(monkeysExample))
print("Example partB", partB(monkeysExample, 23*19*13*17))

#print("partA", partA(monkeysProblem))
print("partB", partB(monkeysProblem, 5*2*19*7*17*13*3*11))
