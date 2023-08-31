import sys
import requests


def find_keyword_occurrences(text, keyword):
    occurrences = []
    start = 0
    while start < len(text):
        index = text.find(keyword, start)
        if index == -1:
            break
        occurrences.append(index)
        start = index + 1
    return occurrences

########################################################
#-h function
########################################################

def print_help():
    print("\n-------------------------------------------------------")
    print("Sensitive Information Disclosure Finder in Source Code")
    print("-------------------------------------------------------")
    print("\n---Sidfinder aims to find sensitive information disclosure by examining the source codes of websites in the given domain or domains.")
    print("\n---This tool makes a comparison with the source codes by using the words that may contain sensitive information in the 'keywords.txt' file in the same folder and saves what it finds as 'results.txt'")
    print("\nThe reason for the use of keywords as text files is to add data that the user wants to compare and potential disclosures.")
    print("\n------------------------------------------------------------------------------------------------------")
    print("Warning: The content of the 'keyword.txt' and 'target file' must be such that there is only one keyword per line.")
    print("------------------------------------------------------------------------------------------------------")
    print("\nUsage:")
    print("\n-h                  	User Manual.")
    print("-d 'domain' 	    	Processes the website on the specified domain.")
    print("-l 'file_path.txt'   	Processes the websites on the file.")
    print("\n---If you want longer outputs for the captured keywords, you can increase the values ​​on lines 59 and 60 in the 'sidfinder.py'.")
    print("\n\nExample:")
    print("\npython3 sidfinder.py -d example.com")
    print("\npython3 sidfinder.py -l url_list.txt")

##########	ADD MISSING HTTP HEADER		##########

def process_url(url, keywords, output_file):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

##########	REQUEST PART	##########
    try:
        response = requests.get(url)
        if response.status_code == 200:
            source_code = response.text
            with open(output_file, "a") as file:
                file.write(f"***'{url}' output:\n")
                keyword_found = False  # Track if any keyword is found
                for keyword in keywords:
                    occurrences = find_keyword_occurrences(source_code, keyword)
                    if occurrences:
                        keyword_found = True
                        file.write(f"\n\n'{keyword}' found:\n")
                        for index in occurrences:
                            snippet_start = max(index - 400, 0) #### Print out keyword before 400 characters
                            snippet_end = min(index + 400, len(source_code)) ## after 400 characters
                            snippet = source_code[snippet_start:snippet_end]
                            file.write(f"\n____________________\n\n{snippet}\n____________________\n")
                
                if not keyword_found:
                    file.write("\n NOT FOUND \n")
                    
                file.write("\n")
        else:
            print("\nConnection Error. \nURL=",url,"\nError Code:", response.status_code)
    except requests.RequestException as e:
        print("Connection Error:", e)

def process_file(file_path, keywords, output_file):
    with open(file_path, "r") as file:
        urls = file.readlines()
        for url in urls:
            url = url.strip()
            process_url(url, keywords, output_file)

##########	SYMTAX ERROR	##########

if len(sys.argv) < 2:
    print("'python3 sidfinder.py -h' for help ")
    sys.exit(1)

option = sys.argv[1]

if option == "-h":
    print_help()
    sys.exit(0)

if len(sys.argv) < 3:
    print("Missing argument. Help: 'python3 sidfinder.py -h'")
    sys.exit(1)

########## 	 OUTPUT  	########## 

input_value = sys.argv[2]
output_file = "results.txt"

with open("keywords.txt", "r") as file:
    keywords = file.read().splitlines()

########## 	PARAMETER 	##########

if option == "-d":
    process_url(input_value, keywords, output_file)
elif option == "-l":
    process_file(input_value, keywords, output_file)
else:
    print("Invalid option. Help: 'python3 sidfinder.py -h'")

print("\nOutputs save as: 'results.txt' ")
