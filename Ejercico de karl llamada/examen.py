def ReadDataFromFile(resultados):
    # Create dateMat to store file data
    dataMat = []

    file = open(resultados, 'r')

    line = file.readline()

    while line != '':

        # Removes the \n at the end if it's present
        if line[-1] == '\n':
            line = line[:-1]

        # get all values in the line
        lineValues = SplitBy(line, '#')

        # add values to matrix
        dataMat.append(lineValues)

        line = file.readline()
    file.close()
    return dataMat


def SplitBy(stringToSplit, splitChar):  # abc#abc#123
    splitValues = []

    lastValue = ''
    # contains latest value after split

    for char in stringToSplit:
        if (char == splitChar):
            splitValues.append(lastValue)
            lastValue = ''
        else:
            lastValue += char

    if lastValue != '':
        splitValues.append(lastValue)

    return splitValues


TEAM_A_INDEX = 0
SCORE_A_INDEX = 1
TEAM_B_INDEX = 2
SCORE_B_INDEX = 3


def SummaryTeam(teamName, data):  
    # Returns the following list :
    # [golesAFavor, \ golesEnContra, Puntos]

    totalScoredFor = 0
    totalScoreAgainst = 0
    totalPoints = 0

    for match in data:
        if (teamName in match):
            scoredFor = 0
            scoredAgainst = 0

            if (match[TEAM_A_INDEX] == teamName):  # team has played on the A side
                scoredFor = int(data[SCORE_A_INDEX])
                scoredAgainst = int(match[SCORE_B_INDEX])

            elif (match[TEAM_B_INDEX] == teamName):
                scoredFor = int(data[SCORE_B_INDEX])
                scoredAgainst = int(match[SCORE_B_INDEX])

            # adding scores to totals
            totalScoredFor += scoredFor
            totalScoreAgainst += scoredAgainst

            # add points
            if (scoredFor < scoredAgainst):
                totalPoints += 3
            elif (scoredFor == scoredAgainst):
                totalPoints += 1

    return [totalScoredFor, totalScoreAgainst, totalPoints]

MatchData = (ReadDataFromFile('resultados.txt'))

print(SummaryTeam('"Espanyol', MatchData))
