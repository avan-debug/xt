import time
import tensorflow as tf
import numpy as np
import pandas as pd

N_STATE = 6
ACTIONS = ["left", "right"]
GREEDY_POLICY = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13
FRESH_TIME = 0.3


def build_q_table(n_state, actions):
    q_table = pd.DataFrame(np.zeros((n_state, len(actions))), columns=actions)
    return q_table


def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > GREEDY_POLICY) or (state_actions.all() == 0):
        return np.random.choice(ACTIONS)
    else:
        return state_actions.idxmax()


def get_env_feedback(S, A):
    if A == "right":
        if S == N_STATE - 2:
            S_ = "terminal"
            R = 1
        else:
            S = S + 1
            R = 0
    elif A == "left":
        if S == 0:
            S_ = S
            R = 0
        else:
            S = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    env_list = "-"*(N_STATE - 1) + "T"
    if S == "terminal":
        interaction = "Episode: %s: total_step = %s" % (episode + 1, step_counter)
        print("\r{}".format(interaction))
        time.sleep(2)
        print("\r                     ", end='')
    else:
        env_list[S] = "o"
        interaction = "".join(env_list)
        print("\r{}".format(interaction), end="")
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATE, ACTIONS)
    for episode in range(MAX_EPISODES):
        S = 0
        step_counter = 0
        is_terminal = False
        update_env(S, episode, step_counter)
        while is_terminal:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.ix[S, A]


if __name__ == '__main__':
    tf.config.experimental.list_physical_devices("GPU")
