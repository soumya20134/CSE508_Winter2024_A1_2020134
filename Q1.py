import os
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def pre_process(content,filename):
    # a. Lowercase the text
    content = content.lower()

    if filename in first_5_files:
        print(f"\nLowercased Content:\n{content}\n")

    # b. Perform tokenization
    tokens = word_tokenize(content)

    if filename in first_5_files:
        print(f"Tokenized Content:\n{tokens}\n")

    # c. Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    if filename in first_5_files:
        print(f"Content after Removing Stopwords:\n{tokens}\n")

    # d. Remove punctuations
    # e. Remove blank space tokens
    tokens = [token for token in tokens if token.strip() != '']

    if filename in first_5_files:
        print(f"tokens after Removing Blank Spaces:\n{tokens}\n")

    text = ' '.join(tokens)
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    if filename in first_5_files:
        print(f"Content after Removing Punctuations and Blank Spaces:\n{text}\n")

    return text


def pre_process_theFile(file_path,filename):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        if filename in first_5_files:
            print(f"\nOriginal Content of {file_path}:\n{content}\n")

        processed_content = pre_process(content,filename)

        if filename in first_5_files:
            print(f"Processed Content of {file_path}:\n{processed_content}\n")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)
    
folder_path = './text_files'
file_list = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]
first_5_files = file_list[:5]
print(first_5_files)

for filename in file_list:
    file_path = os.path.join(folder_path, filename)
    pre_process_theFile(file_path,filename)