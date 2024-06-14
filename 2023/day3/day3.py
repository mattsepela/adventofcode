values = open("values.txt").read().split("\n")
symbols = ['#', '=', '/', '&', '+', '%', '-', '$', '*', '@']
total = 0
for line_num, line in enumerate(values):
    current_num = ""
    for index, char in enumerate(line):
        if char.isdigit():
            if not current_num:
                first_index = index
            current_num += char
        else:
            if current_num:
                try:
                # check if there are symbols next to the part value
                    if line[first_index-1] in symbols or line[first_index + len(current_num)] in symbols:
                        total += int(current_num)
                    # check if there are symbols above the part value
                    elif index > 0 and any(symbol in symbols for symbol in values[line_num-1][first_index-1:first_index + len(current_num) + 1]):
                        total += int(current_num)
                    # check if there are symbols below the part value
                    elif index < len(values)+1 and any(symbol in symbols for symbol in values[line_num+1][first_index-1:first_index + len(current_num) + 1]):
                        total += int(current_num)
                    else:
                        pass
                except IndexError:
                    pass
                print(current_num)
                current_num = ""
print(total)
