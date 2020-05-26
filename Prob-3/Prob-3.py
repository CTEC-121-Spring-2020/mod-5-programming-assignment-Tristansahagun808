# Module 4
#   Programming Assignment 5
#       Prob-3.py

# <Tristan Sahagun>

# IPO
'''Input(s): Area of job in sq feet, price of paint in $
Process: calculates the amount and cost of hours and paint needed along with total cost and prints
Output: prints to terminal'''

# Calculate the values given area and price then print
def paint(area, paintprice):
    hours = (float(area) / 112) * 8
    labor = hours * 35
    hours = str(round(hours, 2))
    laborcost = str(round(labor, 2))
    gallons = float(area) / 112
    gallons = int(round(gallons * 1))
    if gallons == 0:
        gallons = gallons + 2
    elif gallons % 2 == 0:
        return
    else:
        gallons = gallons + 1
    paintcost = gallons * float(paintprice)
    totalcost = paintcost + labor + 99
    print("Number of gallons needed: ", gallons)
    print("Number of hours needed: ", hours)
    print("price for paint: $", paintcost)
    print("price for labor: $", laborcost)
    print("total cost: $", totalcost)

# ask for input of area and paint price then run paint function
def main():
    area = input("How many sq feet?: ")
    paintprice = input("how much does paint cost?: $")
    paint(area, paintprice)

main()