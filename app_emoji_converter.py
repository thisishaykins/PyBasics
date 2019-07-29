
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔",
        ":P": "😋",
        ":D": "😀",
        ":O": "𒃽",
        ";)": "😉",
        "B-)": "🤓",
        "B|": "😎",
        ">:(": "😡",
        ":'(": "😢",
        "3:)": "👹",
        "O:)": "👼",
        ":*": "💋",
        ":***": "😘",
        "<3": "💓",
        "o.O": "😕",
        ">:O": "😠"
    }
    # print(words)

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output


message = input("> ")
result = emoji_converter(message)
print(result)


