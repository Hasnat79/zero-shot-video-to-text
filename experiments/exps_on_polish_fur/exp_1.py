"""
#### exp 2
* video id: Ou24uqaFRPg
* total segments 8
* fixed prompt: video showing

BLEU@1: 0.0799
BLEU@2: 0.0000
BLEU@3: 0.0000
BLEU@4: 0.0000
"""
import os
import subprocess
import json
from tqdm import tqdm
import nltk
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
import statistics

videos_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/least_50_activity_net_first_vid_all_seg.json"
with open(videos_path,'r') as f:
    video_details = json.load(f)

# print(video_details)
os.chdir("../")
# print(os.getcwd())
video_dataset_dir = "data/ActivityNet_200/training/"
testing = video_details[:8] 
# print(testing)
id=0
for id in tqdm(range(id,len(testing))) :
    # print(id)
    # print(data)
    data = testing[id]
    path = video_dataset_dir+ str(data['path'])
    start = data['start']
    end = data['end']

    
    if os.path.exists(path):
        
        command = f"python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path {path} --start_sec {start} --end_sec {end}"
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        generated_caption = output.split("\n")[-3].split(":")[1].strip()
        print(generated_caption)
        testing[id]["generated_cap"] = generated_caption
    else:
        testing[id]["generated_cap"] = "_"

# bleu score calculation
reference_captions = []
candidate_captions = []
for i in testing: 
    
    reference_captions.append(i['caption'])
    candidate_captions.append(i['generated_cap'])

# Tokenize the captions
reference_captions = [caption.split() for caption in reference_captions]
candidate_captions = [caption.split() for caption in candidate_captions]

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

