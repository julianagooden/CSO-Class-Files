hwgrades = []
numberOfGrades = int(raw_input('Input number of homework grades: '))

while len(hwgrades) < numberOfGrades:
    hwgrades.append(int(raw_input('Input homework grades: ')))

hwaverage = sum(hwgrades) / float(len(hwgrades))
hwfinalgrade = hwaverage * .20
if len(hwgrades) > 0: 
    print hwfinalgrade
else:
    print "Input not recognized"   


qgrades = []
numberOfGrades = int(raw_input('Input number of quiz grades: '))

while len(qgrades) < numberOfGrades:
    qgrades.append(int(raw_input('Input quiz grades: ')))

qaverage = sum(qgrades) / float(len(qgrades))
qfinalgrade = qaverage * .25
if len(qgrades) > 0: 
    print qfinalgrade
else:
    print "Input not recognized"  


tgrades = []
numberOfGrades = int(raw_input('Input number of test grades: '))

while len(tgrades) < numberOfGrades:
    tgrades.append(int(raw_input('Input test grades: ')))

taverage = sum(tgrades) / float(len(tgrades))
tfinalgrade = taverage * .30
if len(tgrades) > 0: 
    print tfinalgrade
else:
    print "Input not recognized"  


midtermgrades = []
numberOfGrades = int(raw_input('Input number of midterm grades: '))

while len(midtermgrades) < numberOfGrades:
    midtermgrades.append(int(raw_input('Input midterm grade(s): ')))

midtermaverage = sum(midtermgrades) / float(len(midtermgrades))
midtermfinalgrade = midtermaverage * .10
if len(midtermgrades) > 0: 
    print midtermfinalgrade
else:
    print "Input not recognized"  


x = hwfinalgrade + qfinalgrade + tfinalgrade +midtermfinalgrade 
finalexam = 89.5 - x
finalexamfinalgrade = finalexam / .15
print "This is what you need to get on the final exam in order to receive an A." 
print finalexamfinalgrade





