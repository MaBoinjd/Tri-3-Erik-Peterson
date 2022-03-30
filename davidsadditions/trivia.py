# Defining Score variables 
x = 0
score = x

# Question One 
print("What is 8 + 88 + 888")
answer_1 = input("a)952\nb)984\nc)1783\nd)1054\n:")
if answer_1.lower() == "b" or answer_1.lower() == "984":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, 8 + 88 + 888 is 984")

# Question Two
print("Who was the 16th president of the United States?")
answer_2 = input("a)Barack Obama\nb)Richard Nixon\nc)Abraham Lincoln\nd)Theodore Roosevelt\n:")
if answer_2.lower() == "c" or answer_2.lower() == "abraham lincoln":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The 16th president was Abraham Lincoln")

# Question Three
print("True or False... The Eagles have won the Super Bowl LII?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")  

# Question Four
print("What year was Spider-Man: Homecoming released?")
answer_4 = input("a)2017\nb)2018\nc)2019\nd)2020\n:")
if answer_4.lower() == "a" or answer_4 == "2017":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Spider-Man: Homecoming was released in 2017")

# Question Five 
print("True or False... Adolf Hitler was assassinated by an American soldier?")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Adolf Hitler actually assassinated himself")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")