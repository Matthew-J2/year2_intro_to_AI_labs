import datetime
import random


class Chatbot:
    def __init__(self):
        self.amount_messages = 0
        self.split_input = []
        self.greetings = ("Hello", "Hi", f"Good {self.findtime()}")
        self.compliments = ("Great job", "Well done", "Fantastic", "Good work", "Amazing job")
        self.encouragement = ("You can do it", "Keep going", "Nearly there", "Don't give up")
        self.exercises = ("Football", "Basketball", "Tennis", "Rugby", "Gynmastics", "Sprinting", "Cross-country",
                          "Jogging", "Cycling")
        self.username = ""
        self.happiness = 0
        self.fitness = 0
        self.fitness_level = self.decide_fitness

    def input_splitter(self, input_str):
        self.split_input = input_str.lower().split()

    def findtime(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return "morning"
        elif current_hour < 18:
            return "afternoon"
        else:
            return "evening"

    def decide_happiness(self):
        self.happiness = 0.0
        for i in self.split_input:
            if i in ("sad", "annoyed", "angry", "frustrated", "glum", "forlorn", "downcase", "cross", "irritated",
                     "bad"):
                self.happiness -= 1.0
            elif i in ("furious", "hate", "livid", "miserable", "depressed"):
                self.happiness -= 2.0
            elif i in ("happy", "calm", "relaxed", "content", "glad", "good", "jolly", "cheerful"):
                self.happiness += 1.0
            elif i in ("joyful", "gleeful", "joyous", "delighted", "chuffed"):
                self.happiness += 2.0
        self.happiness = self.happiness / len(self.split_input)

    def decide_fitness(self):
        self.fitness = 0.0
        for i in self.split_input:
            if i in ("hard", "difficult", "tired", "fatigued", "sleepy", "tiring"):
                self.fitness -= 1.0
            elif i in ("demanding", "strenuous", "impossible", "knackered", "exhausted", "gruelling"):
                self.fitness -= 2.0
            elif i in ("easy", "lively", "awake", "fresh", "athletic", "quick", "strong"):
                self.fitness += 1.0
            elif i in ("healthy", "vigorous", "effortless", "painless"):
                self.fitness += 2.0
        self.fitness = self.fitness / len(self.split_input)

    def questions(self):
        if self.amount_messages == 0:
            random_greeting = random.randrange(len(self.greetings))
            return (f"{self.greetings[random_greeting]}.", "")
        elif not self.username:
            return ("I'm your personal trainer, Tom. It's nice to meet you, what's your name?", "name_ask")
        elif abs(self.happiness) >= abs(self.fitness):
            if self.happiness < -0.5:
                return(f"I'm really sorry to hear that {self.username}. Anything I can do to help?", "")
            elif self.happiness < 0.0:
                return(f"Sorry about that {self.username}. Anything I can do to help?", "")
            elif self.happiness < 0.5:
                return(f"That's good to hear {self.username}. Anything I can do to help?", "")
            else:
                return(f"That's great to hear {self.username}! Anything I can do to help?", "")

        elif abs(self.happiness) < abs(self.fitness):
            random_exercise = random.randrange(len(self.exercises))
            random_compliment = random.randrange(len(self.compliments))
            random_encouragement = random.randrange(len(self.encouragement))
            if self.fitness < -0.5:
                return(f"I'm really sorry to hear that {self.username}, {self.encouragement[random_encouragement].lower()}. "
                       f"You could try resting for a few days, then you could try "
                       f"{self.exercises[random_exercise].lower()}.", "")
            elif self.fitness < 0.0:
                return(f"Sorry about that {self.username}, {self.encouragement[random_encouragement].lower()}. "
                       f"Maybe try something different like {self.exercises[random_exercise].lower()}.", "")
            elif self.fitness < 0.5:
                return(f"That's good to hear {self.username}. {self.compliments[random_compliment]}. You could carry "
                       f"on as you are, or try something different like {self.exercises[random_exercise].lower()}.", "")
            else:
                return(f"That's great to hear {self.username}. {self.compliments[random_compliment]}! If the exercise "
                       f"is too easy, maybe try something different like {self.exercises[random_exercise].lower()}", "")

    def parse_input(self, response, question_info):
        self.input_splitter(response)
        self.amount_messages += 1
        self.decide_happiness()
        self.decide_fitness()
        if question_info == "name_ask":
            self.username = response.title()



def main():
    chatbot = Chatbot()
    while True:
        question = chatbot.questions()
        print(question[0])
        response = input()
        chatbot.parse_input(response, question[1])


if __name__ == "__main__":
    main()
