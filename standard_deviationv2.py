import statistics

input_string = input('Enter elements of a list separated by space:')
print("\n")

try:
    # this line of code makes the input numbers split in a list
    user_list = input_string.split()
    # this line of code converts string in the user_list into interger so we can do math operations to it 
    new_list = [int(n) for n in user_list]

    print(statistics.pstdev(new_list))

except:
    print("Please don't include any characters or symbols")
