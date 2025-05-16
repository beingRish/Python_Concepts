# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("Lecture7/LetsPractice/practice2.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)