'''
WAF to find in which line of the file does the word "learning" occur first.
Print -1 if word not ound.
'''

def check_for_line():
    line_no = 1
    word = "programming"
    data = True
    with open("Lecture7/LetsPractice/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()
