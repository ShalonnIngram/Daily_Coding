#Consult this blood pressures chart: http://bit.ly/2CloACs
#
#Write a function called check_blood_pressure that takes two
#parameters: a systolic blood pressure and a diastolic blood
#pressure, in that order. Your function should return "Low",
#"Ideal", "Pre-high", or "High" -- whichever corresponds to
#the given systolic and diastolic blood pressure.
#
#You should assume that if a combined blood pressure is on the
#line between two categories (e.g. 80 and 60, or 120 and 70),
#the result should be the higher category (e.g. Ideal and
#Pre-high for those two combinations).
#
#HINT: Don't overcomplicate this! Think carefully about in
#what order you should check the different categories. This
#problem could be easy or extremely hard depending on the
#order you change and whether you use returns or elifs wisely.


#Add your code here!
def check_blood_pressure(systolic, diastolic):
    if systolic >= 140 or diastolic >= 90:
        return "High"
    elif systolic <= 89 and diastolic <= 59:
        return "Low"
    elif (systolic >= 90 and diastolic >= 60) and (systolic <= 119 and diastolic <= 79):
        return "Ideal"
    elif (systolic >= 120 and diastolic >= 80) or (systolic <= 139 and diastolic <= 89):
        return "Pre-high"
    else:
        return "High"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Ideal
test_systolic = 91
test_diastolic = 92

print(check_blood_pressure(test_systolic, test_diastolic))
