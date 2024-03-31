import re
import long_responses as long  # Importing a module named long_responses

# Function to calculate the probability of a message matching recognized words
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

# Function to check all possible responses based on user input
def check_all_messages(message):
    highest_prob_list = {}

    # Function to add responses to a dictionary with their probabilities
    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Adding predefined responses with their associated words
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    # ... (existing code)

    # Adding additional predefined responses with their associated words
    # ... (existing code)

    # Custom longer responses
    response('Sure! Here\'s some advice: ' + long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response('I don\'t eat, but I can help you find great recipes!', ['what', 'you', 'eat'],
             required_words=['you', 'eat'])

    # ... (existing code)

    best_match = max(highest_prob_list, key=highest_prob_list.get)  # Finding the response with the highest probability
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match  # Returning the best response found


# Function to get response based on user input
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())  # Splitting user input into words
    response = check_all_messages(split_message)  # Getting response based on user input
    return response

# Main loop to continuously interact with the user
while True:
    print('Bot: ' + get_response(input('You: ')))  # Getting user input and printing bot's response
