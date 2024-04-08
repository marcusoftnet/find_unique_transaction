# Unique bank statement transaction finder

I'm trying to find unique transaction texts to be able to better find categories. 

I used ChatGPT to write this entire repo. Except this file

## Usage 

```bash
usage: app.py [-h] [--min_length MIN_LENGTH] [--min_matches MIN_MATCHES] file_path

Find related substrings in transaction texts

positional arguments:
  file_path             Path to the JSON file containing transaction texts

options:
  -h, --help            show this help message and exit
  --min_length MIN_LENGTH
                        Minimum length of substring to consider (default: 3)
```

For example;
```bash
python app.py data.txt --min_length 5 --min_matches 5
```
