# Laymen's Terms
"""

The program is trying to use the Final.txt to display numbers of grades,
the average grade, and the percentage of grades that are above the average.
Display Number of test_scores in list (Final.txt)
Add numbers in list and divide by number of test_scores in list to get
average_grade
Compare test_scores on Final.txt to average_grade;
if test_score > average_score
add 1 to num_scores_above_average
use num_scores_above_average / number of test scores = percent_above_average
return num_grades, avg_grade, and percent_above_average
(For Test;)
Number of grades: 24
Average grade: 83.25
% of grades above average: 54.17
"""
# Pseudo Code
"""
open file (Final.txt)
make variable for grades strip from list
len(grades) get length of list
Int counter and sum of grades
add grades togeather for sum
average equasion is sum(grades)/len(grades)
int counter and set sum to '0'
num = 0 to get started with above average grades
if grade is greather than average
num +=1
use the "{0:2f}%" for equasion and
(100*num)/len(grades) for formatting percentage
print "num of grades"
print" average grade"
print "% of grades > average" 
"""
# Exam End

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades)/len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percent of grades above average: {0:.2f}%".format(100 * num / len(grades)))
