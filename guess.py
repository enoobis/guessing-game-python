import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class HigherLowerGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.guess_count = 0

        # Generate a random number to be guessed
        self.secret_number = random.randint(1, 100)

        # Create widgets
        self.message = Label(text="Guess a number between 1 and 100:")
        self.input = TextInput(text="", multiline=False , halign='center')
        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.check_guess)

        # Add widgets to the layout
        self.add_widget(self.message)
        self.add_widget(self.input)
        self.add_widget(self.submit_button)

    def check_guess(self, instance):
        # Get the guess from the input field
        guess = int(self.input.text)

        # Increment the guess count
        self.guess_count += 1

        # Check if the guess is correct
        if guess == self.secret_number:
            self.message.text = "You guessed the correct number in {} guesses!".format(self.guess_count)
        elif guess > self.secret_number:
            self.message.text = "Your guess is too high. Try again."
        else:
            self.message.text = "Your guess is too low. Try again."

class HigherLowerApp(App):
    def build(self):
        return HigherLowerGame()

if __name__ == '__main__':
    HigherLowerApp().run()