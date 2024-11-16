from dataStructures.Game import Game

def gameToDictionary(game: Game) -> list[dict, dict]:
    teamOneStats = {
        'game_id': game.gameId,
        'points': game.teamOne.points,
        'number_of_first_downs_q1': game.teamOne.numberOfFirstDowns['q1'],
        'number_of_first_downs_q2': game.teamOne.numberOfFirstDowns['q2'],
        'number_of_first_downs_q3': game.teamOne.numberOfFirstDowns['q3'],
        'number_of_first_downs_q4': game.teamOne.numberOfFirstDowns['q4'],
        'third_down_attempts_q1': game.teamOne.thirdDownAttempts['q1'],
        'third_down_attempts_q2': game.teamOne.thirdDownAttempts['q2'],
        'third_down_attempts_q3': game.teamOne.thirdDownAttempts['q3'],
        'third_down_attempts_q4': game.teamOne.thirdDownAttempts['q4'],
        'number_of_successful_third_downs_q1': game.teamOne.thirdDownConversionsSuccessful['q1'],
        'number_of_successful_third_downs_q2': game.teamOne.thirdDownConversionsSuccessful['q2'],
        'number_of_successful_third_downs_q3': game.teamOne.thirdDownConversionsSuccessful['q3'],
        'number_of_successful_third_downs_q4': game.teamOne.thirdDownConversionsSuccessful['q4'],
        'fourth_down_attempts_q1': game.teamOne.fourthDownAttempts['q1'],
        'fourth_down_attempts_q2': game.teamOne.fourthDownAttempts['q2'],
        'fourth_down_attempts_q3': game.teamOne.fourthDownAttempts['q3'],
        'fourth_down_attempts_q4': game.teamOne.fourthDownAttempts['q4'],
        'number_of_successful_fourth_downs_q1': game.teamOne.fourthDownConversionsSuccessful['q1'],
        'number_of_successful_fourth_downs_q2': game.teamOne.fourthDownConversionsSuccessful['q2'],
        'number_of_successful_fourth_downs_q3': game.teamOne.fourthDownConversionsSuccessful['q3'],
        'number_of_successful_fourth_downs_q4': game.teamOne.fourthDownConversionsSuccessful['q4'],
        'yards_moved_q1': game.teamOne.yardsMovedPerQuarter['q1'],
        'yards_moved_q2': game.teamOne.yardsMovedPerQuarter['q2'],
        'yards_moved_q3': game.teamOne.yardsMovedPerQuarter['q3'],
        'yards_moved_q4': game.teamOne.yardsMovedPerQuarter['q4'],
        'num_of_offensive_penalties_q1': game.teamOne.numOfOffensivePenalties['q1'],
        'num_of_offensive_penalties_q2': game.teamOne.numOfOffensivePenalties['q2'],
        'num_of_offensive_penalties_q3': game.teamOne.numOfOffensivePenalties['q3'],
        'num_of_offensive_penalties_q4': game.teamOne.numOfOffensivePenalties['q4'],
        'num_of_offensive_penalty_yards_q1': game.teamOne.numOfOffensivePenaltyYards['q1'],
        'num_of_offensive_penalty_yards_q2': game.teamOne.numOfOffensivePenaltyYards['q2'],
        'num_of_offensive_penalty_yards_q3': game.teamOne.numOfOffensivePenaltyYards['q3'],
        'num_of_offensive_penalty_yards_q4': game.teamOne.numOfOffensivePenaltyYards['q4'],
        'num_of_fumbles_q1': game.teamOne.numOfFumbles['q1'],
        'num_of_fumbles_q2': game.teamOne.numOfFumbles['q2'],
        'num_of_fumbles_q3': game.teamOne.numOfFumbles['q3'],
        'num_of_fumbles_q4': game.teamOne.numOfFumbles['q4'],
        'num_of_interceptions_thrown_q1': game.teamOne.numOfInterceptionsThrown['q1'],
        'num_of_interceptions_thrown_q2': game.teamOne.numOfInterceptionsThrown['q2'],
        'num_of_interceptions_thrown_q3': game.teamOne.numOfInterceptionsThrown['q3'],
        'num_of_interceptions_thrown_q4': game.teamOne.numOfInterceptionsThrown['q4'],
        'num_of_passes_attempted_q1': game.teamOne.passCompletionRate['q1- attempted'],
        'num_of_passes_completed_q1': game.teamOne.passCompletionRate['q1- completed'],
        'num_of_passes_attempted_q2': game.teamOne.passCompletionRate['q2- attempted'],
        'num_of_passes_completed_q2': game.teamOne.passCompletionRate['q2- completed'],
        'num_of_passes_attempted_q3': game.teamOne.passCompletionRate['q3- attempted'],
        'num_of_passes_completed_q3': game.teamOne.passCompletionRate['q3- completed'],
        'num_of_passes_attempted_q4': game.teamOne.passCompletionRate['q4- attempted'],
        'num_of_passes_completed_q4': game.teamOne.passCompletionRate['q4- completed'],
        'num_of_times_sacked_q1': game.teamOne.numOfTimesSacked['q1'],
        'num_of_times_sacked_q2': game.teamOne.numOfTimesSacked['q2'],
        'num_of_times_sacked_q3': game.teamOne.numOfTimesSacked['q3'],
        'num_of_times_sacked_q4': game.teamOne.numOfTimesSacked['q4'],
        'num_of_attempted_two_pt_conversions': game.teamOne.twoPointConversionAttempts,
        'num_of_completed_two_pt_conversions': game.teamOne.twoPointConversionAttempts,
        'yards_allowed_q1': game.teamOne.yardsAllowedPerQuarter['q1'],
        'yards_allowed_q2': game.teamOne.yardsAllowedPerQuarter['q2'],
        'yards_allowed_q3': game.teamOne.yardsAllowedPerQuarter['q3'],
        'yards_allowed_q4': game.teamOne.yardsAllowedPerQuarter['q4'],
        'num_of_sacks_q1': game.teamOne.numOfSacks['q1'],
        'num_of_sacks_q2': game.teamOne.numOfSacks['q2'],
        'num_of_sacks_q3': game.teamOne.numOfSacks['q3'],
        'num_of_sacks_q4': game.teamOne.numOfSacks['q4'],
        'num_of_interceptions_caught_q1': game.teamOne.numOfInterceptionsCaught['q1'],
        'num_of_interceptions_caught_q2': game.teamOne.numOfInterceptionsCaught['q2'],
        'num_of_interceptions_caught_q3': game.teamOne.numOfInterceptionsCaught['q3'],
        'num_of_interceptions_caught_q4': game.teamOne.numOfInterceptionsCaught['q4'],
        'num_of_defensive_penalties_q1': game.teamOne.numOfDefensivePenalties['q1'],
        'num_of_defensive_penalties_q2': game.teamOne.numOfDefensivePenalties['q2'],
        'num_of_defensive_penalties_q3': game.teamOne.numOfDefensivePenalties['q3'],
        'num_of_defensive_penalties_q4': game.teamOne.numOfDefensivePenalties['q4'],
        'num_of_defensive_penalty_yards_q1': game.teamOne.numOfDefensivePenaltyYards['q1'],
        'num_of_defensive_penalty_yards_q2': game.teamOne.numOfDefensivePenaltyYards['q2'],
        'num_of_defensive_penalty_yards_q3': game.teamOne.numOfDefensivePenaltyYards['q3'],
        'num_of_defensive_penalty_yards_q4': game.teamOne.numOfDefensivePenaltyYards['q4'],
    }

    for playFormation in game.teamOne.numOfEachPlayFormation:
        key = 'num_of_' + playFormation
        teamOneStats[key] = game.teamOne.numOfEachPlayFormation[playFormation]

    for playType in game.teamOne.numOfEachPlayType:
        key = 'num_of_' + playType
        teamOneStats[key] = game.teamOne.numOfEachPlayType[playType]

    for rushType in game.teamOne.numOfEachTypeOfRush:
        key = 'num_of_' + rushType
        teamOneStats[key] = game.teamOne.numOfEachTypeOfRush[rushType]

    for passType in game.teamOne.numOfEachPassType:
        key = 'num_of_' + passType
        teamOneStats[key] = game.teamOne.numOfEachPassType[passType]


    teamTwoStats = {
        'game_id': game.gameId,
        'points': game.teamTwo.points,
        'number_of_first_downs_q1': game.teamTwo.numberOfFirstDowns['q1'],
        'number_of_first_downs_q2': game.teamTwo.numberOfFirstDowns['q2'],
        'number_of_first_downs_q3': game.teamTwo.numberOfFirstDowns['q3'],
        'number_of_first_downs_q4': game.teamTwo.numberOfFirstDowns['q4'],
        'third_down_attempts_q1': game.teamTwo.thirdDownAttempts['q1'],
        'third_down_attempts_q2': game.teamTwo.thirdDownAttempts['q2'],
        'third_down_attempts_q3': game.teamTwo.thirdDownAttempts['q3'],
        'third_down_attempts_q4': game.teamTwo.thirdDownAttempts['q4'],
        'number_of_successful_third_downs_q1': game.teamTwo.thirdDownConversionsSuccessful['q1'],
        'number_of_successful_third_downs_q2': game.teamTwo.thirdDownConversionsSuccessful['q2'],
        'number_of_successful_third_downs_q3': game.teamTwo.thirdDownConversionsSuccessful['q3'],
        'number_of_successful_third_downs_q4': game.teamTwo.thirdDownConversionsSuccessful['q4'],
        'fourth_down_attempts_q1': game.teamTwo.fourthDownAttempts['q1'],
        'fourth_down_attempts_q2': game.teamTwo.fourthDownAttempts['q2'],
        'fourth_down_attempts_q3': game.teamTwo.fourthDownAttempts['q3'],
        'fourth_down_attempts_q4': game.teamTwo.fourthDownAttempts['q4'],
        'number_of_successful_fourth_downs_q1': game.teamTwo.fourthDownConversionsSuccessful['q1'],
        'number_of_successful_fourth_downs_q2': game.teamTwo.fourthDownConversionsSuccessful['q2'],
        'number_of_successful_fourth_downs_q3': game.teamTwo.fourthDownConversionsSuccessful['q3'],
        'number_of_successful_fourth_downs_q4': game.teamTwo.fourthDownConversionsSuccessful['q4'],
        'yards_moved_q1': game.teamTwo.yardsMovedPerQuarter['q1'],
        'yards_moved_q2': game.teamTwo.yardsMovedPerQuarter['q2'],
        'yards_moved_q3': game.teamTwo.yardsMovedPerQuarter['q3'],
        'yards_moved_q4': game.teamTwo.yardsMovedPerQuarter['q4'],
        'num_of_offensive_penalties_q1': game.teamTwo.numOfOffensivePenalties['q1'],
        'num_of_offensive_penalties_q2': game.teamTwo.numOfOffensivePenalties['q2'],
        'num_of_offensive_penalties_q3': game.teamTwo.numOfOffensivePenalties['q3'],
        'num_of_offensive_penalties_q4': game.teamTwo.numOfOffensivePenalties['q4'],
        'num_of_offensive_penalty_yards_q1': game.teamTwo.numOfOffensivePenaltyYards['q1'],
        'num_of_offensive_penalty_yards_q2': game.teamTwo.numOfOffensivePenaltyYards['q2'],
        'num_of_offensive_penalty_yards_q3': game.teamTwo.numOfOffensivePenaltyYards['q3'],
        'num_of_offensive_penalty_yards_q4': game.teamTwo.numOfOffensivePenaltyYards['q4'],
        'num_of_fumbles_q1': game.teamTwo.numOfFumbles['q1'],
        'num_of_fumbles_q2': game.teamTwo.numOfFumbles['q2'],
        'num_of_fumbles_q3': game.teamTwo.numOfFumbles['q3'],
        'num_of_fumbles_q4': game.teamTwo.numOfFumbles['q4'],
        'num_of_interceptions_thrown_q1': game.teamTwo.numOfInterceptionsThrown['q1'],
        'num_of_interceptions_thrown_q2': game.teamTwo.numOfInterceptionsThrown['q2'],
        'num_of_interceptions_thrown_q3': game.teamTwo.numOfInterceptionsThrown['q3'],
        'num_of_interceptions_thrown_q4': game.teamTwo.numOfInterceptionsThrown['q4'],
        'num_of_passes_attempted_q1': game.teamTwo.passCompletionRate['q1- attempted'],
        'num_of_passes_completed_q1': game.teamTwo.passCompletionRate['q1- completed'],
        'num_of_passes_attempted_q2': game.teamTwo.passCompletionRate['q2- attempted'],
        'num_of_passes_completed_q2': game.teamTwo.passCompletionRate['q2- completed'],
        'num_of_passes_attempted_q3': game.teamTwo.passCompletionRate['q3- attempted'],
        'num_of_passes_completed_q3': game.teamTwo.passCompletionRate['q3- completed'],
        'num_of_passes_attempted_q4': game.teamTwo.passCompletionRate['q4- attempted'],
        'num_of_passes_completed_q4': game.teamTwo.passCompletionRate['q4- completed'],
        'num_of_times_sacked_q1': game.teamTwo.numOfTimesSacked['q1'],
        'num_of_times_sacked_q2': game.teamTwo.numOfTimesSacked['q2'],
        'num_of_times_sacked_q3': game.teamTwo.numOfTimesSacked['q3'],
        'num_of_times_sacked_q4': game.teamTwo.numOfTimesSacked['q4'],
        'num_of_attempted_two_pt_conversions': game.teamTwo.twoPointConversionAttempts,
        'num_of_completed_two_pt_conversions': game.teamTwo.twoPointConversionAttempts,
        'yards_allowed_q1': game.teamTwo.yardsAllowedPerQuarter['q1'],
        'yards_allowed_q2': game.teamTwo.yardsAllowedPerQuarter['q2'],
        'yards_allowed_q3': game.teamTwo.yardsAllowedPerQuarter['q3'],
        'yards_allowed_q4': game.teamTwo.yardsAllowedPerQuarter['q4'],
        'num_of_sacks_q1': game.teamTwo.numOfSacks['q1'],
        'num_of_sacks_q2': game.teamTwo.numOfSacks['q2'],
        'num_of_sacks_q3': game.teamTwo.numOfSacks['q3'],
        'num_of_sacks_q4': game.teamTwo.numOfSacks['q4'],
        'num_of_interceptions_caught_q1': game.teamTwo.numOfInterceptionsCaught['q1'],
        'num_of_interceptions_caught_q2': game.teamTwo.numOfInterceptionsCaught['q2'],
        'num_of_interceptions_caught_q3': game.teamTwo.numOfInterceptionsCaught['q3'],
        'num_of_interceptions_caught_q4': game.teamTwo.numOfInterceptionsCaught['q4'],
        'num_of_defensive_penalties_q1': game.teamTwo.numOfDefensivePenalties['q1'],
        'num_of_defensive_penalties_q2': game.teamTwo.numOfDefensivePenalties['q2'],
        'num_of_defensive_penalties_q3': game.teamTwo.numOfDefensivePenalties['q3'],
        'num_of_defensive_penalties_q4': game.teamTwo.numOfDefensivePenalties['q4'],
        'num_of_defensive_penalty_yards_q1': game.teamTwo.numOfDefensivePenaltyYards['q1'],
        'num_of_defensive_penalty_yards_q2': game.teamTwo.numOfDefensivePenaltyYards['q2'],
        'num_of_defensive_penalty_yards_q3': game.teamTwo.numOfDefensivePenaltyYards['q3'],
        'num_of_defensive_penalty_yards_q4': game.teamTwo.numOfDefensivePenaltyYards['q4'],
    }

    for playFormation in game.teamTwo.numOfEachPlayFormation:
        key = 'num_of_' + playFormation
        teamTwoStats[key] = game.teamTwo.numOfEachPlayFormation[playFormation]

    for playType in game.teamTwo.numOfEachPlayType:
        key = 'num_of_' + playType
        teamTwoStats[key] = game.teamTwo.numOfEachPlayType[playType]

    for rushType in game.teamTwo.numOfEachTypeOfRush:
        key = 'num_of_' + rushType
        teamTwoStats[key] = game.teamTwo.numOfEachTypeOfRush[rushType]

    for passType in game.teamTwo.numOfEachPassType:
        key = 'num_of_' + passType
        teamTwoStats[key] = game.teamTwo.numOfEachPassType[passType]

    return [teamOneStats, teamTwoStats]
