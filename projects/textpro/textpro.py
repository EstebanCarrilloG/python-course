def sentence_maker(phrase):
    """
    Converts a given phrase into a sentence by capitalizing the first letter 
    and appending a punctuation mark. If the phrase starts with a question word, 
    a question mark is added. Otherwise, a period is added.

    Args:
        phrase (str): The input phrase to be converted into a sentence.

    Returns:
        str: The formatted sentence with appropriate capitalization and punctuation.
    """
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
