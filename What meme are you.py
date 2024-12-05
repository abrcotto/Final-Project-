import cv2  # Import OpenCV

# Defining meme traits and images
meme_traits = {
    "No Chick-fil-a sauce": "You're quick to judge .",
    "In the clurb we all fam": "You love to have fun with friends.",
    "Mamma a girl behind you": "You're supportive but",
    "What I do": "You're cool, collected, and don't care what anyone thinks."
}

# Pathway to my meme images
meme_images = {"No Chick-fil-a sauce": "no_chick_fila_sauce.jpg.jpg",
               "In the clurb we all fam": "in_the_clurb.jpg.jpg",
               "Mamma a girl behind you": "mamma_a_girl.jpg.jpg",
               "What I do": "what_i_do.jpg.jpg"}

# Define the questions and answer options
questions = [
    {
        "question": "What one word best describes you?",
        "choices": ["Confrontational", "Needy", "Annoying", "Rude"],
        "answers": {
            "Confrontational": "No Chick-fil-a sauce",
            "Needy": "In the clurb we all fam",
            "Annoying": "Mamma a girl behind you",
            "Rude": "What I do"
        }
    },
    {
        "question": "Are you a doom scoller?",
        "choices": ["Yasssss", "Naur", "I have a screen time", "What?"],
        "answers": {
            "Yasssss": "No Chick-fil-a sauce",
            "Naur": "In the clurb we all fam",
            "I have a screen time": "Mamma a girl behind you",
            "What?": "What I do"
        }
    },
    {
        "question": "What animal would you want?",
        "choices": ["Dog", "Cat", "Lizard", "Dragon"],
        "answers": {
            "Dog": "No Chick-fil-a sauce",
            "Cat": "In the clurb we all fam",
            "Lizard": "Mamma a girl behind you",
            "Dragon": "What I do"
        }
    },
    {
        "question": "What's most important to you?",
        "choices": ["Work", "Party with freinds", "Listen to music", "Shopping"],
        "answers": {
            "Work": "No Chick-fil-a sauce",
            "Party with freinds": "In the clurb we all fam",
            "Listen to music": "Mamma a girl behind you",
            "Shopping": "What I do"
        }
    },
    {
        "question": "What would you do if you saw money on the ground?",
        "choices": ["Give it back", "Share it", "Tell the police", "Thats a lil to broke for me"],
        "answers": {
            "Give it back": "No Chick-fil-a sauce",
            "Share it": "In the clurb we all fam",
            "Tell the police": "Mamma a girl behind you",
            "Thats a lil to broke for me": "What I do"
        }
    },
    {
        "question": "What celeb do you like the most?",
        "choices": ["Ryan Reynolds", "Jennifer Lawrence", "Tikashi 69", "Tupac"],
        "answers": {
            "Ryan Reynolds": "No Chick-fil-a sauce",
            "Tikashi 69": "In the clurb we all fam",
            "Jennifer Lawrence": "Mamma a girl behind you",
            "Tupac": "What I do"
        }
    },
    {
        "question": "What type of art do you like more?",
        "choices": ["Painting", "ceramics", "finger painting", "Art?"],
        "answers": {
            "Painting": "No Chick-fil-a sauce",
            "ceramics": "In the clurb we all fam",
            "finger painting": "Mamma a girl behind you",
            "Art?": "What I do"
        }
    }
]


def ask_questions():
    scores = {"No Chick-fil-a sauce": 0, "In the clurb we all fam": 0, "Mamma a girl behind you": 0, "What I do": 0}
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"], 1):
            print(f"{i}. {choice}")
        # Get user's input
        while True:
            try:
                answer_index = int(input("Choose your answer (1/2/3/4): ")) - 1
                if 0 <= answer_index < len(question["choices"]):
                    answer = question["choices"][answer_index]
                    meme_choice = question["answers"][answer]  # get the meme choice
                    scores[meme_choice] += 1  # add points to meme
                    break
                else:
                    print("Invalid choice, please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return scores


def determine_meme(scores):
    # Sort the memes based on score
    sorted_memes = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return sorted_memes[0][0]  # return the meme with the highest score


def show_meme_image(meme_name):
    # Load the meme image using OpenCV
    meme_image_path = meme_images[meme_name]
    meme_image = cv2.imread(meme_image_path)

    if meme_image is None:
        print("Error: Meme image not found.")
        return

    # Display the meme image in a window
    cv2.imshow(f"Your Meme: {meme_name}", meme_image)

    # Wait until any key is pressed
    cv2.waitKey(0)

    # Close the image window
    cv2.destroyAllWindows()


def main():
    print("What viral TikTok meme are you?")
    scores = ask_questions()
    meme = determine_meme(scores)
    input(f"You are this meme: {meme}! Press enter for more")
    input(f"Meme explanation: {meme_traits[meme]}Press enter for your imagae")

    # Show the meme image.
    show_meme_image(meme)

# Run the program


main()