from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_string_secret_returns_correct_hint():
    # Target the 'string conversion' bug on alternate attempts
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"

def test_update_score_decreases_on_incorrect_guess():
    # Target the 'Too High' incorrect score logic on even attempt numbers
    new_score_1 = update_score(10, "Too High", attempt_number=1)
    new_score_2 = update_score(10, "Too High", attempt_number=2)
    assert new_score_1 == 5
    assert new_score_2 == 5
