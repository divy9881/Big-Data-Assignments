import subprocess

def calc_stats(sentences):
    results = []
    instr_arr = ["instructions","cache-misses","cache-references","L1-dcache-load-misses","L1-dcache-loads","time","LLC-load-misses","LLC-loads"]
    for sentence in sentences:
        sentence_stat = {}
        output = subprocess.run(["sudo","perf","stat","-e","instructions,cache-misses,cache-references,L1-dcache-load-misses,L1-dcache-loads,LLC-load-misses,LLC-loads","python3", "you_token_to_me.py", sentence[0]], capture_output = True)
        
        formatted_text = str(output.stderr).split(" ")
        cleaned_data = [item for item in formatted_text if item.strip()]

        #print(cleaned_data)

        for instr in instr_arr:
            for j in range(0,len(cleaned_data)):
                if(cleaned_data[j] == instr and instr == "time"):
                    sentence_stat[instr] = cleaned_data[j-2]
                elif(cleaned_data[j] == instr):
                    sentence_stat[instr] = cleaned_data[j-1]
                    break
        
        sentence_stat["length"] = sentence[1]
        results.append(sentence_stat)  
        #print(cleaned_data)
        print(sentence_stat)

    print(len(results))