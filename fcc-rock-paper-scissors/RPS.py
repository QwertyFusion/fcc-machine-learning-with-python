# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random


my_history = []
init_play = prev_play = 'S' # Assuming we are always starting with Scissor (S)
current_opponent = [False, False, False, False] # Quincy, Abbey, Krish, Mrugesh
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
opponent_quincy_counter = -1
play_order = [{
    "RR" : 0, 
    "RP" : 0, 
    "RS" : 0, 
    "PR" : 0, 
    "PP" : 0, 
    "PS" : 0, 
    "SR" : 0, 
    "SP" : 0, 
    "SS" : 0, 
}]

def player(prev_opponent_play, opponent_history = []):
    """
    Plays Rock-Paper-Scissors based on opponent bot's previous plays.

    Args:
        prev_opponent_play: The opponent's previous play ('R', 'P', or 'S').
        opponent_history: A list of the opponent's previous plays.

    Returns:
        The player's next play ('R', 'P', or 'S').
    """
    # Declaring Global Variables
    global my_history, prev_play, current_opponent, opponent_quincy_counter, play_order

    # Updating game history
    opponent_history.append(prev_opponent_play)
    my_history.append(prev_play)

    
    # Check if no oponents are active
    if not(any(current_opponent)):
      ## Quincy
      if (opponent_history[-5:] == ['R', 'P', 'P', 'S', 'R']):
        current_opponent[0] = True

      ## Abbey
      elif (opponent_history[-5:] == ['P', 'P', 'R', 'R', 'R']):
        current_opponent[1] = True

      ## Kris
      elif (opponent_history[-5:] == ['P', 'R', 'R', 'R', 'R']):
        current_opponent[2] = True

      ## Mrugesh
      elif (opponent_history[-5:] == ['R', 'R', 'R', 'R', 'R']):
        current_opponent[3] = True

    # Opponent Counter Moves
    ## Quincy Counter Move
    if current_opponent[0]: 
        if len(opponent_history) % 1000 == 0:
            current_opponent = [False, False, False, False]
            opponent_history.clear()

        opponent_quincy_list = ['R', 'P', 'P', 'S', 'R']
        opponent_quincy_counter = (opponent_quincy_counter + 1) % 5
        return ideal_response[opponent_quincy_list[opponent_quincy_counter]]
    
    ## Abbey Counter Move
    elif current_opponent[1]: 
        last_two = ''.join(my_history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1
        potential_plays = [
            prev_play + 'R', 
            prev_play + 'P', 
            prev_play + 'S', 
        ]
        sub_order = {
            k : play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }
        prediction = max(sub_order, key = sub_order.get)[-1:]

        # Adding Randomness to break Abbey's prediction
        if random.random() < 0.25:  # 25% chance to break the pattern
            prev_play = random.choice(['R', 'P', 'S'])  # Make a random move to disrupt Abbey's prediction
        else:
            prev_play = ideal_response[ideal_response[prediction]]

        if len(opponent_history) % 1000 == 0:
            current_opponent = [False, False, False, False]
            opponent_history.clear()
            play_order = [{
                "RR" : 0, 
                "RP" : 0, 
                "RS" : 0, 
                "PR" : 0, 
                "PP" : 0, 
                "PS" : 0, 
                "SR" : 0, 
                "SP" : 0, 
                "SS" : 0, 
            }]

        return prev_play
    
    ## Kris Counter Move
    elif current_opponent[2]: 
        if len(opponent_history) % 1000 == 0:
            current_opponent = [False, False, False, False]
            opponent_history.clear()

        prev_play = ideal_response[ideal_response[prev_play]]
        return prev_play

    ## Mrugesh Counter Move
    elif current_opponent[3]: 
        if len(opponent_history) == 1000:
            current_opponent = [False, False, False, False]
            opponent_history.clear()

        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key = last_ten.count)
        prev_play = ideal_response[ideal_response[most_frequent]]
        return prev_play

    # Returning our move
    prev_play = init_play
    return prev_play