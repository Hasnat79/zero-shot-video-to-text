"""
generating summary of ActivityNet Caption Validation set 2
Total Videos: 434

"""
#-------------------------------------------
import os
import subprocess
from tqdm import tqdm
import json
from concurrent.futures import ThreadPoolExecutor
import time

#load summary data file
val_2_summary_id_caption_path ="/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/val_2 exp/val_2_summary_id_to_caption.json"


with open(val_2_summary_id_caption_path,'r') as f:
    val_2_summary_id_caption = json.load(f)
print(len(val_2_summary_id_caption))

os.chdir("../../../")
video_dir = "data/ActivityNet_captions dataset/validation/"
print(os.getcwd())
c = 0
output_val_2_summary_id_caption ={}
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
    
    output_val_2_summary_id_caption[video_id]= video
    
    exp_dir = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/val_2 exp/"
    with open(exp_dir+"output_val_2_summary_id_caption.json",'w') as f:
            json.dump(output_val_2_summary_id_caption,f,indent=4)
    # time.sleep(2) 
    
#index distribution
# total: 434

# 0-55*
# 55-110
# 110-165
# 165-220
# 220-275
# 275-330
# 330-385
# 385-434

# vidoe id list
val_2_video_ids = list(val_2_summary_id_caption.keys())
# print("ids",len(ids))



for i in tqdm(range(110,434)):
    video_id =val_2_video_ids[i]
    video =val_2_summary_id_caption[video_id]
    # print(video_id)
    # print(video)
    generate_cap(video_id,video)








    




