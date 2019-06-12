import player
import csv
import numpy


def load_players(path):
    players = []
    with open(path, mode='r', encoding = 'utf8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            players.append(
                player.Player(row['Name'], row['Position'], row['Crossing'], row['Finishing'], row['HeadingAccuracy'],
                              row['ShortPassing'], row['Volleys'], row['Dribbling'], row['Curve'], row['FKAccuracy'],
                              row['LongPassing'], row['BallControl'], row['Acceleration'], row['SprintSpeed'],
                              row['Agility'], row['Reactions'],
                              row['Balance'], row['ShotPower'], row['Jumping'], row['Stamina'], row['Strength'],
                              row['LongShots'],
                              row['Aggression'], row['Interceptions'], row['Positioning'], row['Vision'],
                              row['Penalties'], row['Composure'], row['Marking'],
                              row['StandingTackle'], row['SlidingTackle'], row['GKDiving'], row['GKHandling'],
                              row['GKKicking'], row['GKPositioning'], row['GKReflexes'], row['Overall']))
    return players


def select_goalkeepers(players_list):
    return [player for player in players_list if (player.position == "GK")]


def select_centre_backs(players_list):
    return [player for player in players_list
            if (player.position == "CB")
            or (player.position == "RCB")
            or (player.position == "LCB")]


def select_side_backs(players_list):
    return [player for player in players_list
            if (player.position == "LB")
            or (player.position == "LWB")
            or (player.position == "RB")
            or (player.position == "RWB")]


def select_centre_midfielders(players_list):
    return [player for player in players_list
            if (player.position == "CM")
            or (player.position == "CDM")
            or (player.position == "CAM")
            or (player.position == "LCM")
            or (player.position == "RCM")
            or (player.position == "LDM")
            or (player.position == "RDM")
            or (player.position == "LAM")
            or (player.position == "RAM")]


def select_wingers(players_list):
    return [player for player in players_list
            if (player.position == "LM")
            or (player.position == "RM")
            or (player.position == "LW")
            or (player.position == "RW")]

def select_strikers(players_list):
    return [player for player in players_list
            if (player.position == "ST")
            or (player.position == "LS")
            or (player.position == "RS")
            or (player.position == "CF")
            or (player.position == "RF")
            or (player.position == "LF")]

def sigmoid(s, beta):
    # activation function
    return 1 / (1 + numpy.exp(-s*beta))


def sigmoid_derivative(s, beta):
    #derivative of sigmoid
    return beta*s * (1 - s)


def generate_matrix(number_of_rows, number_of_columns):
    return numpy.random.random((number_of_rows, number_of_columns))


def convert_player_to_input_matrix(player):
            matrix = numpy.empty([1, 34])
            matrix[0][0] = player.crossing
            matrix[0][1] = player.finishing
            matrix[0][2] = player.heading_accuracy
            matrix[0][3] = player.short_passing
            matrix[0][4] = player.volleys
            matrix[0][5] = player.dribbling
            matrix[0][6] = player.curve
            matrix[0][7] = player.free_kick_accuracy
            matrix[0][8] = player.long_passing
            matrix[0][9] = player.ball_control
            matrix[0][10] = player.acceleration
            matrix[0][11] = player.sprint_speed
            matrix[0][12] = player.agility
            matrix[0][13] = player.reactions
            matrix[0][14] = player.balance
            matrix[0][15] = player.shot_power
            matrix[0][16] = player.jumping
            matrix[0][17] = player.stamina
            matrix[0][18] = player.strength
            matrix[0][19] = player.long_shots
            matrix[0][20] = player.aggression
            matrix[0][21] = player.interceptions
            matrix[0][22] = player.positioning
            matrix[0][23] = player.vision
            matrix[0][24] = player.penalties
            matrix[0][25] = player.composure
            matrix[0][26] = player.marking
            matrix[0][27] = player.standing_tackle
            matrix[0][28] = player.sliding_tackle
            matrix[0][29] = player.gk_diving
            matrix[0][30] = player.gk_handling
            matrix[0][31] = player.gk_kicking
            matrix[0][32] = player.gk_positioning
            matrix[0][33] = player.gk_reflexes
            return matrix


def convert_player_to_output_matrix(player):
    matrix = numpy.empty([1,1])
    matrix[0][0] = player.overall
    return matrix


def load_weights(path_to_file):
    return numpy.loadtxt(path_to_file)


def save_weights(path_to_file, matrix):
    numpy.savetxt(path_to_file, matrix, fmt="%s")


def load_thresholds(path_to_file):
    with open(path_to_file, 'r') as file:
        thresholds = file.read().split()
    return thresholds


def save_threshold(path_to_file, input_hidden_threshold, hidden_output_threshold):
    with open(path_to_file, 'w') as file:
        file.write("{} {}".format(float(input_hidden_threshold), float(hidden_output_threshold)))

