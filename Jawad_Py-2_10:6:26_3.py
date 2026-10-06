# Rumi Jawad
# 10/6/2026
# Asks the user for a number and checks it against the range 10 to 100.
# It prints whether the number is within range, exceeds the maximum, or
# is below the minimum, then says goodbye.
 
# ask the user to type a number and convert the text they enter into an integer
number = int(input("Enter a number: "))
 
# check if the number is between 10 and 100, including both 10 and 100
if 10 <= number <= 100:
    # The number is inside the allowed range, so let the user know
    print("Value within range")
# if the first check failed, see if the number is larger than 100
elif number > 100:
    # The number is above the maximum allowed value, so report that
    print("Exceed max value")
# anything left over must be smaller than 10
else:
    # the number is under the minimum allowed value, so report that
    print("Below Minimum")
 
# print the goodbye message; this runs every time, no matter which branch ran
print("Good bye")
 