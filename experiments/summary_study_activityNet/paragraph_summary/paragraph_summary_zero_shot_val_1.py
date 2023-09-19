import json
import os 
import subprocess
from tqdm import tqdm

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
def write_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
def zero_cap_runner(path,start,end):
    if os.path.exists(path):
        command = f"python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path {path} --start_sec {start} --end_sec {end}"
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        generated_caption = output.split("\n")[-3].split(":")[1].strip()
        # generated_caption = "siuuuuuuuuuuuuu."
    else:
        generated_caption= "_"  
        
    return generated_caption

def generate_cap(video_id, video_details):
    timestamps = video_details['timestamps']
    # print(timestamps)
    path = video_details['path']
    # print(path)
    paragraph_summary = ""
    for time in tqdm(timestamps):
        # print(time)
        start =time[0]
        end = time [1]
        # print(f"start: {start}")
        # print(f"end: {end}")
        generated_cap = zero_cap_runner(path,start,end)
        if paragraph_summary == "":
            paragraph_summary = generated_cap
        else: 
            paragraph_summary = paragraph_summary+" "+ generated_cap
        
    video_details['zero_shot_generated_paragraph_summary']= paragraph_summary



    output_paragraph_summary_zeroshot_experiment[video_id]= video_details

    exp_dir = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/paragraph_summary/"
    write_to_json_file(output_paragraph_summary_zeroshot_experiment,exp_dir+"output_paragraph_summary_zeroshot_experiment.json")
#-----------------------------------
an_cap_val_1_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/data/ActivityNet_captions_dataset/val_1.json"
an_cap_val_2_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/data/ActivityNet_captions_dataset/val_2.json"


experiment_5_videos_path = "/home/grads/h/hasnat.md.abdullah/open_ended_activity_analysis/zero-shot-video-to-text/experiments/summary_study_activityNet/paragraph_summary/experiment_decap_low10_videos.json"
experiment_5_videos = load_json_file(experiment_5_videos_path)

video_dir = "data/ActivityNet_captions dataset/validation/"
# print(os.getcwd())
os.chdir("../../../")

# print(os.getcwd())

video_ids = [
    "v_4Lu8ECLHvK4",
    "v_yE5whKJ-DE4",
    "v_sRN_crwj3B4",
    "v_OPp3DqFq0O0",
    "v_1926p23ooUM"
]

# c = 0
output_paragraph_summary_zeroshot_experiment ={}



    

for id in tqdm(video_ids):
    video_details = experiment_5_videos[id]
    # print(video_details)
    generate_cap(id,video_details)
    
    


    