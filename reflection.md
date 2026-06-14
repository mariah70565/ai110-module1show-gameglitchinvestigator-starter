# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    - The game loaded properly on initial visit, but the feedback did not accurately correlate with my guesses. The hints were guiding me further away from the guess, telling me to go higher when my guess is already too high, for instance. Additionally, the guess counter was not updating correctly after each round.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The hints were suggesting incorrect directions. If a guess is too high, it suggests to go higher, and if a guess is too low, it suggests to go lower. I also noticed that when you click "new game", i wasn't able to actually play a new game, even though a new secret was being generated. I was unable to re-guess unless the page was refreshed.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 50 | Game should provide a hint if guess is incorrect | I'm provided a hint of the opposite direction I need to go in | "Too Low" when it should be "Too High" or "Too High" when it should be "Too Low" |
| Click "New Game" button | A new secret number should be chosen and I should be able to start guessing | A new secret number is generated, but I am unable to guess | none |
| Guess of 50 | Game should go from 7 attempts to 6 | The number of attempts still reads as 7 | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    - VSCode Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - The AI recognized that when a guess was too low, it displayed "go lower" instead of "go higher" and when a guess was too high, it displayed "go higher" instead of "go lower". It correctly fixed it such that when a guess is too low, it displays "go higher" and when a guess is too high, it displays "go lower"
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    - The AI also realized that the reason for backward hints was due to the secret being casted as a string for every other attempt, meaning we were comparing lexiographically instead of numerically. It suggested that in check_guess, I recast the secret as an int if the type is a string. While this worked, it seemed unnecessary. Instead, I chose to remove the string casting, regardless of what attempt the user is on.  This simplified the code, while leading to correct hints. To verify the result, I purposely guessed values too low or too high to confirm what the hint should be.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    - Before fixing the bug, I first played the game with different test cases to understand how the behavior should change, such as guessing exactly the number, guessing too high, or guessing too low. Once I implemented the fix, I retested using the same test cases to monitor the behavior change. I also asked AI to generate a test file to verify.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One of my pytest cases looks for a correct result and hint when a guess is higher than the secret number. Originally, the hints were backwards and if a number was too high, it would suggest to go higher, leading a user further away from the solution. This test ensures my fix now leads the user closer to the solution and guides them in the right direction. 
- Did AI help you design or understand any tests? How?
    - Yes, after realizing the hints were backwards, I asked CoPilot to help me further understand why that was the case. At first I thought it was only due to the messages being inversed (when a guess was too high, the code would print "Go HIGHER") but it also pointed out that every other game was comparing the guess and secret lexiographically instead of numerically. The code was wrongly casting the secret as a string, leading to faulty numerical comparisons.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
