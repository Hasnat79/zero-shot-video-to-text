#!/bin/bash

# List of commands to execute
commands=(

    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Mixing_drinks/yjazHd6a5SQ.mp4 --start_sec 0.0 --end_sec 17.87"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Mixing_drinks/yjazHd6a5SQ.mp4 --start_sec 17.87 --end_sec 43.51"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Mixing_drinks/yjazHd6a5SQ.mp4 --start_sec 43.51 --end_sec 66.81"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Mixing_drinks/yjazHd6a5SQ.mp4 --start_sec 66.81 --end_sec 80.02"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Mixing_drinks/yjazHd6a5SQ.mp4 --start_sec 97.89 --end_sec 155.38"

    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Doing_crunches/CN01Gm2Yc4k.mp4 --start_sec 0.0 --end_sec 5.0"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Doing_crunches/CN01Gm2Yc4k.mp4 --start_sec 5.0 --end_sec 12.2"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Doing_crunches/CN01Gm2Yc4k.mp4 --start_sec 12.2 --end_sec 17.56"

    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Zumba/eI_LceS_qnQ.mp4 --start_sec 0.0 --end_sec 148.21"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Zumba/eI_LceS_qnQ.mp4 --start_sec 0.74 --end_sec 148.21"
    "python run.py --token_wise --randomized_prompt --run_type caption_videos --data_path ../data/ActivityNet_200/validation/Zumba/eI_LceS_qnQ.mp4 --start_sec 5.19 --end_sec 148.21"
        
    # Add more commands here...
)

# Execute each command in the list
for cmd in "${commands[@]}"; do
    echo "Executing command: $cmd"
    eval "$cmd"
done
