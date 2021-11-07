Score = 0
roundcomplete = False

def writeFile(qType, ): #did have a highscore file
  with open(qType) as f:
      with open("highScores.txt", "w") as f1:
          for line in f:
              f1.write(line)
