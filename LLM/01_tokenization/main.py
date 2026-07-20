import tiktoken

enc=tiktoken.encoding_for_model("gpt-4.1")
text="Hey there! My name is MS"
tokens=enc.encode(text)
print("Tokens",tokens)
#Decode (reverse it)
decoded=enc.decode([25216, 1354, 0, 3673, 1308, 382, 15861])
print("Decoded",decoded)
