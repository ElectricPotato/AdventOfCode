'''

'''


requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def partA(inputText):
    return sum(
        [all([field in passport
            for field in requiredFields])
                for passport in inputText.split("\n\n")]
    )

def partB(inputText):
    import re

    s=0
    for passport in inputText.split("\n\n"):
        fields = passport.split()
        fieldDict = {}
        for field in fields:
            key, val = field.split(":")
            fieldDict[key] = val
        if(all([key in fieldDict.keys() for key in requiredFields])):
            if(1920 <= int(fieldDict["byr"]) <= 2002
            and 2010 <= int(fieldDict["iyr"]) <= 2020
            and 2020 <= int(fieldDict["eyr"]) <= 2030
            and ((fieldDict["hgt"][-2:] == "cm" and 150 <= int(fieldDict["hgt"][:-2]) <= 193)
                or (fieldDict["hgt"][-2:] == "in" and 59 <= int(fieldDict["hgt"][:-2]) <= 76))
            and re.fullmatch(r"#[\da-f]{6}",fieldDict["hcl"])
            and fieldDict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and re.fullmatch(r"\d{9}",fieldDict["pid"])
            ): s+=1
        #print(fieldDict)
    return s



inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))