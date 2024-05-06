import sys

def read_text_file(file_path):
    """Reads text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', ' ')
        text = text.split(' ')
    return text

def generate_sentences(text, min_length, max_length):
    """Generates sentences of varying lengths from the given text."""
    length=min_length
    sentences = []
    text_length = len(text)
    while length <= max_length:
        count = 0
        start_index = 0
        # Generate 50 sentences of length words, to average out all variance in results.
        while count < 10:
            end_index = (start_index+length)%text_length

            if start_index < end_index:
                sentences.append((' '.join(text[start_index:end_index]),length))
            else : 
                sen1 = ' '.join(text[0:end_index])
                sen2 = ' '.join(text[start_index:text_length])
                sentences.append((sen2 + sen1, length))
                
            start_index = (start_index+length+1)%text_length
            count += 1
        length *= 2

    return sentences

def main():

    if len(sys.argv) != 3:
        print("Usage: python script_name.py <text_file_path> <max_length>")
        sys.exit(1)
    
    # command : python3 generate_sentences.py english/base_dataset 128000

    file_path = sys.argv[1]
    # Max length from command-line argument
    max_length = int(sys.argv[2])

    # Read the text from the file
    text = read_text_file(file_path)

    # Generate sentences
    sentences = generate_sentences(text, max_length)

    # Display the generated sentences
    for i, sentence in enumerate(sentences):
        print(f"Sentence {i+1} ({sentence[1]} words): {sentence[0]}")

if __name__ == "__main__":
    main()
