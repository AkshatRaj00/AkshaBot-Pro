def get_response(msg):
    msg = msg.lower()
    if "hello" in msg:
        return "Hi there!"
    elif "bye" in msg:
        return "Goodbye!"
    else:
        return "I didn’t understand that."
