import sys
import json
import nltk
import string
from nltk.translate.bleu_score import sentence_bleu
import statistics

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
def remove_punctuation(sentence):
    # Remove punctuations from the sentence
    no_punct = sentence.translate(str.maketrans("", "", string.punctuation))
    # Lowercase all the words
    lowercase_sentence = no_punct.lower()

    # stem words
    stemmer = nltk.stem.PorterStemmer()
    sentence = " ".join([stemmer.stem(word) for word in lowercase_sentence.split()])
    return sentence

def generate_bleu(data_1,data_2=None,reference_key='',candidate_key=''):
    reference = []
    candidate = []
    if data_2 == None: 
        for v in data_1:
            # Extract 'tian_caption_no_instruction' in a list called 'candidate'
            # candidate.append(remove_punctuation(v[1].get('tian_caption_no_instruction', '')))
            candidate.append(remove_punctuation(v[1].get(candidate_key, '')))

            # Extract 'summary_cap' in a list called 'reference'
            # reference.append(remove_punctuation(v[1].get('summary_cap', '')))
            reference.append(remove_punctuation(v[1].get(reference_key, '')))
    else: 
        for v in data_1:
            # Extract 'tian_caption_no_instruction' in a list called 'candidate'
            # candidate.append(remove_punctuation(v[1].get('tian_caption_no_instruction', '')))
            candidate.append(remove_punctuation(v[1].get(candidate_key, '')))
        for v in data_2:
            reference.append(remove_punctuation(v[1].get(reference_key, '')))
    print(reference)
    # print("len(reference_captions)",len(reference))
    # print("len(candidate_captions)",len(candidate))
    # Tokenize the captions
    reference_captions = [caption.split() for caption in reference]
    candidate_captions = [caption.split() for caption in candidate]
    # Calculate BLEU score
    cumulative_bleu_scores = []
    weight_list = [(1, 0, 0, 0),(0.5, 0.5, 0, 0),(0.33, 0.33, 0.33, 0),(0.25, 0.25, 0.25, 0.25)]
    for n in range(1, 5):
        bleu_scores = [sentence_bleu(ref, cand, weights=weight_list[n-1]) for ref, cand in zip(reference_captions, candidate_captions)]
        
        # print(type(bleu_scores))

        average_bleu_score = statistics.mean(bleu_scores)
        cumulative_bleu_scores.append(average_bleu_score)

    # Print cumulative BLEU scores
    print("cumulative BLEU scores:")
    for i, score in enumerate(cumulative_bleu_scores):
        print(f"BLEU@{i+1}: {score:.4f}")

def main():
    

    hasnat_high10 = sys.argv[1]
    hasnat_high10 = load_json_file(hasnat_high10)
    
    tian_high10 = sys.argv[2]
    tian_high10 = load_json_file(tian_high10)
    
    print("bleu scores: val-v1 High10 annotations\n")
    print("hasnat vs high10")
    generate_bleu(data_1=hasnat_high10,
                  
                reference_key="summary_cap",
                candidate_key="hasnat_caption_no_instruction")
    print("\ntian vs high10")
    generate_bleu(data_1=tian_high10,
                  reference_key="summary_cap",
                candidate_key="tian_caption_no_instruction")
    
    print("\ntian vs hasnat")
    generate_bleu(data_1=tian_high10,
                data_2=hasnat_high10,
                reference_key="hasnat_caption_no_instruction",
                candidate_key="tian_caption_no_instruction")
if __name__ == "__main__":
    main()