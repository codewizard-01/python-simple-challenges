def generate_hashtag(s):
    # It splits the string into a list of words
    words_list = s.split(" ")
    # This loop capitalizes all the list's words
    for index, word in enumerate(words_list):
        capitalized_word = word.capitalize()
        words_list[index] = capitalized_word
    # This part joins the list's words into a single string
    my_hashtag ="".join(words_list)

    # Here, we check if the hashtag is longer than 140 characters and if it's empty
    if len(my_hashtag) >= 140 or my_hashtag == "":
        return "False"
    else:
        return f"#{my_hashtag}"


# Call the function and printing that in the console
print(generate_hashtag("my name is esmat"))