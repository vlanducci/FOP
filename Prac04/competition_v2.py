#
# 
#

numJudges = 7
numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc): "))
comp = 0

while (numCompetitors < 3) or (numCompetitors > 16):
    numCompetitors = int(input("Error - Re-enter number of competitors (between 3 and 16 inc): "))

for comp in range(0, (numCompetitors-1)):
    totalC = 0
    print("input scores between 0 and 10 for each Judge")
    for j in range(0, (numJudges-1)):
        scoreJ = int(input("Score for judge: "))
        while (scoreJ < 0) or (scoreJ > 10):
            scoreJ = int(input("Error - re-enter score (0-10): "))
        totalC = totalC + scoreJ
    scoreC = totalC/numJudges
    print("Score for competitor ", j ," is", scoreC)

