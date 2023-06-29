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
    
#multi threading 
max_threads = min(4, len(combined_val_summary_id_caption))
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    # Submit the video processing tasks to the thread pool
    futures = [executor.submit(generate_cap,video_id, combined_val_summary_id_caption[video_id]) for video_id in combined_val_summary_id_caption]

    # Wait for all tasks to complete
    for i,future in enumerate(futures):
        
        future.result()
    
with open("output_combined_val_summary_id_caption.json",'+a') as f:
        json.dump(output_combined_val_summary_id_caption,f,indent=4)

# for video_id in combined_val_summary_id_caption:
#     print(video_id)
#     video = combined_val_summary_id_caption[video_id]
#     generate_cap(video_id, video)


#     break

    






    




