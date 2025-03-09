
from dataframes import df_turn_attributes


def generate_inverses(algs):

    inverse_algs = []

    for alg in algs:
        turns = alg.split()
        turns.reverse()  # reverse the order of the turns (one of the two necessary steps in generating an alg's inverse)


        inverse_turns = []
        for turn in turns:
               turn = df_turn_attributes.at[turn, "inverse"]
               inverse_turns.append(turn)


        inverse_alg = ' '.join(inverse_turns)    # turn the list back into a string
        inverse_algs.append(inverse_alg)


    return inverse_algs