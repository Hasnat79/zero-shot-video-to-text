import json
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import statistics
import nltk
import string
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

hasnat_low10_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/manual_captioning/decap_output_val_1_summary_id_caption_hasnat_low10.json"
tian_low10_path ="/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/manual_captioning/decap_output_val_1_summary_id_caption_tian_low10.json"

hasnat_low10 = load_json_file(hasnat_low10_path)
tian_low10 = load_json_file(tian_low10_path)
# filling the candidates and references
reference = []
candidate = []
for v in hasnat_low10:
            # Extract 'tian_caption_no_instruction' in a list called 'candidate'
            # candidate.append(remove_punctuation(v[1].get('tian_caption_no_instruction', '')))
            candidate.append(v[1].get("hasnat_caption_no_instruction", ''))
for v in tian_low10:
    reference.append(v[1].get("summary_cap", ''))

# Define the BERT model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)



# Function to calculate sentence embeddings using BERT
def sentence_embeddings(sentences):
    inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy()

# Calculate embeddings for Candidate 1 and all reference sentences
candidate1_embedding = sentence_embeddings(candidate[:1])

reference_embeddings = sentence_embeddings(reference)

# Calculate cosine similarity between Candidate 1 and all references (excluding Reference 1)

# for i in candidate_embeddings:
#      print(len(i))
#      break
dis_sim = []
for i in range(1, len(reference)):
    reference_embedding = reference_embeddings[i:i+1]
    cosine_similarities = cosine_similarity(candidate1_embedding, reference_embedding)
    print(f"Cosine Similarity between Candidate 1 and Reference {i+1}: {cosine_similarities[0][0]:.4f}")
    dis_sim.append(cosine_similarities[0][0])

print(len(dis_sim))
print(f"{statistics.mean(dis_sim):.4f}")