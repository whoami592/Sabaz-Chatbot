import re

class ChatBot:
    def __init__(self):
        self.name = "whoamiBot"
        self.greetings = ["hi", "hello", "hey", "greetings", "salam"]
        self.farewells = ["bye", "goodbye", "see you", "take care"]
        self.questions = {
            r"how are you": "I'm just a program, but I'm here and ready to help!",
            r"what is your name": f"My name is {self.name}. I was created by Mr. Sabaz Ali Khan.",
            r"who created you": "I was created by Mr. Sabaz Ali Khan.",
            r"what can you do": "I can answer your questions, have simple conversations, and assist with basic tasks.",
            r"tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            r"thank you|thanks": "You're welcome! If you have more questions, feel free to ask."
        }

    def process_input(self, user_input):
        user_input = user_input.lower()
        
        # Check for greetings
        if any(greet in user_input for greet in self.greetings):
            return "Hello! How can I assist you today?"
        
        # Check for farewells
        if any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! Have a great day!"
        
        # Check for predefined questions
        for pattern, response in self.questions.items():
            if re.search(pattern, user_input):
                return response
        
        # Default response for unknown inputs
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

    def start_chat(self):
        print(f"Welcome! I am {self.name}, your personal AI assistant. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in self.farewells:
                print(f"{self.name}: Goodbye!")
                break
            response = self.process_input(user_input)
            print(f"{self.name}: {response}")


# Run the chatbot
if __name__ == "__main__":
    bot = ChatBot()
    bot.start_chat()