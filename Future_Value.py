# Creates decimal values for user-defined preent value, monthly interest, time
# User gives whole rate value, which is divided by 100 for function
def getValues():
    presentValue = float(input("\nPresent value: $"))
    monthlyRate = float(input("Monthly interest rate: "))/100
    numberMonths = int(input("Number of months in account: "))
    
    return presentValue, monthlyRate, numberMonths

# User-defined variables are plugged into future-value function
# 'futureValue' is value generated at end of function
def futureValue(presentValue, monthlyRate, numberMonths):
    futureValue = presentValue * (1 + monthlyRate) ** numberMonths
    
    return futureValue

# Three variables are given values from arguments in previous functions
# These values are printed for the final message with future value stated
def main():
    presentValue, monthlyRate, numberMonths = getValues()
    
    print ("\n\nAccount with present value","$" + format(presentValue, \
           ".2f"), "and a", format(monthlyRate, ".1%"), \
           "monthly rate \nwhen left for", numberMonths, \
           "months will yield a future value of...", "$" + \
           format(futureValue(presentValue, monthlyRate, \
                  numberMonths), ".2f"), "\n")

main()