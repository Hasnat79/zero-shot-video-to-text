"""
generating summary of ActivityNet Caption Validation set 1
Total Videos: 380

"""
#-------------------------------------------
import os
import subprocess
from tqdm import tqdm
import json
from concurrent.futures import ThreadPoolExecutor
import time
os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
#load summary data file
val_1_summary_id_caption_path ="/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/val_1 exp/val_1_summary_id_to_caption.json"


with open(val_1_summary_id_caption_path,'r') as f:
    val_1_summary_id_caption = json.load(f)
print(len(val_1_summary_id_caption))

os.chdir("../../../")
video_dir = "data/ActivityNet_captions dataset/validation/"
print(os.getcwd())
c = 0
output_val_1_summary_id_caption ={}
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
    
    output_val_1_summary_id_caption[video_id]= video
    
    exp_dir = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/val_1 exp/"
    with open(exp_dir+"output_val_1_summary_id_caption.json",'w') as f:
            json.dump(output_val_1_summary_id_caption,f,indent=4)
    # time.sleep(2) 
    
#index distribution
# total: 380
# last index : 753
# 0-75* 
# 75-150
# 150-225
# 225-300
# 300-380

# vidoe id list
val_1_video_ids = list(val_1_summary_id_caption.keys())
# print("ids",len(ids))



for i in tqdm(range(0,380)):
    video_id =val_1_video_ids[i]
    video =val_1_summary_id_caption[video_id]
    # print(video_id)
    # print(video)
    generate_cap(video_id,video)








    




