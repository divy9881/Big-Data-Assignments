import subprocess
import csv
import time

def write_to_csv(data):
    csv_file_path = "sample_output.csv"

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
    instr_arr = ["time"]

    for sentence in sentences:
        sentence_stat = {}

        with open('large_sentence.txt', 'w') as file:
            # Write the string into the file
            file.write(sentence[0])

        start_time = time.time()

        # cpu limit command
        output = subprocess.run(["sudo","cpulimit","-l","1","-i","--","python3", "tik_token_file.py", "large_sentence.txt"], capture_output = True)

        end_time = time.time()
        # print(start_time)
        # print(end_time)
        
        sentence_stat["time"] = end_time-start_time
        sentence_stat["length"] = sentence[1]
        print(sentence_stat["time"])

        results.append(sentence_stat)  
        #print(cleaned_data)
        #print(sentence_stat)

    print(len(results))
    print(results)

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
                # print(instr)
                # print(result[instr])
                try:
                    if instr in su:
                        su[instr] += float(result[instr])
                    else:
                        su[instr] = float(result[instr])
                except Exception:
                    print("Exception occured " + instr)
                    print(Exception)
                    su[instr] = 0
                    
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