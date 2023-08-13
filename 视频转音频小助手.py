import os
from tqdm import tqdm
from moviepy.video.io.VideoFileClip import VideoFileClip

print("这是一个可以扫描当前目录所有的MP4格式（视频）文件，并将其转换为WAV格式（音频）文件的工具")
print("当然，你也可以更改当前目录为别的工作目录")

input("请按任意键继续")

current_dir = os.getcwd()
print(f"当前工作目录是{current_dir}")
choice_dir = input("请问你是否需要更改工作目录？\n如果想要保持当前目录，请输入“keepit”。\n否则，请在下面的步骤中输入新的目标工作目录：")
if choice_dir == "keepit":
    print("好的，已保持当前工作目录")
else:
    new_dir = input("请输入新的工作目录")
    os.chdir(new_dir)
    current_dir = new_dir
    print(f"已更改，当前工作目录是{current_dir}")

input("已确认工作目录，下面即将开始扫描所有MP4文件\n请按任意键继续")

file_list = os.listdir(current_dir)


mp4_files = [file for file in file_list if file.endswith('.mp4')]

if not mp4_files:
    input("没有找到MP4文件，按任意键退出")
    exit()

print("以下是找到的所有MP4文件：")
for mp4_file in mp4_files:
    print(mp4_file)

input("下面即将进行MP4转WAV，请按任意键继续")

for mp4_file in tqdm(mp4_files, desc="提取音频进度", unit="文件"):
    video_path = os.path.join(current_dir, mp4_file)
    
    video_clip = VideoFileClip(video_path)
    
    audio_clip = video_clip.audio
    
    audio_output_path = os.path.splitext(mp4_file)[0] + '_audio.wav'
    audio_output_path = os.path.join(current_dir, audio_output_path)
    
    audio_clip.write_audiofile(audio_output_path)
    
    video_clip.close()
    audio_clip.close()
    
    print(f"提取音频完成：{audio_output_path}")

input("有任何问题请向我反馈\n按任意键结束程序")
