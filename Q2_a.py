import os
import pickle

def create_inverted_index(folder_path):
    inverted_index = {}

    # Get a list of preprocessed files in the folder
    preprocessed_file_list = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]

    for filename in preprocessed_file_list:
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            tokens = file.read().split()

            # Build the inverted index
            for term in set(tokens):  # Use set to remove duplicates
                if term not in inverted_index:
                    inverted_index[term] = [filename]
                else:
                    inverted_index[term].append(filename)

    return inverted_index


preprocessed_folder_path = './text_files'

# Create the inverted index
unigram_inverted_index = create_inverted_index(preprocessed_folder_path)
# print(unigram_inverted_index.keys())

# Save the inverted index using pickle
with open('unigram_inverted_index.pkl', 'wb') as pickle_file:
    pickle.dump(unigram_inverted_index, pickle_file)

# Load the inverted index using pickle
with open('unigram_inverted_index.pkl', 'rb') as pickle_file:
    loaded_inverted_index = pickle.load(pickle_file)

# Print a sample of the loaded inverted index (optional)
print("Sample Loaded Inverted Index:")
for term, filenames in list(loaded_inverted_index.items())[:5]:
    print(f"{term}: {filenames}")
