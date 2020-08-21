from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


def generate_fully_connected_net(action_space, observation_space):
    """.
     Standard fully connected 3 layers net

    Arguments:
    shape: image shape, in the format (nb_channels, x_size, y_size).


    Returns:
    DNN model - it still needs to be compiled.

    """
    model = Sequential()
    model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
    model.add(Dense(24, activation="relu"))
    model.add(Dense(action_space, activation="linear"))
    return model
