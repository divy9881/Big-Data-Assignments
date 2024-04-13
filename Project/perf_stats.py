import subprocess
import csv

def write_to_csv(data):
    csv_file_path = "data.csv"

    # Specify the fieldnames based on the keys in your dictionaries
    fieldnames = data[0].keys()

    # Write the data to CSV
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        for row in data:
            writer.writerow(row)

    print("CSV file has been created successfully.")


def calc_stats(sentences):
    results = []

    # code to populate 100 results for each sentence length.
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
        #print(sentence_stat)

    print(len(results))

    # Now, the results array is populated, now we need to calculate averages for each unique sentence length.
    averages = []
    average = {}
    su = {}
    cur_len = 1
    count = 0
    for result in results:
        if cur_len != result['length']:
            # print("sum : ")
            # print(su)
            # print(count)
            for instr in instr_arr:
                average[instr] = su[instr]/count
            average['length'] = cur_len
            count = 0
            cur_len *= 2
            averages.append(average)
            average = {}
            su = {}

        if cur_len == result['length']:
            for instr in instr_arr:
                if instr in su:
                    su[instr] += float(result[instr].replace(',', ''))
                else:
                    su[instr] = float(result[instr].replace(',', ''))
            count += 1
    
    # calculating average for the last length.
    for instr in instr_arr:
        average[instr] = su[instr]/count
    average['length'] = cur_len
    count = 0
    cur_len *= 2
    averages.append(average)
    average = {}
    su = {}

    print(averages)
    write_to_csv(averages)