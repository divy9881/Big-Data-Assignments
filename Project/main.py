import tiktoken

# load an encoding by name
encoding = tiktoken.get_encoding("cl100k_base")
encoding_1 = tiktoken.get_encoding("p50k_base")
encoding_2 = tiktoken.get_encoding("r50k_base")

# to convert string into a list of token integers.
token_list = encoding.encode("tiktoken is not so great!")
token_list_1 = encoding_1.encode("tiktoken is not so great!")
token_list_2 = encoding_2.encode("tiktoken is not so great!")

print(token_list, token_list_1, token_list_2)

# For single tokens, .decode_single_token_bytes() safely converts a single integer token to the bytes it represents.
tokens = [encoding.decode_single_token_bytes(token) for token in token_list]
tokens_1 = [encoding_1.decode_single_token_bytes(token) for token in token_list_1]
tokens_2 = [encoding_2.decode_single_token_bytes(token) for token in token_list_2]

print(tokens)
print(tokens_1)
print(tokens_2)