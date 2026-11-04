#imports
import time
import random

#introduction
score = 0
time.sleep(2)
print("Welcome to the foundational maths knowledge quiz.")
time.sleep(2)
print("There will be 10 basic arithmetic questions.")
time.sleep(2)
print("The questions will be marked and your final score alongside a grade will be displayed to you at the end.")
time.sleep(2)
print("No calculators or devices that may indicate the answers to you should be used during the quiz.")
time.sleep(2)
print("Pen or pencil with paper is suggested to carry out calculations during the quiz.")
time.sleep(7)
print("")

time.sleep(2)
print("The quiz starts now.")

#question1
Q1number1 = random.randint(1, 1000)
Q1number2 = random.randint(0, 1000)
Q1answer = Q1number1 + Q1number2
time.sleep(2)
Q1 = int(input(f"Q1) What is {Q1number1} + {Q1number2} equal to? "))
if Q1 == Q1answer:
    score += 1

#question2
Q2number1 = random.randint(1, 100)
Q2number2 = random.randint(0, 100)
Q2answer = Q2number1 * Q2number2
time.sleep(2)
Q2 = int(input(f"Q2) What is {Q2number1} multiplied by {Q2number2} equal to? "))
if Q2 == Q2answer:
    score += 1

#question3
Q3number1 = random.randint(4999, 9999)
Q3number2 = random.randint(0, 4998)
Q3answer = Q3number1 - Q3number2
time.sleep(2)
Q3 = int(input(f"Q3) What is {Q3number1} - {Q3number2} equal to? "))
if Q3 == Q3answer:
    score += 1

#question4
Q4number1 = random.randrange(5, 1000, 5)
Q4number2 = 5
Q4answer = Q4number1 / Q4number2
time.sleep(2)
Q4 = int(input(f"Q4) What is {Q4number1} divided by {Q4number2} equal to? "))
if Q4 == Q4answer:
    score += 1

#question5
Q5number1 = random.randint(1, 9999)
Q5number2 = random.randint(0, 9999)
Q5number3 = random.randint(0, 9999)
Q5answer = Q5number1 + Q5number2 + Q5number3
time.sleep(2)
Q5 = int(input(f"Q5) What is {Q5number1} + {Q5number2} + {Q5number3} equal to? "))
if Q5 == Q5answer:
    score += 1

#question6
Q6number1 = random.randint(4999, 9999)
Q6number2 = random.randint(1999, 4998)
Q6number3 = random.randint(1, 1998)
Q6answer = Q6number1 - Q6number2 - Q6number3
time.sleep(2)
Q6 = int(input(f"Q6) What is {Q6number1} - {Q6number2} - {Q6number3} equal to? "))
if Q6 == Q6answer:
    score += 1

#question7
Q7number1 = random.randint(1, 99)
Q7number2 = random.randint(1, 99)
Q7number3 = random.randint(1, 99)
Q7answer = Q7number1 * Q7number2 * Q7number3
time.sleep(2)
Q7 = int(input(f"Q7) What is {Q7number1} multiplied by {Q7number2} multiplied by {Q7number3} equal to? "))
if Q7 == Q7answer:
    score += 1

#question8
Q8number1 = random.randrange(7, 7000, 7)
Q8number2 = 7
Q8answer = Q8number1 / Q8number2
time.sleep(2)
Q8 = int(input(f"Q8) What is {Q8number1} divided by {Q8number2} equal to? "))
if Q8 == Q8answer:
    score += 1

#question9
Q9number1 = random.randint(1, 4999)
Q9number2 = random.randint(1, 4999)
Q9number3 = 2
Q9answer = (Q9number1 + Q9number2) / Q9number3
time.sleep(2)
Q9 = float(input(f"Q9) What is ({Q9number1} + {Q9number2}) divided by {Q9number3} equal to? "))
if Q9 == Q9answer:
    score += 1

#question10
Q10number1 = random.randint(4999, 9999)
Q10number2 = random.randint(1, 4998)
Q10number3 = 5
Q10answer = (Q10number1 - Q10number2) / Q10number3
time.sleep(2)
Q10 = float(input(f"Q10) What is ({Q10number1} - {Q10number2}) divided by {Q10number3} equal to? "))
if Q10 == Q10answer:
    score += 1

if score == 10:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade A*.")
elif score >= 8:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade A.")
elif score == 7:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade B.")
elif score == 6:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade C.")
elif score == 5:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade D.")
elif score == 4:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade E.")
else:
    time.sleep(2)
    print(f"Your score is {score}/10, which is a grade F.")
    
    
