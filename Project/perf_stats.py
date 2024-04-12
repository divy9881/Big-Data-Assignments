import subprocess

def calc_stats(sentences):
    results = {}

    for sentence in sentences:
        subprocess.run(["python3", "you_token_to_me.py", sentence[0]]) 
