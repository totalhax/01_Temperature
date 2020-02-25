all_calculations = []

for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent 3 ****")

for item in range(0,3):
    print(all_calculations[len(all_calculations) - item - 1])