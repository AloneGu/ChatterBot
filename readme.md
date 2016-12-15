# ChatterBot

ChatterBot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatterBot allows it
to be trained to speak any language.


An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:** Do you like hats?  


## Basic Usage

check examples

# Training data

Chatterbot comes with a data utility module that can be used to train chat bots.
At the moment there is three languages, English, Spanish and Portuguese training data in this module. Contributions
of additional training data or training data in other languages would be greatly
appreciated. Take a look at the data files in the
[chatterbot/corpus](https://github.com/gunthercox/ChatterBot/tree/master/chatterbot/corpus)
directory if you are interested in contributing.

```
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")
```

# flask-chatterbot

#### A web implementation of [ChatterBot](https://github.com/gunthercox/ChatterBot) using Flask.

## Local Setup:
 1. Ensure that Python, Flask, and ChatterBot are installed.
 2. Run *app.py* ( in backend: nohup python app.py & )
 3. Base URL will be [http://localhost:5000/](http://localhost:5000/)
 4. try chat in terminal? python interact_run.py

## Usage example:
*   [/get/how are you?](http://localhost:5000/get/how are you?)
  *   Browser handles whitespace for you ([/get/how%20are%20you?](http://localhost:5000))
  *   Returns raw response (ex: I am good).

# all install under ubuntu
```
pip install -r requirements
sudo python setup.py install
```