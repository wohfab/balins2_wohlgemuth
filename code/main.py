import spacy

nlp = spacy.load("en_core_web_sm")

text = ("A light in the room. It was you who was standing there. Tried, it was true As your glance met my stare. But your heart drifted off Like the land split by sea. I tried to go, to follow To kneel down at your feet")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])