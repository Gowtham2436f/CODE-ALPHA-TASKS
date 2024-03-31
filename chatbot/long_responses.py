import random
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

R_EATING = "I dont like eating anything because i'm a bot obviously!"
def unknown():
    response = ['could you please re-phrase that?'
                "...",
                "sounds about right",
                "what does that mean?"][random.randrange(4)]
    return response


