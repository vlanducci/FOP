#
# 
#

numJudges = 7
numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc): "))
comp = 0

for comp in range(0, numCompetitors-1):
    totalC = 0
    print("input scores between 0 and 10 for each Judge")
    for j in range(0, numJudges-1):
        scoreJ = int(input("Score for judge: "))
        totalC = totalC + scoreJ
    scoreC = totalC/numJudges
    print("Score for competitor", j, "is", scoreC)

