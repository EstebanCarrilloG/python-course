def sentence_maker(phrase):
    questions = ("what", "when", "where", "who", "why", "how")
    if phrase.startswith(questions):
        return phrase.__add__("?").capitalize()
    else:
        return phrase.__add__(".").capitalize()
    
strings_array = []

while True:
    input_text = input("Say something: ")

    if input_text =="\end":
        break
    else:
        strings_array.append(sentence_maker(input_text))
        continue

print (" ".join(strings_array))
