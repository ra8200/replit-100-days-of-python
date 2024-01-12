import random

print("Bingo Card Maker")

# Initialize an empty list to represent the bingo grid.
# Function to generate a random number between 1 and 90.
def randomNumber():
  num = random.randint(1,90)
  return num
    
# List to store random numbers.
nums = []

# Generate 8 random numbers and add them to the 'numbers' list.
for i in range(8):
  number = randomNumber()
  if number not in nums:
    nums.append(number)

# Sort the numbers in ascending order.
nums.sort()

# Create the bingo grid as a 3x3 matrix.
# The center cell is "BINGO" and others are filled with sorted random numbers.
bingoBoard = [
  [ nums[0], nums[1], nums[2] ],
  [ nums[3], "BINGO!", nums[4] ],
  [ nums[5], nums[6], nums[7] ]
]

# Function to print the bingo grid in a formatted way.
def printNum():
  for row in bingoBoard:
    print(row)

# printNum()

print(nums)


