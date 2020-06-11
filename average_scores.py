"""
Program:  average_score.py
Author:  Lisa Kilmer
The purpose of this program is to have user enter 3 scores and find the average.
input first name, last name, age and calculates average score of 3 entered scores.
prints out inputs and average score rounded to 2 decimal points.
"""

def average(score1, score2, score3):
    score1 = input("Enter score1: ")
    if score1 < 0:
        raise ValueError
    score2 = input("Enter score2: ")
    if score2 < 0:
        raise ValueError
    score3 = input("Enter score3: ")
    if score3 < 0:
        raise ValueError
    return (int(score1) + int(score2) + int(score3))/3


if __name__ == '__main__':
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter your age: ")
    average_scores = average()
    print(f"{last_name}, {first_name} age: {age}  average grade: {str(round(average_scores, 2))}")

"""
I ran tests with different names and ages and scores:
Lisa    Kilmer  45  13  34  68
Joe     Smith   34  15  58  12

"""