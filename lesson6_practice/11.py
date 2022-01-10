# 11. Write a Python program to convert seconds to day, hour, minutes and seconds. Seconds get from input


time = int(input("Input time in seconds: "))
day = time // (24 * 3600)
time %= (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
seconds = time % 60 
print(day, hour, minutes, seconds)

