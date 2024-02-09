import os
import string
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pickle


def load_positional_index(filename):
    with open(filename, 'rb') as file:
        index = pickle.load(file)
    return index

def process_ordered_phrase_query(tokens, positional_index):
    
    result = set()

    if tokens[0] in positional_index:
        result = set(positional_index[tokens[0]].keys())

    for i in range(1,len(tokens)):
        prev_term = tokens[i-1]
        curr_term = tokens[i]

        if(prev_term not in positional_index or curr_term not in positional_index):
            return set()
        
        doc_prev = set(positional_index[prev_term].keys())
        doc_curr = set(positional_index[curr_term].keys())

        common_docs = doc_prev.intersection(doc_curr)
        positional_common_docs = set()

        for doc in common_docs:
            positions_prev = positional_index[prev_term][doc]
            positions_curr = positional_index[curr_term][doc]

            i = 0
            j = 0
            while(i<len(positions_prev) and j<len(positions_curr)):
                if(positions_prev[i]==positions_curr[j]-1):
                    positional_common_docs.add(doc)
                    break
                elif(positions_prev[i] > positions_curr[j]-1):
                    j+=1
                else:
                    i+=1
        
        result = result.intersection(positional_common_docs)

    return result


def main():
    # Specify the path to the positional index file
    positional_index_file = 'positional_index.pkl'

    # Load the positional index
    positional_index = load_positional_index(positional_index_file)

    # Read the number of queries
    num_queries = int(input())

    query_setences = []
    for _ in range(num_queries):
        # Read each ordered phrase query and perform the operations
        query = input()
        query_setences.append(query)

    for i in range(num_queries):
        query = query_setences[i]
        query = query.lower()
        tokens = word_tokenize(query)
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
        query_result = process_ordered_phrase_query(tokens, positional_index)

        # Print the results
        print(f"Number of documents retrieved for query {i + 1} using positional index: {len(query_result)}")
        print(f"Names of documents retrieved for query {i + 1} using positional index: {', '.join(sorted(query_result))}")

if __name__ == "__main__":
    main()

