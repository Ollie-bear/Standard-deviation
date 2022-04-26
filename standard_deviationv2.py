import statistics

input_string = input('Enter elements of a list separated by space:')
print("\n")

try:
    
    user_list = input_string.split()

    new_list = [int(n) for n in user_list]

    print(statistics.pstdev(new_list))

except:
    print("Please don't include any characters or symbols")
