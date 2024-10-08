import streamlit as st
import random


st.title('Number Guessing Game')
st.write('Are you a genius? Try guessing my number. Don\'t worry, I\'ll give you some hints')

# Function to initialize or reset the game
def start_game():
    st.session_state.my_num = random.randint(1, 15)
    st.session_state.game_active = True

# Initialize 'my_num' and 'game_active' if they are not in session_state
if 'my_num' not in st.session_state:
    start_game()
if 'game_active' not in st.session_state:
    st.session_state.game_active = True

def main():
    st.write('I have guessed a number between 1 and 15. Can you guess my number?')

    # If the game is active, allow the user to guess
    if st.session_state.game_active:
        # Keep track of the user's guess
        guess_no = st.number_input("Enter your number here", key="guess_number", min_value=1, max_value=15)

        action_button = st.button("Submit Guess")
        if action_button:
            # Provide feedback based on the user's guess
            if guess_no == st.session_state.my_num:
                st.success(f"You're a Genius!!! You read my mind. I chose {st.session_state.my_num} and you guessed {guess_no}.")
                st.session_state.game_active = False  # End the game after correct guess
            elif guess_no < st.session_state.my_num:
                st.warning(f"Oops!!! You guessed wrong. You guessed {guess_no}. Keep Trying. Here's a hint: My number is greater than yours.")
            else:
                st.warning(f"Oops!!! You guessed wrong. You guessed {guess_no}. Keep Trying. Here's a hint: My number is lesser than yours.")
    else:
        st.write("You've already guessed the number correctly! Click 'Restart Game' to play again.")

    # Restart game button
    if st.button("Restart Game"):
        start_game()

if __name__ == "__main__":
    main()