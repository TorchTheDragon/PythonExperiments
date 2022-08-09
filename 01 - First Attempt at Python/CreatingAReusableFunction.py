# Creating a Reusable Function
message = input("> ")

def emoji_converter(message):
    output = ""
    words = message.split(' ')
    emojis = {
        ":)" : "😀",
        ":(" : "😞"
    }
    for word in words:
        output += emojis.get(word, word) + " "
    return output


result = emoji_converter(message)
print(result)
# I hath just learned it is better to have two lines seperating code from a function