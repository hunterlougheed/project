import math

run = "Y"

while run == "Y":

    program = ""
    while program != "QP" and program != "TIP" and program != "TEMP":
        program = input("which program would you like to run? (QP,Tip,Temp): ")
        program = program.upper()

    if program == "QP":
        int1 = int(input("\nEnter number 1: "))
        int2 = int(input("Enter number 2: "))

        int1 = int1 * int1
        int2 = int2 * int2

        hypotenuse = math.sqrt(int1 + int2)
        hypotenuse = str(round(hypotenuse, 2))

        print("The hypotenuse is %s" % hypotenuse)

    elif program == "TIP":
        bill = float(input("\nEnter bill price: "))
        tip = int(input("Enter tip amount (as an integer): "))
        tip = float(tip/100)

        tip_left = bill * tip
        tip_left = str(round(tip_left, 2))
        bill = str(round(bill, 2))

        print("You should leave a tip of %s on a bill of %s" % (tip_left, bill))

    else:
        temp_type = input("\nWhich type of temperature are you entering? (c or f): ")
        temp_type = temp_type.upper()
        temp = float(input("Enter temperature: "))

        if temp_type == "C":
            converted = (temp*(9/5)) + 32
            converted = str(round(converted, 2))
            temp = str(round(temp, 2))

        else:
             converted = (temp-32)/(9/5)
             converted = str(round(converted, 2))
             temp = str(round(temp, 2))

             print("%s degrees fahrenheit is %s degrees celsius" % (temp, converted))

