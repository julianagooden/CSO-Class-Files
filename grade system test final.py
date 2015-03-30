hw_scores = [100,100,100,85,65,100,100,100,0,105,105]
hw_average = sum(hw_scores) / float(len(hw_scores))
hwFinalGrade = hw_average * .20
print hwFinalGrade

quiz_scores = [93,87,100,100,100,72]
quiz_average = sum(quiz_scores) / float(len(quiz_scores))
quizFinalGrade = quiz_average * .25
print quizFinalGrade

test_scores = [98,92,75,80]
test_average = sum(test_scores) / float(len(test_scores))
testFinalGrade = test_average * .30
print testFinalGrade

midterm_score = 85
midtermFinalGrade = midterm_score * .10
print midtermFinalGrade

x = hwFinalGrade + quizFinalGrade + testFinalGrade + midtermFinalGrade
finalexam = 89.5 - x
finaleExamFinaleGrade = finalexam / .15
print finaleExamFinaleGrade