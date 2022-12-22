import sys
import calendar
# Method 1
months = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October", "November", "December"]


def month_name():

    try:
        number = int(input("Enter the month number: "))
        for i in range(len(months)):
            if i+1 == number:
                print(months[i])

            if number < 1 or number > 12:
                print("Enter correct number from 1 to 12", file=sys.stderr)
                return month_name()

    except ValueError:
        print("Ooops! You have to input integers", file=sys.stderr)
        month_name()


month_name()

# Method 2
def built_in_lib(digit):
    try:
        x = calendar.month_name[digit]
        if digit > 12 or digit < 1:
            raise IndexError
        print(x)

    except IndexError:
        print("Something went wrong!", file=sys.stderr)
    except ValueError:
        print("Ooops! You have to input integers", file=sys.stderr)


built_in_lib(int(input("Input number for the second method: ")))
