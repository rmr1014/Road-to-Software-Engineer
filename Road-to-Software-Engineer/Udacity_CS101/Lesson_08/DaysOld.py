# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def yearHelper(year):
    if((year % 4) != 0):
        return 365
    if((year % 100) != 0):
        return 366
    if((year % 400) != 0):
        return 365
    else:
        return 366

def monthHelper(month):
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return daysOfMonth[month - 1]

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    return "Not Implemented"

# Test routine

# yearHelper, input year = 2020, returns days = 366
passed = "Failed"
days = yearHelper(2020)
if(days == 366):
    passed = "Passed"
print("yearHelper, input year = 2020, returns days = 366: ", passed)

# monthHelper, input month = 7, returns daysInMonth = 31
passed = "Failed"
daysInMonth = monthHelper(7)
if(daysInMonth == 31):
    passed = "Passed"
print("monthHelper, input month = 7, returns daysInMonth = 31: ", passed)

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()