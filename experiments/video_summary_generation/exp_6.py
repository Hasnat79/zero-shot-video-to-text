"""
generating summary / captions of whole videos
data: 1 video from each of the 50 least frequent labels
output: save the summaries on a json file
evaluate: exp_5_eval.py

"""
#-------------------------------------------
import os
import subprocess
from tqdm import tqdm
import json

#load summary data file
summary_data_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/video_summary_generation/least50_video_summary.json"
with open(summary_data_path,'r') as f:
    video_details = json.load(f)

video_dir = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/data/ActivityNet_200/training/"
os.chdir("../../")
for i in tqdm(range(len(video_details))):
    video = video_details[i]
    path = video['path']
    video_path = video_dir+path
    if os.path.exists(video_path):
        command = f"python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path {video_path}"
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        generated_caption = output.split("\n")[-3].split(":")[1].strip()
    
        video['generated_summary'] = generated_caption
    else:
        video['generated_summary']= "_"

    if i%2 == 1:
        with open("output_least50_video_summary.json", 'w') as f:
            json.dump(video_details,f,indent=4)
         

    






# os.chdir("../../")

# command = f"python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path {video_path}"
# # Run the command and capture the output
# output = subprocess.check_output(command, shell=True, universal_newlines=True)
# generated_caption = output.split("\n")[-3].split(":")[1].strip()
# print(generated_caption)

