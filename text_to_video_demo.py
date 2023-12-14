
# refer to (https://github.com/Picsart-AI-Research/Text2Video-Zero#text-to-video)

import os
import torch
from model import Model

# from hf_utils import get_model_list

IS_DEBUG = True
save_tag = "debug_" if IS_DEBUG else ""


model = Model(device = "cuda", dtype = torch.float16)


prompt = "A horse galloping on a street"
prompt = "A man sits on the chair then stands up"
params = {"t0": 44, "t1": 47 , "motion_field_strength_x" : 12, "motion_field_strength_y" : 12, "video_length": 8}

out_dir = "./txt2video_output/"
os.makedirs(out_dir,exist_ok=True)
out_path = os.path.join(out_dir,f"{save_tag}{prompt.replace(' ','_')}.mp4")
fps =  4

# model_list = get_model_list()
# for idx, name in enumerate(model_list):
#   print(idx, name)
# idx = int(input("Select the model by the listed number: ")) # select the model of your choice
# model.process_text2video(prompt, model_name = model_list[idx], fps = fps, path = out_path, **params)

model_name = "/home/zhaizhichao/.cache/huggingface/hub/models--stabilityai--stable-diffusion-2-1-base/snapshots/5ede9e4bf3e3fd1cb0ef2f7a3fff13ee514fdf06"
model.process_text2video(prompt, model_name, fps = fps, path = out_path, **params)
