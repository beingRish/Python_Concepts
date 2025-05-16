with open("Lecture7/demo2.txt", "r") as f:
    data = f.read()
    print(data)

with open("Lecture7/demo2.txt", "w") as f:
    f.write("new data")