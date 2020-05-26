# Module 4
#   Programming Assignment 5
#       Prob-2.py

# <Tristan Sahagun>

# IPO
'''Input(s): amount paid and the cost
Process: calculates the change due and breaks it down to each denomination of cash returned
Output: prints to terminal'''


# Calculate change and find each denomination returned
def main():
    money = float(input("How much paid: "))
    cost = float(input("How much cost:"))
    change = money - cost
    print("Cost: $", cost, "\tTendered: $", money, "\tChange: $", change)
    changedue = int(round(change * 100))

    fifty = changedue // 5000
    changedue = changedue - (fifty * 5000)
    if fifty >= 1:
        print ("Fifty: ", fifty)

    twenty = changedue // 2000
    changedue = changedue - (twenty * 2000)
    if twenty >= 1:
        print ("twenty: ", twenty)


    tens = changedue // 1000
    changedue = changedue - (tens * 1000)
    if tens >= 1:
        print ("ten: ", tens)


    five = changedue // 500
    changedue = changedue - (five * 500)
    if five >= 1:
        print ("five: ", five)


    ones = changedue // 100
    changedue = changedue - (ones * 100)
    if ones >= 1:
        print ("one: ", ones)


    quarter = changedue // 25
    changedue = changedue - (quarter * 25)
    if quarter >= 1:
        print ("quarter: ", quarter)


    dimes = changedue // 10
    changedue = changedue - (dimes * 10)
    if dimes >= 1:
        print ("dime: ", dimes)


    nickles = changedue // 5
    changedue = changedue - (nickles * 5)
    if nickles >= 1:
        print ("nickle: ", nickles)
    
    if changedue >= 1:
        print ("penny: ", changedue)





main()
