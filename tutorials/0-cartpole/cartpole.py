import gym
import time

import matplotlib.pyplot as plt
import numpy as np

from agent import DQNSolver

ENV_NAME = "CartPole-v1"

EPOCH = 1000

GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995
SCORE = [0 for _ in range(EPOCH)]


def cartpole():
    timer = time.time()
    env = gym.make(ENV_NAME)
    observation_space = env.observation_space.shape[0]
    action_space = env.action_space.n
    dqn_solver = DQNSolver(observation_space,
                           action_space,
                           learning_rate=LEARNING_RATE,
                           gamma=GAMMA,
                           exploration_max=EXPLORATION_MAX,
                           exploration_min=EXPLORATION_MIN,
                           exploration_dec=EXPLORATION_DECAY,
                           memory_size=MEMORY_SIZE,
                           batch_size=BATCH_SIZE)
    run = 0
    while run < EPOCH:
        run += 1
        state = env.reset()
        state = np.reshape(state, [1, observation_space])
        step = 0
        while True:
            step += 1
            env.render()
            action = dqn_solver.act(state)
            state_next, reward, terminal, info = env.step(action)
            reward = reward if not terminal else -reward  # si terminal c'est que l'on a échoué, on punit
            state_next = np.reshape(state_next, [1, observation_space])
            dqn_solver.add_to_memory(state, action, reward, state_next, terminal)
            state = state_next
            if terminal:
                print(
                    "Run: " + str(run) + ", exploration: " + str(dqn_solver.exploration_rate) + ", score: " + str(step))
                SCORE[run] = step
                break
            dqn_solver.fit()
    print('Executing time : %s' % (time.time() - timer))
    plt.figure(1)
    plt.plot([i for i in range(EPOCH)], SCORE)
    plt.show()


if __name__ == "__main__":
    cartpole()
