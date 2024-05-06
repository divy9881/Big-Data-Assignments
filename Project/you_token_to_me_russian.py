import sys
import youtokentome as yttm


train_data_path = "train_russian.txt"
model_path = "russian.model"

# Generating random file with training data
# 10000 lines with 100 characters in each line
# n_lines = 10000
# n_characters = 100
# with open(train_data_path, "w") as fout:
#     for _ in range(n_lines):
#         print("".join([random.choice("abcd ") for _ in range(n_characters)]), file=fout)

# Training model
# yttm.BPE.train(data=train_data_path, vocab_size=5000, model=model_path)

# Loading model
bpe = yttm.BPE(model=model_path)

sentence = ""
with open(sys.argv[1], 'r') as file:
    sentence = file.read()

test_text = sentence

# test_text = sys.argv[1]

# running tokenizer
#print(bpe.encode([test_text], output_type=yttm.OutputType.SUBWORD))
bpe.encode([test_text], output_type=yttm.OutputType.SUBWORD)