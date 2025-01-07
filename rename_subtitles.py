import os
import shutil

# Subtitles should be placed in the 'sub' folder

def rename_subtitles(video_dir):
    # Supported video file extensions
    video_extensions = ['.mkv', '.mp4', '.avi']
    # Supported subtitle file extensions
    subtitle_extensions = ['.srt', '.smi', '.ass']
    
    # Get a list of video files
    video_files = sorted([f for f in os.listdir(video_dir) if os.path.splitext(f)[1].lower() in video_extensions])
    
    # Get a list of subtitle files
    subtitle_dir = os.path.join(video_dir, 'sub')
    subtitle_files = sorted([f for f in os.listdir(subtitle_dir) if os.path.splitext(f)[1].lower() in subtitle_extensions])
    
    # Raise an error if the number of video and subtitle files does not match
    if len(video_files) != len(subtitle_files):
        raise ValueError("The number of video files and subtitle files does not match.")
    
    # Create the 'subfix' folder if it does not exist
    subfix_dir = os.path.join(video_dir, 'subfix')
    if not os.path.exists(subfix_dir):
        os.makedirs(subfix_dir)
    
    # Rename and save subtitle files
    for video_file, subtitle_file in zip(video_files, subtitle_files):
        subtitle_extension = os.path.splitext(subtitle_file)[1]
        new_subtitle_name = os.path.splitext(video_file)[0] + subtitle_extension
        old_subtitle_path = os.path.join(subtitle_dir, subtitle_file)
        new_subtitle_path = os.path.join(subfix_dir, new_subtitle_name)
        shutil.copy2(old_subtitle_path, new_subtitle_path)
    
    print("Subtitle files have been successfully renamed and copied.")

if __name__ == "__main__":
    video_directory = input("Enter the directory path containing the video files: ")
    if not os.path.isdir(video_directory):
        print("Please enter a valid directory path.")
    else:
        rename_subtitles(video_directory)