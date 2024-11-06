from dataStructures.Team import Team

# game class to help group data game by game
class Game():
    def __init__(self, gameId: int, teamOneName: str, teamTwoName: str) -> None:
        self.gameId = gameId

        self.teamOne: Team = Team(teamOneName)
        self.teamTwo: Team = Team(teamTwoName)

    # helps process data one play at a time
    def processSinglePlay(self, playData: tuple):
        if self.teamOne.teamName == playData.OffenseTeam:
            self.teamOne.isOffense(playData)
            self.teamTwo.isDefense(playData)
        else:
            self.teamOne.isDefense(playData)
            self.teamTwo.isOffense(playData)
