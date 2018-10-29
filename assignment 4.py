kp = int(input(print("how many cookies are being produced?"))) #this is the question it first asks the user
crates_of_cookies = 0
while kp >= 240:
    kp = kp - 240 #This means that that anytime there is greater than 240 in the original input, it will subtracts 240
    crates_of_cookie = crates_of_cookie + 1

boxes = 0
while kp >= 12:
    kp = kp - 12
    boxes = boxes + 1

cookies = 0
while kp >= 1:
    kp = kp - 1
    cookies = cookies + 1

crc = crates_of_cookies * 80 #these codes are to find out the price of the different prices to make the most sense in output
coc = cookies * 0.5
tc = crc + kp + coc
print(crates_of_cookies)
print("is the amount of crates")
print(boxes)
print("is the amount of boxes")
print(cookies)
print("is the amount of cookies")
print(tc)
print("is the total value of the cookies produced")