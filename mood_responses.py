# mood_responses.py
def mood_response(mood):
    mood = mood.lower()
    if mood in ['happy', 'joyful', 'great', 'good']:
        return "That's wonderful to hear! Keep smiling!"
    elif mood in ['sad', 'down', 'depressed']:
        return "I'm sorry to hear that. I hope things get better soon."
    elif mood in ['angry', 'mad', 'frustrated']:
        return "Take a deep breath. It's okay to feel this way."
    elif mood in ['tired', 'exhausted', 'sleepy']:
        return "Make sure to get some rest. Your well-being is important."
    else:
        return "Thank you for sharing how you feel."
