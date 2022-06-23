def emoji_convert(message):
    words = message.split(" ")
    emoji = {
        ":)" : "😃",
        ":(" : "😞"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input('>')
print(emoji_convert(message))