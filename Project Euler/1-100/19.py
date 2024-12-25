def count_sundays_on_first():
    # Helper function to check if a year is a leap year
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    # Number of days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Start on 1 Jan 1900, which is a Monday (day_of_week = 1)
    day_of_week = 1  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday

    # Advance to 1 Jan 1901
    for year in range(1900, 1901):
        for month in range(12):
            day_of_week = (day_of_week + days_in_month[month]) % 7
            if month == 1 and is_leap_year(year):
                day_of_week = (day_of_week + 1) % 7

    # Count Sundays that fall on the first of the month from 1901 to 2000
    sunday_count = 0

    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:  # If the first day of the month is Sunday
                sunday_count += 1

            # Advance to the next month
            day_of_week = (day_of_week + days_in_month[month]) % 7
            if month == 1 and is_leap_year(year):
                day_of_week = (day_of_week + 1) % 7

    return sunday_count


# Calculate and print the result
result = count_sundays_on_first()
print("Number of Sundays that fell on the first of the month during the twentieth century:", result)
