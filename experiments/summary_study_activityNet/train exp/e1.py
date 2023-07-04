"""
generating summary of ActivityNet Caption train set
Total Videos: 705

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
train_summary_id_caption_path ="/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/train exp/train_summary_id_to_caption.json"


with open(train_summary_id_caption_path,'r') as f:
    train_summary_id_caption = json.load(f)
print(len(train_summary_id_caption))

os.chdir("../../../")
video_dir = "data/ActivityNet_captions dataset/validation/"
print(os.getcwd())
c = 0
output_train_summary_id_caption ={}
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
    
    output_train_summary_id_caption[video_id]= video
    
    exp_dir = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/train exp/"
    with open(exp_dir+"output_train_summary_id_caption(0-353).json",'w') as f:
            json.dump(output_train_summary_id_caption,f,indent=4)
    # time.sleep(2) 
    


# vidoe id list
train_video_ids = list(train_summary_id_caption.keys())
# print("ids",len(ids))



for i in tqdm(range(0,353)):
    video_id =train_video_ids[i]
    video =train_summary_id_caption[video_id]
    # print(video_id)
    # print(video)
    generate_cap(video_id,video)








    




