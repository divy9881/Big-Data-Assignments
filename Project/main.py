import sys
from generate_sentences import generate_sentences,read_text_file
from perf_stats import calc_stats

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
    calc_stats(sentences)
    # Display the generated sentences
    # for i, sentence in enumerate(sentences):
    #     print(f"Sentence {i+1} ({sentence[1]} words): {sentence[0]}")

if __name__ == "__main__":
    main()