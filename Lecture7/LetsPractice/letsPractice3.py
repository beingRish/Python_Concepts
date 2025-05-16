#Search if the word "learning" exists in the file or not.

def check_for_word():
    word = "learning"
    with open("Lecture7/LetsPractice/practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not Found")

check_for_word()