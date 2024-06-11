#test_lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
lines_1 = open("values_1.txt").readlines()

def chal_1(lines):
    output = 0
    for word in lines:
        first_int = None
        last_int = None
        for char in word:
            if char.isdigit():
                if not first_int:
                    first_int = char
                last_int = char
        output += int(first_int + last_int)
    return output

output = chal_1(lines_1)
print(output)

lines_2 = open("values_2.txt").readlines()
def chal_2(lines):
    digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    output = 0
    for word in lines:
        digits = []
        for index, char in enumerate(word):
            if char.isdigit():
                digits.append(char)
            for i, dgt in enumerate(digit_words):
                if word[index:].startswith(dgt):
                    digits.append(i+1)
        print(digits)
        output += int(str(digits[0]) + str(digits[-1]))
    return output
score = chal_2(lines_2)
print(score)



