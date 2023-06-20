"""
checking a generated caption of a whole video. 
Objective: To know, how much better the summary of a video is on zero-shot scenario

# selecting a random video to see what the model generates


ground truth summary caption: not available *we need to check quality of output manually* 
Label: Assembling bicycle
Id: BfnM0eyjB5Q
yt_link: https://www.youtube.com/watch?v=BfnM0eyjB5Q
settings: random prompts
model: clip, gpt2
generated output: Video illustrating saddle bike repair on the job, including a wrench and tool.    
Comment: the original video title includes : How to install a bike seat. The generated output is semantically
correct with the video
"""
#-------------------------------------------
import os
import subprocess
video_path = "data/ActivityNet_200/training/Assembling_bicycle/BfnM0eyjB5Q.mp4"
start = 12.07
end = 185.62

os.chdir("../../")

command = f"python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path {video_path}"
# Run the command and capture the output
output = subprocess.check_output(command, shell=True, universal_newlines=True)
generated_caption = output.split("\n")[-3].split(":")[1].strip()
print(generated_caption)

