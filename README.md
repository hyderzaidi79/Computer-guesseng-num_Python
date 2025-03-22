📈 Computer Guessing Game
📝 Description

This is a simple Python console game where the computer tries to guess a number you are thinking of between 1 and 100. Using a binary search algorithm, the computer will narrow down the range based on your feedback and guess your number efficiently!

🎮 How to Play

    Think of a number between 1 and 100 (inclusive), but don't tell the computer.

    Run the program and press Enter when you're ready.

    The computer will make a guess.

    After each guess, provide feedback:

        Enter H if the guess is too High.

        Enter L if the guess is too Low.

        Enter C if the guess is Correct.

    The computer will continue guessing until it gets it right!

    🧠 How It Works

    The computer starts with a range of 1 to 100.

    It will always guess the midpoint of the current range.

    Based on your feedback (H, L, or C), it will adjust the range:

        If the guess is too high, the upper limit decreases.

        If the guess is too low, the lower limit increases.

        If correct, the game ends and shows how many tries it took.



🚀 How to Run

    Ensure you have Python installed (version 3.x recommended).

    Save the code in a file named, for example, computer_guess.py.

    Open your terminal or command prompt.

    Navigate to the directory where the file is saved.

    Run the program using:


    🛠 Features

    Interactive console game.

    Simple implementation of a binary search algorithm.

    Input validation for feedback.

    Fun and playful output (including emojis 🎉).


    📌 Notes

    The game assumes honest input from the user.

    If conflicting feedback is provided, the game will notify you that something went wrong.



    💡 Future Improvements

    Add error handling for non-alphabetic inputs.

    Allow customization of the number range (e.g., 1 to 1000).

    Add a GUI version using libraries like Tkinter or PyQt.




Enjoy the game! 😄
