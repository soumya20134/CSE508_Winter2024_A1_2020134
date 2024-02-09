from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pickle

def load_inverted_index(filename):
    with open(filename, 'rb') as file:
        index = pickle.load(file)
    
    return index

def process_query(terms, operations, inverted_index):

    result = set()
    result = set(inverted_index.get(terms[0],[]))

    j=0
    for i in range(1,len(terms)):
        term = terms[i]
        operation = operations[j]
        j+=1
        if operation == 'AND':
            result = result.intersection(inverted_index.get(term,[]))

        elif operation == 'OR':
                result = result.union(inverted_index.get(term,[]))

        elif operation == 'AND NOT':
            result = result.difference(inverted_index.get(term,[]))
        
        elif operation == 'OR NOT':
            lst = set(inverted_index.get(term,[]))
            everything = set()

            for i in range(999):
                everything.add("file"+str(i)+".txt")

            or_not = everything.difference(lst)
            result = result.union(or_not)
    
    return result


def main():

    num_queries = int(input())
    inverted_index_file = 'unigram_inverted_index.pkl'
    inverted_index = load_inverted_index(inverted_index_file)
    
    query_setences = []
    query_operations_ = []
    for _ in range(num_queries):
        # Read each query and perform the operations
        query_setence = input()
        query_operations = input().split(", ")

        query_setences.append(query_setence)
        query_operations_.append(query_operations)

    
    for i in range(num_queries):
        query_setence = query_setences[i]
        query_operations = query_operations_[i]

        query_setence = query_setence.lower()
        tokens = word_tokenize(query_setence)
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]


        # Print the results

        query_result = process_query(tokens,query_operations, inverted_index)

        query_statement = tokens[0]
        for j in range(len(query_operations)):
            query_statement += " "+query_operations[j] + " " + tokens[j+1]

        print(f"Query {i + 1}:{query_statement}")
        #query_result = process_query(tokens, query_operations, inverted_index)
        print(f"Number of documents retrieved for query {i + 1}: {len(query_result)}")
        print(f"Names of the documents retrieved for query {i + 1}: {', '.join(query_result)}")

        

if __name__ == "__main__":
    main()

