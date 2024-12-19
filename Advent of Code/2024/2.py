def puzzle1():
    reports = []
    with open('input', 'r') as file:
        for line in file:
            # Split the line into numbers and convert them to integers
            levels = [int(num) for num in line.split()]
            reports.append(levels)

    safe_num = 0
    for report in reports:
        is_safe = True

        if report[0] < report[1]:
            # Ascending
            for i in range(0, len(report) - 1):
                diff = report[i + 1] - report[i]
                if diff > 3 or diff < 1:
                    is_safe = False
        else:
            # Descending
            for i in range(0, len(report) - 1):
                diff = report[i] - report[i + 1]
                if diff > 3 or diff < 1:
                    is_safe = False

        if is_safe:
            safe_num += 1

    return safe_num


def is_safe_report(report):
    if report[0] < report[1]:  # Ascending
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if diff > 3 or diff < 1:
                return False
    else:  # Descending
        for i in range(len(report) - 1):
            diff = report[i] - report[i + 1]
            if diff > 3 or diff < 1:
                return False
    return True


def puzzle2():
    reports = []
    with open('input', 'r') as file:
        for line in file:
            # Split the line into numbers and convert them to integers
            levels = [int(num) for num in line.split()]
            reports.append(levels)

    safe_num = 0
    for report in reports:
        if is_safe_report(report):
            safe_num += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe_report(modified_report):
                safe_num += 1
                break

    print(safe_num)
    return safe_num


puzzle1()
puzzle2()
