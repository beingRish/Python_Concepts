count = 1
while count <= 5:
    print("hello")
    count += 1

i = 1
while i <= 5:
    print("being_rish_")
    i += 1

#print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

print("reversed")
i = 5
while i >= 1:
    print(i)
    i -= 1

#break
print("break")
i = 1
while i<=5:
    if(i==3):
        break
    print(i)
    i+=1

#continue
print("continue")
i = 0
while i <= 5:
    if(i%2==0):
        i+=1
        continue    #skip
    print(i)
    i+=1