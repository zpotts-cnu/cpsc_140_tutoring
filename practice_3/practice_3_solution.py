# Don't worry about how I got the list of numbers, it is beyond the scope of this course.
usr_nums = [int(input(f"Please enter a whole number ({i} of 5): ")) for i in range(1, 6)]
print()  # Just a new line to separate the output

magic_num = 7  # A value I am defining to be used in your solution

# Your solution starts here:
print(f"The numbers you entered are: {usr_nums}")
print(f"The sum of those numbers are: {sum(usr_nums)}")

if magic_num in usr_nums:
    print("You guessed the magic number!")
    additional_num = int(input("Please enter an additional number: "))
    usr_nums.append(additional_num)
    print(f"Your new list is: {usr_nums}")

print(f"The first two numbers in your list are: {usr_nums[:2]}")
print(f"The highest number you entered is:", max(usr_nums))

lowest_num = min(usr_nums)
print("The lowest number is: " + str(lowest_num))  # I just am showing a different way to print the number.
usr_nums.remove(lowest_num)
print(f"The list after the lowest number is removed is: {usr_nums}")

# Another way to do the last part (Select every line of code and press 'CTRL + /' or remove the '#' character to run it)
# This removes the number from the list and returns it to be stored in lowest_num
# lowest_num = usr_nums.pop(usr_nums.index(min(usr_nums)))
# print(f"The lowest number is: {lowest_num}")
# print(f"The list after the lowest number is removed is: {usr_nums}")
