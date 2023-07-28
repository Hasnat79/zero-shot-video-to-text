import json
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
import nltk
import string
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
def gen_cos_sim(reference,candidate):
    model_name = 'bert-base-uncased'

    model = SentenceTransformer(model_name)
    # print(model)
    reference_embeddings =  model.encode(reference)
    candidate_embeddings = model.encode(candidate)

    # #calculation similarities between first sentence and others
    # similarities_first = cosine_similarity(reference_embeddings[0:1],candidate_embeddings[1:]) 
    # print(len(similarities_first[0]))
    # print(statistics.mean(similarities_first[0]))

    sim_scores= []
    for i in range(len(reference)):
        sim = cosine_similarity(reference_embeddings[i:i+1],candidate_embeddings[i:i+1])
        
        print(f"val v1:\t{reference[i]}")
        print(f"val v2:\t{candidate[i]}")
        print(f"cosine similarity:\t{sim[0][0]:.4f}")
        sim_scores.append(sim[0][0])
        print("=======================================")
    print(f"average cosine similarity scores = {statistics.mean(sim_scores):.4f}")
    sim = cosine_similarity(reference_embeddings[0:1],candidate_embeddings[1:])
    
    print(f"average similarity between irrelevant caps: {statistics.mean(sim[0]):.4f}")

combined_val_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/combined_val_summary_id_to_caption.json"

combined_val_summary_id_to_cap = load_json_file(combined_val_path)

reference = []
candidate = []
for k,v in combined_val_summary_id_to_cap.items():
    if len(v) == 5:
        reference.append(v['summary_cap'])
        candidate.append(v['summary_cap_2'])


gen_cos_sim(reference,candidate)

