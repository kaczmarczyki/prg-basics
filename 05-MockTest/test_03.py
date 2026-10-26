###
# A program that reads time (hh:mm:ss) and prints
# the number of seconds since midnight.
#
time = input('Enter time (hh:mm:ss): ')
time_split = time.split(":")
hours = int(time_split[0])
minutes = int(time_split[1])
seconds = int(time_split[2])
#sekund w minucie = 60s
#sekund w godzinie = 36000s
total = hours * 3600 + minutes * 60 + seconds
print(f'Seconds since midnight: {total}')
