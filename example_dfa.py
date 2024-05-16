# example_dfa.py
class SentenceDFA:
    def __init__(self):
        self.current_state = 'START'
        self.accept_state = 'POSITIVE'
        self.positive_words = {"spaß", "laune", "bock", "fun"}  # positive words

    def transition(self, word):
        word = word.lower()  # lower case for better comparison
        if self.current_state == 'START' and word == "python":
            self.current_state = 'PYTHON'
        elif self.current_state == 'PYTHON' and word == "macht":
            self.current_state = 'MAKES'
        elif self.current_state == 'MAKES' and word in self.positive_words:
            self.current_state = self.accept_state

    def in_accept_state(self):
        return self.current_state == self.accept_state

# Example of usage
sentences = [
    "Python macht Spaß",
    "Python macht Laune",
    "Python macht Bock",
    "Python macht Fun",
    "Python ist doof"
]

for sentence in sentences:
    dfa = SentenceDFA()
    words = sentence.split()
    for word in words:
        dfa.transition(word)
    print(f"'{sentence}' -> {dfa.in_accept_state()}")