# Sidfinder

Sensitive Information Disclosure Finder in Source Code

Sidfinder aims to find sensitive information disclosure by examining the source codes of websites in the given domain or domains.

- This tool makes a comparison with the source codes by using the words that may contain sensitive information in the 'keywords.txt' file.
- And and creates a file named 'results.txt' containing the results in the same folder.

- The reason for the use of keywords as text files is to add data that the user wants to compare and potential disclosures.

- WARNING: The content of the 'keyword.txt' and 'target file' must be such that there is only one keyword per line.

## Requirements 

- Only need Python and libraries


## Installations

- Download as zip or copy code and create your own python file.
- If create on your own make sure create other necessarry file:

  "keywords.txt"
 

## Usage

```
-h                  	User Manual
-d 'domain' 	        Processes the website on the specified domain.
-l 'file_path.txt'   	Processes the websites on the file.

```
## Usage example

```
python3 sidfinder.py -d example.com
```
```
python3 sidfinder.py -l url_list.txt
```

