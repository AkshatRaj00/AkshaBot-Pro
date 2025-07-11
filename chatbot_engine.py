def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! I am AkshaBot Pro. How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn’t get that."
