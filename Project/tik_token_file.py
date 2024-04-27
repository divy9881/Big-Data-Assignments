import tiktoken
import sys

# load an encoding by name
encoding = tiktoken.get_encoding("cl100k_base")

sentence = ""
with open(sys.argv[1], 'r') as file:
    sentence = file.read()


# to convert string into a list of token integers.
token_list = encoding.encode(sentence)

# print(token_list)
# print(len(token_list))

# For single tokens, .decode_single_token_bytes() safely converts a single integer token to the bytes it represents.
# To see how tokens are generated.
#tokens = [encoding.decode_single_token_bytes(token) for token in token_list]

# file_path = "tt_tokens.txt"
# with open(file_path, 'w') as file:
#     for item in tokens:
#         file.write(str(item) + '\n')

# print(tokens)