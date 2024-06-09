import urllib.request
from pathlib import Path

def download_file(url, file_path):
    print(f"Downloading {url} to {file_path}...")
    urllib.request.urlretrieve(url, file_path)
    urllib.request.urlretrieve(url, file_path)

def open_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    print("Total number of character:", len(raw_text))
    print(raw_text[:99])

if __name__ == "__main__":
    url = ("https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt")
    file_path = "the-verdict.txt"
    
    if Path(file_path).is_file():
        print(f"{file_path} already exists.")
    else:
        download_file(url, file_path)

    open_file(file_path)
