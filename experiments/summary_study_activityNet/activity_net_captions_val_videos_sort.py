"""
Checked downloadable(from youtube) videos count for ActivityNet captions validation set
(I ran this locally on my pc where the full dataset is downloaded)
Count: 571
"""

import os
import json
import shutil
from pprint import pprint
# from tqdm import tqdm



# specify download directory
directory = './data/ActivityNet_200/'

destination_folder = "./data/ActivityNet_captions/"


# open json file
with open('activity_net.v1-3.min.json') as data_file:    
    data = json.load(data_file)
with open('AN_caps_val_summary_video_ids.json') as f:
	AN_val_summary_video_ids = json.load(f)
print(len(AN_val_summary_video_ids))
# take only video informations from database object
videos = data['database']

total_videos = len(videos)
print("total videos:",total_videos)
# iterate through dictionary of videos
count =0
for id, key in enumerate(videos):
	# print(key)
	k = "v_"+key
	
	
	if k in AN_val_summary_video_ids:
		# take video
		video = videos[key]

		# find video subset
		subset = video['subset']

		# find video label
		annotations = video['annotations']
		label = ''
		if len(annotations) != 0:
			label = annotations[0]['label']
			label = '/' + label.replace(' ', '_')

		# create folder named as <label> if does not exist
		label_dir = directory + subset + label
		video_path = label_dir+"/"+key+".mp4"
		# print(video_path)
		if os.path.exists(video_path):
			count+=1
			destination_dir = destination_folder+subset+label
			destination_video_path = destination_dir+"/"+key+".mp4"
			# print(destination_video_path)
			if not os.path.exists(destination_dir):
				os.makedirs(destination_dir)
				print('Created directory: ' + destination_dir)
			shutil.copy(video_path,destination_video_path)
		# else:
		# 	print("no")

		

		
		
		
		
	# try:
	# 	# Create a YouTube object with the provided URL
	# 	yt = YouTube(url)
		
	# 	# Filter the available video streams to get the highest resolution
	# 	video = yt.streams.get_highest_resolution()
		
	# 	# Download the video to the specified output path, rename the video as the key
	# 	video.download(label_dir, key+'.mp4')
	# 	videoCounter += 1		
	# 	print("{}/{}/{} Video downloaded successfully! {} {}".format(id+1, total_videos, videoCounter, key, url))
		
		

	# except Exception as e:
	# 	print("{}/{}/{} Error: {}! {} {}".format(id+1, total_videos, videoCounter, str(e), key, url))
	
print("count",count)	

