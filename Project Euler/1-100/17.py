def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "one thousand"

    result = ""

    if n >= 100:
        hundreds = n // 100
        result += ones[hundreds] + " hundred"
        n = n % 100
        if n > 0:
            result += " and "

    if n >= 20:
        tens_place = n // 10
        ones_place = n % 10
        result += tens[tens_place]
        if ones_place > 0:
            result += "-" + ones[ones_place]
    elif n > 0:
        result += ones[n]

    return result


# Count total number of letters used
total_letters = 0

for i in range(1, 1001):
    words = number_to_words(i)
    total_letters += len(words.replace(" ", "").replace("-", ""))  # Remove spaces and hyphens

print(total_letters)
