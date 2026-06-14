import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess
from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).resolve().parents[1] / "app.py"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📈 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"

def test_new_game_button():
    """Test the functionality of the New Game button."""
    at = AppTest.from_file(str(APP_PATH))
    at.run(timeout=10)
    at.selectbox[0].select("Normal")  # Set the difficulty selectbox
    at.run(timeout=10)

    at.session_state["secret"] = 999
    at.session_state["attempts"] = 3
    at.session_state["score"] = 50
    at.session_state["history"] = [10, 20, 30]
    at.session_state["status"] = "won"

    at.button[1].click().run()  # New Game 🔁

    assert at.session_state["attempts"] == 0
    assert at.session_state["score"] == 0
    assert at.session_state["history"] == []
    assert at.session_state["status"] == "playing"
    assert 1 <= at.session_state["secret"] <= 100
    assert at.session_state["secret"] != 999

def test_higher_lower_hints():
    """Test the hints for higher/lower guesses."""
    from streamlit import session_state

    session_state.secret = 50

    # Test a guess that is too low
    guess_low = 30
    outcome, message = check_guess(guess_low, session_state.secret)
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"

    # Test a guess that is too high
    guess_high = 70
    outcome, message = check_guess(guess_high, session_state.secret)
    assert outcome == "Too High"
    assert message == "📈 Go LOWER!"
