import random

import numpy as np

from models.fully_connected import generate_fully_connected_net
from keras.optimizers import Adam
from collections import deque


class DQNSolver:

    def __init__(self, observation_space, action_space, learning_rate, gamma, exploration_max, exploration_min,
                 exploration_dec, memory_size, batch_size):
        self.exploration_min = exploration_min
        self.exploration_dec = exploration_dec
        self.gamma = gamma
        self.batch_size = batch_size
        self.exploration_rate = exploration_max

        self.action_space = action_space
        self.memory = deque(maxlen=memory_size)

        self.model = generate_fully_connected_net(action_space, observation_space)
        self.model.compile(loss="mse", optimizer=Adam(
            lr=learning_rate))  # utiliser la mse permet de calculer l'erreur quadratique moyenne entre le premier et le second argument

    def add_to_memory(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:  # avec une proba epsilon, on choisit de ne pas utiliser le reseau mais de faire une action au pif, pour explorer
            return np.random.randint(self.action_space)
        else:
            q_values = self.model.predict(state)
            return np.argmax(q_values[0])

    def fit(self):
        if len(self.memory) < self.batch_size:
            return
        batch = random.sample(self.memory, self.batch_size)
        for state, action, reward, state_next, terminal in batch:
            if not terminal:
                q_update = (reward + self.gamma * np.amax(self.model.predict(state_next)[0]))
            else:
                q_update = reward
            q_values = self.model.predict(state)
            q_values[0][action] = q_update
            self.model.fit(state, q_values, epochs=1, verbose=0)
        self.exploration_rate = max(self.exploration_dec * self.exploration_rate,
                                    self.exploration_min)  # on diminue la proba d'explorer au fur et a mesure de l'entrainement


class DDQNSolver:

    def __init__(self, observation_space, action_space, learning_rate, gamma, exploration_max, exploration_min,
                 exploration_dec, memory_size, batch_size):
        self.exploration_min = exploration_min
        self.exploration_dec = exploration_dec
        self.gamma = gamma
        self.batch_size = batch_size
        self.exploration_rate = exploration_max

        self.action_space = action_space
        self.memory = deque(maxlen=memory_size)

        self.model = generate_fully_connected_net(action_space, observation_space)
        self.model.compile(loss="mse", optimizer=Adam(
            lr=learning_rate))  # utiliser la mse permet de calculer l'erreur quadratique moyenne entre le premier et le second argument
        self.target = generate_fully_connected_net(action_space, observation_space)
        self.target.compile(loss="mse", optimizer=Adam(
            lr=learning_rate))
        self.update_target_model()

    def update_target_model(self):
        self.target.set_weights(self.model.get_weights())
        return self.target

    def add_to_memory(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:  # avec une proba epsilon, on choisit de ne pas utiliser le reseau mais de faire une action au pif, pour explorer
            return np.random.randint(self.action_space)
        else:
            q_values = self.model.predict(state)
            return np.argmax(q_values[0])

    def fit(self):
        if len(self.memory) < self.batch_size:
            return
        batch = random.sample(self.memory, self.batch_size)
        for state, action, reward, state_next, terminal in batch:
            if not terminal:
                q_update = (reward + self.gamma * np.amax(self.model.predict(state_next)[0]))
            else:
                q_update = reward
            q_values = self.model.predict(state)
            q_values[0][action] = q_update
            self.model.fit(state, q_values, epochs=1, verbose=0)
        self.exploration_rate = max(self.exploration_dec * self.exploration_rate,
                                    self.exploration_min)  # on diminue la proba d'explorer au fur et a mesure de l'entrainement
