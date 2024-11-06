# Team class to help store data for each game
class Team():
    def __init__(self, teamName: str) -> None:
        self.teamName = teamName

        # offensive stats

        # TARGET
        self.points: int = 0

        # Features
        self.numberOfFirstDowns: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.thirdDownAttempts: dict[str: float] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.thirdDownConversionsSuccessful: dict[str: float] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.fourthDownAttempts: dict[str: float] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.fourthDownConversionsSuccessful: dict[str: float] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.yardsMovedPerQuarter: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfEachPlayFormation: dict[str: int] = {}
        self.numOfEachPlayType: dict[str: int] = {}
        self.numOfEachTypeOfRush: dict[str: int] = {}
        self.numOfEachPassType: dict[str: int] = {}
        self.numOfOffensivePenalties: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfOffensivePenaltyYards: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfFumbles: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfInterceptionsThrown: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.passCompletionRate: dict[str: int] = {
            'q1- attempted': 0,
            'q1- completed': 0,
            'q2- attempted': 0,
            'q2- completed': 0,
            'q3- attempted': 0,
            'q3- completed': 0,
            'q4- attempted': 0,
            'q4- completed': 0,
        }
        self.numOfTimesSacked: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.twoPointConversionSuccesses = 0
        self.twoPointConversionAttempts = 0

        # Defensive Stats
        self.yardsAllowedPerQuarter: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfSacks: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfInterceptionsCaught: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfDefensivePenalties: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }
        self.numOfDefensivePenaltyYards: dict[str: int] = {
            'q1': 0,
            'q2': 0,
            'q3': 0,
            'q4': 0
        }

    def isDefense(self, playData):

        if playData.Quarter == 1:
            self.yardsAllowedPerQuarter['q1'] += playData.Yards
        elif playData.Quarter == 2:
            self.yardsAllowedPerQuarter['q2'] += playData.Yards
        elif playData.Quarter == 3:
            self.yardsAllowedPerQuarter['q3'] += playData.Yards
        elif playData.Quarter == 4:
            self.yardsAllowedPerQuarter['q4'] += playData.Yards


        if playData.Quarter == 1:
            self.numOfSacks['q1'] += playData.IsSack
        elif playData.Quarter == 2:
            self.numOfSacks['q2'] += playData.IsSack
        elif playData.Quarter == 3:
            self.numOfSacks['q3'] += playData.IsSack
        elif playData.Quarter == 4:
            self.numOfSacks['q4'] += playData.IsSack


        if playData.Quarter == 1:
            self.numOfInterceptionsCaught['q1'] += playData.IsInterception
        elif playData.Quarter == 2:
            self.numOfInterceptionsCaught['q2'] += playData.IsInterception
        elif playData.Quarter == 3:
            self.numOfInterceptionsCaught['q3'] += playData.IsInterception
        elif playData.Quarter == 4:
            self.numOfInterceptionsCaught['q4'] += playData.IsInterception


        if playData.PenaltyTeam == self.teamName:
            if playData.Quarter == 1:
                self.numOfDefensivePenalties['q1'] += 1
                self.numOfDefensivePenaltyYards['q1'] += playData.PenaltyYards
            elif playData.Quarter == 2:
                self.numOfDefensivePenalties['q2'] += 1
                self.numOfDefensivePenaltyYards['q2'] += playData.PenaltyYards
            elif playData.Quarter == 3:
                self.numOfDefensivePenalties['q3'] += 1
                self.numOfDefensivePenaltyYards['q3'] += playData.PenaltyYards
            elif playData.Quarter == 4:
                self.numOfDefensivePenalties['q4'] += 1
                self.numOfDefensivePenaltyYards['q4'] += playData.PenaltyYards
                
    def isOffense(self, playData):
        # tally points
        if playData.IsTouchdown == 1:
            self.points += 6
        elif playData.IsTwoPointConversionSuccessful == 1:
            self.points += 2
        elif 'FIELD GOAL IS GOOD' in playData.Description:
            self.points += 3
        elif 'EXTRA POINT IS GOOD' in playData.Description:
            self.points += 1

        
        # handle first downs
        if playData.Yards >= playData.ToGo:
            if playData.Quarter == 1:
                self.numberOfFirstDowns['q1'] += 1
            elif playData.Quarter == 2:
                self.numberOfFirstDowns['q2'] += 1
            elif playData.Quarter == 3:
                self.numberOfFirstDowns['q3'] += 1
            elif playData.Quarter == 4:
                self.numberOfFirstDowns['q4'] += 1

        
        # handle third down conversion
        if playData.Down == 3:
            if playData.Quarter == 1:
                self.thirdDownAttempts['q1'] += 1
            elif playData.Quarter == 2:
                self.thirdDownAttempts['q2'] += 1
            elif playData.Quarter == 3:
                self.thirdDownAttempts['q3'] += 1
            elif playData.Quarter == 4:
                self.thirdDownAttempts['q4'] += 1

        if (playData.Yards >= playData.ToGo) and playData.Down == 3:
            if playData.Quarter == 1:
                self.thirdDownConversionsSuccessful['q1'] += 1
            elif playData.Quarter == 2:
                self.thirdDownConversionsSuccessful['q2'] += 1
            elif playData.Quarter == 3:
                self.thirdDownConversionsSuccessful['q3'] += 1
            elif playData.Quarter == 4:
                self.thirdDownConversionsSuccessful['q4'] += 1


        # handle fourth down conversion
        if playData.Down == 4:
            if playData.Quarter == 1:
                self.fourthDownAttempts['q1'] += 1
            elif playData.Quarter == 2:
                self.fourthDownAttempts['q2'] += 1
            elif playData.Quarter == 3:
                self.fourthDownAttempts['q3'] += 1
            elif playData.Quarter == 4:
                self.fourthDownAttempts['q4'] += 1

        if (playData.Yards >= playData.ToGo) and playData.Down == 4:
            if playData.Quarter == 1:
                self.fourthDownConversionsSuccessful['q1'] += 1
            elif playData.Quarter == 2:
                self.fourthDownConversionsSuccessful['q2'] += 1
            elif playData.Quarter == 3:
                self.fourthDownConversionsSuccessful['q3'] += 1
            elif playData.Quarter == 4:
                self.fourthDownConversionsSuccessful['q4'] += 1
        

        # handle yards moved 
        if playData.Quarter == 1:
            self.yardsMovedPerQuarter['q1'] += playData.Yards
        elif playData.Quarter == 2:
            self.yardsMovedPerQuarter['q2'] += playData.Yards
        elif playData.Quarter == 3:
            self.yardsMovedPerQuarter['q3'] += playData.Yards
        elif playData.Quarter == 4:
            self.yardsMovedPerQuarter['q4'] += playData.Yards


        # count formations
        if playData.Formation in self.numOfEachPlayFormation:
            self.numOfEachPlayFormation[playData.Formation] += 1
        else:
            self.numOfEachPlayFormation[playData.Formation] = 1

        
        # count play types
        if playData.PlayType in self.numOfEachPlayType:
            self.numOfEachPlayType[playData.PlayType] += 1
        else:
            self.numOfEachPlayType[playData.PlayType] = 1


        # count rush types
        if playData.RushDirection in self.numOfEachTypeOfRush:
            self.numOfEachTypeOfRush[playData.RushDirection] += 1
        else:
            self.numOfEachTypeOfRush[playData.RushDirection] = 1


        # count pass types
        if playData.PassType in self.numOfEachPassType:
            self.numOfEachPassType[playData.PassType] += 1
        else:
            self.numOfEachPassType[playData.PassType] = 1



        if playData.PenaltyTeam == self.teamName:
            if playData.Quarter == 1:
                self.numOfOffensivePenalties['q1'] += 1
                self.numOfOffensivePenaltyYards['q1'] += playData.PenaltyYards
            elif playData.Quarter == 2:
                self.numOfOffensivePenalties['q2'] += 1
                self.numOfOffensivePenaltyYards['q2'] += playData.PenaltyYards
            elif playData.Quarter == 3:
                self.numOfOffensivePenalties['q3'] += 1
                self.numOfOffensivePenaltyYards['q3'] += playData.PenaltyYards
            elif playData.Quarter == 4:
                self.numOfOffensivePenalties['q4'] += 1
                self.numOfOffensivePenaltyYards['q4'] += playData.PenaltyYards


        # count fumbles
        if playData.Quarter == 1:
            self.numOfFumbles['q1'] += playData.IsFumble
        elif playData.Quarter == 2:
            self.numOfFumbles['q2'] += playData.IsFumble
        elif playData.Quarter == 3:
            self.numOfFumbles['q3'] += playData.IsFumble
        elif playData.Quarter == 4:
            self.numOfFumbles['q4'] += playData.IsFumble


        # count interceptions
        if playData.Quarter == 1:
            self.numOfInterceptionsThrown['q1'] += playData.IsInterception
        elif playData.Quarter == 2:
            self.numOfInterceptionsThrown['q2'] += playData.IsInterception
        elif playData.Quarter == 3:
            self.numOfInterceptionsThrown['q3'] += playData.IsInterception
        elif playData.Quarter == 4:
            self.numOfInterceptionsThrown['q4'] += playData.IsInterception


        # pass completion rate
        if playData.IsPass:

            if playData.Quarter == 1:
                self.passCompletionRate['q1- attempted'] += 1
                if not playData.IsIncomplete:
                    self.passCompletionRate['q1- completed'] += 1

            elif playData.Quarter == 2:
                self.passCompletionRate['q2- attempted'] += 1
                if not playData.IsIncomplete:
                    self.passCompletionRate['q2- completed'] += 1

            elif playData.Quarter == 3:
                self.passCompletionRate['q3- attempted'] += 1
                if not playData.IsIncomplete:
                    self.passCompletionRate['q3- completed'] += 1

            elif playData.Quarter == 4:
                self.passCompletionRate['q4- attempted'] += 1
                if not playData.IsIncomplete:
                    self.passCompletionRate['q4- completed'] += 1


        if playData.Quarter == 1:
            self.numOfTimesSacked['q1'] += playData.IsSack
        elif playData.Quarter == 2:
            self.numOfTimesSacked['q2'] += playData.IsSack
        elif playData.Quarter == 3:
            self.numOfTimesSacked['q3'] += playData.IsSack
        elif playData.Quarter == 4:
            self.numOfTimesSacked['q4'] += playData.IsSack


        # 2 pt conversion stats
        if playData.IsTwoPointConversion:
            self.twoPointConversionAttempts += 1
        
        if playData.IsTwoPointConversionSuccessful:
            self.twoPointConversionSuccesses += 1
