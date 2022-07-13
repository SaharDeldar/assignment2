


Scores=[]
Totalscores=0
Countofstudents=int(input("enter number of students = "))
for numbers in range(Countofstudents):
    Score=int(input('score = '))
    if 0<=Score<=20:
        Scores.append(Score)
        Totalscores+=Scores[numbers]
    else:
        print("Enter the correct grade")
        break
maxscore=Scores[0]
minscore=Scores[0]
for i in Scores:
    if i >= maxscore:
        maxscore=i
    if i < minscore:
        minscore=i
print(Scores)
print("minscore = "+str(minscore))
print("maxscore = "+str(maxscore))
print("avg = "+str(Totalscores/Countofstudents))


