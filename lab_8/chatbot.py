import datetime
import random


class Chatbot:
    """
    A class representing a chatbot.
    Methods:
        input_splitter: Splits the user's input into lowercase words.
        find_time: Finds the current system time and returns a greeting based on it.
        decide_happiness: Decides the happiness emotion value for the user's input.
        decide_fitness: Decides how easy the user found their exercise based on their input.
        questions: Decides on the response to give a user.
        parse_input: Makes conclusions based on the user's input.
    Attributes:
        self.amount_messages: The amount of messages the user has sent
        self.split_input: The user's input split into words.
        self.greetings: A tuple of greetings which the chatbot can use.
        self.compliments: A tuple of compliments the chatbot can give.
        self.encouragement: A tuple of encouraging things the chatbot can say.
        self.exercises: A tuple of different activities the user can engage in to exercise.
        self.username: The user's name.
        self.happiness: The user's happiness emotion value for their message.
        self.fitness: How easy the user found their exercise based on their previous message.
    """

    def __init__(self):
        """Constructor used to create a Chatbot object"""
        self.amount_messages = 0
        self.split_input = []
        self.greetings = ("Hello", "Hi", f"Good {self.find_time()}")
        self.compliments = ("Great job", "Well done", "Fantastic", "Good work", "Amazing job")
        self.encouragement = ("You can do it", "Keep going", "Nearly there", "Don't give up")
        self.exercises = ("Football", "Basketball", "Tennis", "Rugby", "Gynmastics", "Sprinting", "Cross-country",
                          "Jogging", "Cycling")
        self.username = ""
        self.happiness = 0
        self.fitness = 0

    def input_splitter(self, input_str):
        """Splits the user's input into lowercase words."""
        self.split_input = input_str.lower().split()

    def find_time(self):
        """Finds the current system time and returns a greeting based on it."""
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return "morning"
        elif current_hour < 18:
            return "afternoon"
        else:
            return "evening"

    def decide_happiness(self):
        """
        Decides the happiness emotion value for the user's input, based on the number of words in the input string
        indicating happiness and unhappiness.
        """

        self.happiness = 0.0
        for i in self.split_input:
            if i in ("sad", "annoyed", "angry", "frustrated", "glum", "forlorn", "downcast", "cross", "irritated",
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
        """
        Decides the fitness value for the user's input, based on the number of words in the input string indicating
        fitness and unfitness.
        """

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
        """
        Decides on the response to give to a user, based on if the user has given any input, given their name, and how
        happy they are and how difficult they are finding their exercise.
        """
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
        """
        Makes conclusions about the user's happiness and how easy their exercise is based on the user's input.
        Records number of messages and changes the user's amount of messages. Checks for any extra information returned
        with the chatbot's response string.
        """
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
