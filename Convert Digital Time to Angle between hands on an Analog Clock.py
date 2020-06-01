# Write a programme that converts the time in 12hr format to the corresponding angle between the hour and minute hands.
# The programme should return the smaller of the two angles.

# 6 degrees between each minute and 30 degrees between each hour.


def time_to_angle():

    time = input("Enter the time in 12 hour format.\nExample: 10:30 or 7:48 or 5:45\nTime: ")
    time_split = time.split(":")

    hour_angle = int(time_split[0])*30

    minute_angle = int(time_split[1]) * 6

    if hour_angle > minute_angle:
        angle = hour_angle - minute_angle
    else:
        angle = minute_angle - hour_angle

    if angle > 180:
        angle = 360 - angle

    print(angle)


time_to_angle()
