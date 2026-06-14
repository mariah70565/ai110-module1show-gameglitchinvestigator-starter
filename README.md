# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
    - The game allows for a user to guess a secret number, providing hints after each guess that leads them closer to the solution. A user is able to replay as many times as desired, with a new secret number generated each time.
- [ ] Detail which bugs you found.
    - Hints were reversed, such that if a user guesses a number higher than the secret, the game would suggest to go higher, and similar if the guess is lower than the secret.
    - When clicking "new game", a user wouldn't be able input any new guesses, despite a new secret number being generated. The only way to play a new game would be by refreshing the page entirely.
- [ ] Explain what fixes you applied.
    - For the backward hints, I change the hint messages to suggest going lower when a guess is too high and going higher when a guess is too low. I also removed the every-other-game string casting on the secret number to avoid lexiographic comparisons. This allowed for proper numerical comparisions to determine which hint too return.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 70
2. Game returns "Too High, go LOWER"
3. Score goes down
4. User enters a guess of 50
5. Game returns "Too High, go LOWER"
6. Score goes down
7. User enters a guess of 45
8. Game returns "You won!" with final score
9. Game ends
**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
================================= 5 passed in 0.86s ==================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
