#General responses
def get_response(user_input: str) -> str:
    user_input = user_input.lower()

    if user_input == '':
        return 'You\'re awfully silent'
    
    elif user_input.startswith('hello'):
        return 'Hello there!'
    
    elif user_input.startswith('bye'):
        return 'See you next time!'
    
    else:
        return 'I didn\'t understand what you try to tell me'