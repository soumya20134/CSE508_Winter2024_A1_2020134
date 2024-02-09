import os
import pickle

def create_positional_index(folder_path):
    positional_index = {}

    # Get a list of preprocessed files in the folder
    preprocessed_file_list = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]

    for filename in preprocessed_file_list:
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            tokens = file.read().split()

            # Build the positional index
            for position, term in enumerate(tokens):
                if term not in positional_index:
                    positional_index[term] = {filename: [position]}
                else:
                    if filename not in positional_index[term]:
                        positional_index[term][filename] = [position]
                    else:
                        positional_index[term][filename].append(position)

    return positional_index

# Specify the folder path containing preprocessed text files
preprocessed_folder_path = './text_files'

# Create the positional index
positional_index = create_positional_index(preprocessed_folder_path)

# Save the positional index using pickle
with open('positional_index.pkl', 'wb') as pickle_file:
    pickle.dump(positional_index, pickle_file)

# Load the positional index using pickle (optional)
with open('positional_index.pkl', 'rb') as pickle_file:
    loaded_positional_index = pickle.load(pickle_file)

# Print a sample of the loaded positional index (optional)
print("Sample Loaded Positional Index:")
for term, postings in list(loaded_positional_index.items())[:5]:
    print(f"{term}: {postings}")
