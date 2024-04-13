import tiktoken
import sys

# load an encoding by name
encoding = tiktoken.get_encoding("cl100k_base")

# to convert string into a list of token integers.
token_list = encoding.encode(sys.argv[1])

print(token_list)

# For single tokens, .decode_single_token_bytes() safely converts a single integer token to the bytes it represents.
tokens = [encoding.decode_single_token_bytes(token) for token in token_list]

print(tokens)