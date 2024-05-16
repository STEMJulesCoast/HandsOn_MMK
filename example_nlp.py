import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser


# Download necessary resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Example text
text = "What is the weather in Hamburg today?"

# Tokenization
tokens = word_tokenize(text)

# Part-of-Speech Tagging
tagged = pos_tag(tokens)

print("Tokenized:", tokens)
print("POS-Tags:", tagged)


#Extract all parts of speech from text
chunker = RegexpParser("""
    NP: {<DT>?<JJ>*<NN.*>+}    # To capture noun phrases
    VP: {<VBZ> <NP>}          # Verb phrases that include a verb followed by a noun phrase
    PP: {<IN> <NP>}           # Prepositional phrases
""")





# Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)

# Draw the parse tree
output.draw()
