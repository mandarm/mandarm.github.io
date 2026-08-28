import sys

if len(sys.argv) != 3:
    sys.exit('Usage: ' + sys.argv[0] + ' <number of taps> <number of drains>')

num_taps = int(sys.argv[1])
num_drains = int(sys.argv[2])

total_water_added_per_min = 0
total_water_removed_per_min = 0

for i in range(num_taps):
    message = 'How long does it take for Tap ' + str(i) + \
        ' to fill an empty reservoir by itself? '
    filling_time = int(input(message))
    total_water_added_per_min += 1/filling_time

for i in range(num_drains):
    message = 'How long does it take for Drain ' + str(i) + \
        ' to empty a full reservoir by itself? '
    draining_time = int(input(message))
    total_water_removed_per_min += 1/draining_time

if total_water_added_per_min == total_water_removed_per_min:
    print("A partially full reservoir never becomes completely full or empty when all taps and drains are kept open.")
elif total_water_added_per_min > total_water_removed_per_min:
    print("An initially empty reservoir becomes completely full in",
          1 / (total_water_added_per_min - total_water_removed_per_min),
          "minutes.")
else:
    print("An initially full reservoir becomes completely empty in",
          1 / (total_water_removed_per_min - total_water_added_per_min),
          "minutes.")
