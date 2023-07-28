import json
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
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
    # similarities_first = cosine_similarity(reference_embeddings[0:1],candidate_embeddings[0:]) 
    # print(similarities_first)
    # print(len(similarities_first[0]))
    # print(statistics.mean(similarities_first[0]))

    sim_scores= []
    for i in range(len(reference)):
        sim = cosine_similarity(reference_embeddings[i:i+1],candidate_embeddings[i:i+1])
        print(f"hasnat:\t{candidate[i]}")
        print(f"Tian:\t{reference[i]}")
        print(f"cosine similarity:\t{sim[0][0]:.4f}")
        sim_scores.append(sim[0][0])
        print("=======================================")
    print(f"average cosine similarity scores = {statistics.mean(sim_scores):.4f}")
    sim = cosine_similarity(reference_embeddings[0:1],candidate_embeddings[1:])
    
    print(f"average similarity between irrelevant caps: {statistics.mean(sim[0]):.4f}")

hasnat_high10_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/manual_captioning/decap_output_val_1_summary_id_caption_hasnat_high10.json"
tian_high10_path ="/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/manual_captioning/decap_output_val_1_summary_id_caption_tian_high10.json"

hasnat_high10 = load_json_file(hasnat_high10_path)
tian_high10 = load_json_file(tian_high10_path)
# filling the candidates and references
reference = []
candidate = []
for v in hasnat_high10:
            # Extract 'tian_caption_no_instruction' in a list called 'candidate'
            # candidate.append(remove_punctuation(v[1].get('tian_caption_no_instruction', '')))
            candidate.append(v[1].get("hasnat_caption_no_instruction", ''))
for v in tian_high10:
    reference.append(v[1].get("summary_cap", ''))

gen_cos_sim(reference,candidate)