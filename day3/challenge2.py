file = []

with open('input.txt', 'r') as f:
    for line in f:
        file.append(line.replace('\n', ''))

def getOxygenRating(diagnostic_report):

    for i in range(len(diagnostic_report[0])):
        if len(diagnostic_report) != 1:
            temp_diagnostic_report = []
            zero_count = 0
            one_count = 0

            for line in diagnostic_report:
                if line[i] == '1':
                    one_count += 1
                elif line[i] == '0':
                    zero_count += 1
            if one_count > zero_count:
                for line in diagnostic_report:
                    if line[i] == '1':
                        temp_diagnostic_report.append(line)
            elif zero_count > one_count:
                for line in diagnostic_report:
                    if line[i] == '0':
                        temp_diagnostic_report.append(line)
            elif one_count == zero_count:
                for line in diagnostic_report:
                    if line[i] == '1':
                        temp_diagnostic_report.append(line)

            diagnostic_report = temp_diagnostic_report
    
    return diagnostic_report


def getCO2Rating(diagnostic_report):

    for i in range(len(diagnostic_report[0])):
        if len(diagnostic_report) != 1:
            temp_diagnostic_report = []
            zero_count = 0
            one_count = 0

            for line in diagnostic_report:
                if line[i] == '1':
                    one_count += 1
                elif line[i] == '0':
                    zero_count += 1
            if one_count < zero_count:
                for line in diagnostic_report:
                    if line[i] == '1':
                        temp_diagnostic_report.append(line)
            elif zero_count < one_count:
                for line in diagnostic_report:
                    if line[i] == '0':
                        temp_diagnostic_report.append(line)
            elif one_count == zero_count:
                for line in diagnostic_report:
                    if line[i] == '0':
                        temp_diagnostic_report.append(line)

            diagnostic_report = temp_diagnostic_report
    
    return diagnostic_report

print(int(getCO2Rating(file)[0], 2) * int(getOxygenRating(file)[0], 2))