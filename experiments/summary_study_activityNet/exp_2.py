"""
generating summary of ActivityNet Caption Validation set
Total Videos: 571

"""
#-------------------------------------------
import os
import subprocess
from tqdm import tqdm
import json
from concurrent.futures import ThreadPoolExecutor
import time
#load summary data file
combined_val_summary_id_caption_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/combined_val_summary_id_to_caption.json"
with open(combined_val_summary_id_caption_path,'r') as f:
    combined_val_summary_id_caption = json.load(f)
print(len(combined_val_summary_id_caption))

os.chdir("../../")
video_dir = "data/ActivityNet_captions dataset/validation/"
print(os.getcwd())
c = 0
output_combined_val_summary_id_caption ={}
def generate_cap(video_id, video):
    
    start = video['start']
    end = video['end']
    # print(type(end))
    path = str(video['path'])

    # print(path)
    if os.path.exists(path):
        command = f"python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path {path} --start_sec {start} --end_sec {end}"
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        generated_caption = output.split("\n")[-3].split(":")[1].strip()
    
        video['generated_summary'] = generated_caption
    else:
        video['generated_summary']= "_"
    
    output_combined_val_summary_id_caption[video_id]= video
    
    # time.sleep(2) 
    
#index distribution
# total: 754
# last index : 753
# 0-150* 
# 150-300 
# 300-450
# 450-600
# 600-754
    
# vidoe id list
combined_val_video_ids = list(combined_val_summary_id_caption.keys())
print(len(combined_val_video_ids))
for i in tqdm(range(0,150)):
    video_id = combined_val_video_ids[i]
    video = combined_val_summary_id_caption[video_id]
    # print(video_id)
    # print(video)
    generate_cap(video_id,video)


    

with open("(0-150)output_combined_val_summary_id_caption.json",'w') as f:
        json.dump(output_combined_val_summary_id_caption,f,indent=4)





    




