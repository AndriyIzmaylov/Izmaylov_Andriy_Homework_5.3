# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes


import string


def hashtag_converter(input_string):
    cleaned_string = input_string.translate(str.maketrans('', '', string.punctuation)).split()

    capitalized_words = [word.capitalize() for word in cleaned_string]

    hashtag_string = "#" + "".join(capitalized_words)

    if len(hashtag_string) > 140:
        hashtag_string = hashtag_string[:140]

    return hashtag_string


examples_strings = [
    "Python Community",
    "i like python community!",
    "Should, I. subscribe? Yes!"
]

print("******************** EXAMPLE STRINGS ********************")
for example_string in examples_strings:
    print(f"'{example_string}' -> '{hashtag_converter(example_string)}'")

user_input = input("Enter the text to convert to hashtag: ").strip()

print(f"Converted hashtag: {hashtag_converter(user_input)}")
