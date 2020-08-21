Celeste TAS by reinforcement learning
==============================

DISCLAIMER: This work is in progress. We have a lot to do/ to learn, and we are only at the beginning. 

This project aims to create an AI capable of creating a *tool-assisted speedrun* of the plateform game [Celeste](http://www.celestegame.com/). 

Few definitions :

A *speedrun* is an instance of completing a video game, or level of a game, as fast as possible. 

A tool-assisted speedrun or tool-assisted superplay (TAS) is generally defined as speedrunning a game in an emulator with the goal of creating a theoretically perfect playthrough. As the name implies, a TAS is not performed by an actual human being, but rather by a program or a piece of software that delivers frame-perfect optimized controller input to complete the game in the fastest way possible

Here, our main goal is to design a algorithm which play the game, and learn how to finish it as fast as possible, with reinforcement learning.


 

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README.
    │
    ├── \_can_be_deleted   <- Trash bin (!! git ignored)
    |
    ├── models             <- Trained and serialized models.
    │                         
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                        the creator's initials, and a short `-` delimited description.        
    |    
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting 
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to manage data
    │   │   └── make_dataset.py
    │   │
    │   ├── game_input     <- Script to send input to the game from the output of the model
    │   │
    │   ├── game_output    <- Script to extract the features to the game, to send it to the python model
    │   │
    │   ├── models         <- Definitions of model classes used in the notebooks 
    │   │
    │   └── visualization <- Script for visualization, graph, animation...
    │       
    └── tutorials         <- Simpler use-cases of reinforcement learning, to learn/pratice our ideas
       ├──0-cartpole                              
       └──1-atari_games


