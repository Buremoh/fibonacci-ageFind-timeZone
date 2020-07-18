from datetime import datetime, timedelta, date


# Game setup
print('Welcome, please enter your date of birth in the format: 28/02/2000')

now = datetime.now()
birthday_in = str(input())

# Use try to check if the date was entered in the correct format
try:
    # Parse the given date to a datetime object so python can understand it
    birthday = datetime.strptime(birthday_in, '%d/%m/%Y')

# Calculate your age and print it on the console
    countdown = now - birthday
    age = int(countdown.days/365.25)
    print("You're currently", age, "years old.")

# Find out on which weekday you were born'
    print('You were born on a', birthday.strftime('%A')+'!'+'\n')

# Set a new datetime object by replacing your birthday-year with the current one
    birthday_this_year = birthday.replace(year=now.year)

# Find out how much time is left until your next birthday
    time_until_birthday = now - birthday_this_year

    if birthday.month == now.month and birthday.day == now.day:

        # If your birthday is today, print a special message

        print("It's your birthday today!"+'\n')
        print('Happy Birthday to you!')
        print('Congratulations! You are now', age, 'years old'+'\n')

    elif (birthday.month - now.month) * (-1) <= 3 and now < birthday_this_year:

        # If your birthday has not yet passed and lies within the next three months, print how many days are left until your birthday along with a message"

        print('Hey, your birthday is coming soon!'+'\n')

    else:

        # If you're birthday is further away than three months, print the days until your birthday and a message

        print('Your birthday is coming in', 365 -
              time_until_birthday.days, 'days.'+'\n')


except ValueError:

    # If the input was in a wrong format, print the following error message

    print('Please check the format of date your entered. It should be in the following format: 28/02/2000')
