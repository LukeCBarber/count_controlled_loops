import random

valid_input = False
while valid_input == False:
    throws = int(input('Number of throws: '))
    if throws > 0:
        valid_input = True
        print()
    else:
        print("Please enter a positive number.")
        print()



red = 0
blue = 0
green = 0
miss = 0
dark_gray = 0
light_gray = 0
for throw in range(throws):
    color = False
    x = random.randint(0,800)
    y = random.randint(0,500)
    #red rectangle
    if x >= 350:
        if x <= 450:
            if y >= 300:
                if y <= 450:
                    red += 1
                    color = True
    #blue circle
    blue_dist = (((x - 400)**2 + (y - 150)**2)**0.5)
    if blue_dist <= 100:
        blue += 1
        color = True
    #green rectangle
    if x >= 550:
        if x <= 750:
            if y >= 50:
                if y <= 450:
                    green +=1
                    color = True
    if x >= 600:
        if x <= 700:
            if y >= 100:
                if y <= 200:
                    green -=1
                    color = False
    if x >600:
        if x <= 650:
            if y >= 250:
                if y <= 300:
                    green -=1
                    color = False
    if x >= 650:
        if x <= 700:
            if y >= 350:
                if y <= 400:
                    green -= 1
                    color = False
    #grey circles
    gray_dist1 = (((x - 150)**2 + (y - 200)**2)**0.5)
    gray_dist2 = (((x - 150)**2 + (y - 300)**2)**0.5)
    if gray_dist1 <= 50 and gray_dist2 <= 100:
        light_gray +=1
        color = True
    elif gray_dist1 <= 50:
        dark_gray +=1
        color = True
    elif gray_dist2 <= 100:
        dark_gray +=1
        color = True

    if color == False:
        miss +=1

       
   
redpercent = (red/throws)
bluepercent = (blue/throws)
greenpercent = (green/throws)
darkgraypercent = (dark_gray/throws)
lightgraypercent = (light_gray/throws)
misspercent = (miss/throws)
   
print(format('Red:','25s'),format(str(red),'10s')," ", "{:.2%}".format(redpercent))
print(format('Blue:','25s'), format(str(blue),'10s')," ", "{:.2%}".format(bluepercent))
print(format('Green:', '25s'), format(str(green), '10s')," ", "{:.2%}".format(greenpercent))
print(format('Dark gray:', '25s'), format(str(dark_gray), '10s')," ", "{:.2%}".format(darkgraypercent))
print(format('Light gray:', '25s'), format(str(light_gray),'10s')," ", "{:.2%}".format(lightgraypercent))
print(format('Misses:', '25s'), format(str(miss),'10s')," ", "{:.2%}".format(misspercent))
