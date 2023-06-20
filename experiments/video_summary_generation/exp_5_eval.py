"""
evaluating the generated summaries of 50 (least freq labels) videos

"""
import os
import subprocess
import json
from tqdm import tqdm
import nltk
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
import statistics

# loading the output file from exp_5
file_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/video_summary_generation/output_least50_video_summary.json"
with open(file_path,'r') as f: 
    testing = json.load(f)
# for i in testing:
#     print(i)
#     break
# bleu score calculation
reference_captions = []
candidate_captions = []
for i in testing: 
    if i['generated_summary']!="_":
        reference_captions.append(i['title'])
        candidate_captions.append(i['generated_summary'])

# Tokenize the captions
reference_captions = [caption.split() for caption in reference_captions]
candidate_captions = [caption.split() for caption in candidate_captions]

print("len(reference_captions)",len(reference_captions))
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
