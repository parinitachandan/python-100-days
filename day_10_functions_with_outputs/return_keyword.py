# can have multiple return keywords in a function and also an empty return function
def format_name(first_name, last_name):
    """
An Example of a docstring
    """
    name = first_name + last_name
    return name.title()
    # print("Hello") - the return function tells it to end the function, thus doesn't print this line


print(format_name("parinita", " p c"))


def names(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide a valid input"

    name = (first_name + last_name).title()
    return f"Result: {name}"


print(names(first_name=input("Enter your first name: "), last_name=input("Enter your last name: ")))


def is_leap(leap_year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(years, months):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month entered."
    if month == 2 and is_leap(years):
        return 29
    return month_days[month - 1]


year_input = int(input("Enter a year: "))
month_input = int(input("Enter a month: "))
days = days_in_month(year_input, month_input)
print(f"The year {year_input}, in the month {month_input} has so many {days} days")
