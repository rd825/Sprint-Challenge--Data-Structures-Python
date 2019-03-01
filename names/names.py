import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# initial solution
duplicates = set(names_1).intersection(names_2)

# stretch solution
# has better space complexity but is far slower than above
# duplicates = [item for item in names_1 if item in names_2]

end_time = time.time()
# note to self -- expect 64 dupes
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# PROVIDED CODE
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
