#WAF that replace all occurrences of "Java" with "Python" in above file.

def replace_all_occurrences(str1, str2):
    with open("Lecture7/LetsPractice/practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace(str1, str2)
    print(new_data)

    with open("Lecture7/LetsPractice/practice.txt", "w") as f:
        data = f.write(new_data)


str1 = "Java"
str2 = "Python"
replace_all_occurrences(str1, str2)