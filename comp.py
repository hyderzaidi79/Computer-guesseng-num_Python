def computer_guess():
    print("\n🤔Think of a number between 1 and 100, and I'll try to guess it!")
    input("👉Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("🤨Hmm... something went wrong. Did you give correct feedback?")
            break

        guess = (low + high) // 2
        attempts += 1

        print(f"\nMy guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'c':
            print(f"\n✨Yay! I guessed your number in {attempts} tries! 🎉")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please respond with 'H', 'L', or 'C'.")

computer_guess()
