ENTRY_AGE_LIMIT = 10
ENTRY_HEIGHT_LIMIT = 120


def have_fun_at_the_park():
    age = is_eligible_for_entry()
    if age:
        calculate_bill(age)


def is_eligible_for_entry():
    age = int(input("Please enter your age\n"))

    if verify_age(age):
        height = int(input("Please enter your height\n"))

        if verify_height(height):
            return age

    return False


def is_negative(number):
    return number < 0


def verify_age(age):
    if is_negative(age):
        print('\nAge cannot be a negative number')
        return False

    if age < ENTRY_AGE_LIMIT:
        print('\nEntry age limit is ' + str(ENTRY_AGE_LIMIT) + ". You are not allowed to enter")
        return False

    return True


def verify_height(height):
    if is_negative(height):
        print('\nHeight cannot be a negative number')
        return False

    if height < ENTRY_HEIGHT_LIMIT:
        print('\nEntry age limit is ' + str(ENTRY_AGE_LIMIT) + ". You are not allowed to enter")
        return False

    return True


def calculate_bill(age):
    if age >= 10 and age <= 12:
        print("You need to pay $5")
    elif int(age) >= 13 and int(age) <= 18:
        print("You need to pay $15")
    else:
        print("You need to pay $25")


have_fun_at_the_park()
