speed = int(input("what is the car speed"))

speed_limit= 50 #that is the max speed of the car and if they go over there are fines

if speed>speed_limit:
    if speed <speed_limit+20:
        print("you are above the speed speed limit")
        print("fine is $45") #to tell the user when they go 20km over the speed limit that the fine is $45
if speed>speed_limit+20:
    if speed<speed_limit+30:
        print("you are above the speed speed limit")
        print("fine is $75") #to tell the user when they go 30km over the speed limit that the fine is $75
if speed>=speed_limit+31:
    print("you are above the speed speed limit")
    print("fine is $150") #to tell the user when they go 31+km over the speed limit that the fine is $150
