from urllib import request
import json
import pyttsx3

url = "https://official-joke-api.appspot.com/random_ten"
fazz = request.urlopen(url)
print(fazz.getcode())
data = fazz.read()
json_data = json.loads(data)
print(json_data)

class Jokes:
    def __init__(self,setup,punchline):
        self.setup = setup
        self.punchline = puchline
    def __str__(self):
        return f"joke {self.setup} punchline {self.punchline}"
jokes = []
for j in json_data:
    setup = j["setup"]
    puchline = j["punchline"]
    joke = Jokes(setup,puchline)
    jokes.append(joke)
print(len(jokes))
print(f"got {len(jokes)} jokes")
for joke in jokes:
    print(joke)
    pyttsx3.speak("joke")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("punchline")
    pyttsx3.speak(joke.punchline)