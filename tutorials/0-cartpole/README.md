Cartpole 
==============================

The classic cartpole benchmark. We use the gym env to make experiment around reinforcement learning, testing different agents or Network architecture.
 

SubProject Organization
------------

    ├── README.md          <- You are litteraly reading it.
    │
    ├── \_can_be_deleted   <- Trash bin (!! git ignored)
    |
    ├── models             <- Contains trained and serializzed models, and python files to generates those 
    │   ├── __init__.py    <- Makes models a Python module
    │   └── fully_connected.py <- To generated a 3 layers fully connected network
    │           
    ├── cartpole-requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── agents.py         <- Hold agent class definitions
    |
    └── cartpole.py       <- Main python file. 

## Environment set up

Everything you need can be installed with pip, from the cartpoel-requirement.txt file at tutorials/0-catpole 
```bash
pip install -r $PATH/cartpole-requirement.txt
```


<p><small>Project based on the <a target="_blank" href="http://git.equancy.io/tools/cookiecutter-data-science-project/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
