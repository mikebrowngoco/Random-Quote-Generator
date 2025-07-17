import random

quotes = [
    "Believe you can and you're halfway there.",
    "Do not wait to strike till the iron is hot; but make it hot by striking.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Keep your face always toward the sunshine—and shadows will fall behind you."
]

def show_random_quote():
    print("\n🌟 Here's your quote:\n")
    print(random.choice(quotes))

if __name__ == "__main__":
    show_random_quote()
