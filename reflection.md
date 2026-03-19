# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game loaded successfully with the UI intact, but as soon as I started playing and submitting guesses, I noticed several issues with the game logic and score tracking. The user interface was responsive but the background logic was glitching.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Incorrect Hints (String comparison bug): Sometimes the hints were completely wrong (e.g. telling me to go higher when my guess was already higher than the secret). This happened because the secret was being converted to a string on even-numbered attempts.
  2. Score Increasing on Wrong Guesses: When receiving a "Too High" hint on an even attempt number, the score actually increased by 5 points instead of decreasing.
  3. Starting Attempts Display: The game showed 1 attempt mathematically used up before I even made my first guess, because the session state for attempts started at 1 instead of 0.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Copilot (via Agent Mode and Inline Chat).
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The Agent suggested refactoring `update_score` to subtract 5 unconditionally when the outcome is "Too High", instead of the parity-check code that added points on even attempts. I verified the result by playing the game and watching my score go down instead of up when guessing too high.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI suggested using `assert check_guess(...) == "Win"` in the pytest case without realizing that `check_guess` actually returns a tuple `("Win", "🎉 Correct!")`. The test failed due to the tuple mismatch, which I verified by inspecting the actual return values of the logic functions.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I determined a bug was fixed by verifying it no longer occurred in my manual tests via the Streamlit interface and running a pytest case targeting the exact logic flaw.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest targeting the "Too High" score deduction. `test_update_score_decreases_on_incorrect_guess` passed inputs for attempt numbers 1 and 2, which proved the score correctly deducted 5 points regardless of the parity. 
- Did AI help you design or understand any tests? How?
  Yes, the AI generated a test case that bypassed the Streamlit frontend and tested `check_guess` by feeding it a string for the secret on purpose, which perfectly simulated the parity string bug that was breaking the game.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit runs the entire python script from top to bottom every time a user interacts with the app (like clicking a button). Session state is like a hidden memory box that holds variables (like the secret number) across these reruns so they don't get reset every time the page refreshes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  I want to reuse the strategy of marking the "crime scene" with a `# FIXME` comment before addressing bugs. It keeps me focused on isolated parts of the codebase.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would double-check the AI's generated tests against the actual function signatures. Sometimes AI generates tests that look correct but fail because of incorrect assumptions about return types (like the tuple).
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I realize now that AI generated code can be flawed and buggy, often hiding fundamental logic errors under a shiny interface. It reinforced my belief that understanding the underlying logic is essential, even when using powerful code generation tools.
