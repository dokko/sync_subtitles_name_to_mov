# Subtitle Renaming Tool

[![Forks](https://img.shields.io/github/forks/dokko/sync_subtitles_name_to_mov.svg)](https://github.com/dokko/sync_subtitles_name_to_mov/network/members)
[![Stargazers](https://img.shields.io/github/stars/dokko/sync_subtitles_name_to_mov.svg)](https://github.com/dokko/sync_subtitles_name_to_mov/stargazers)
[![Issues](https://img.shields.io/github/issues/dokko/sync_subtitles_name_to_mov.svg)](https://github.com/dokko/sync_subtitles_name_to_mov/issues)
[![License](https://img.shields.io/github/license/dokko/sync_subtitles_name_to_mov.svg)](https://github.com/dokko/sync_subtitles_name_to_mov/blob/main/LICENSE)

This script renames subtitle files to match the corresponding video file names and saves them in a separate folder named `subfix`.

## Features

- Automatically matches video files and subtitle files in a given directory.
- Renames subtitle files to match the names of their corresponding video files.
- Copies the renamed subtitle files to a new folder named `subfix` without modifying the original files.

## Requirements

- **Python 3.x**
- **`sub` folder** within the video directory containing the subtitle files.

## Supported File Formats

- **Video file extensions**: `.mkv`, `.mp4`, `.avi`
- **Subtitle file extensions**: `.srt`, `.smi`, `.ass`

## How It Works

1. Place your video files in a folder.
2. Create a `sub` folder inside the video directory and place the corresponding subtitle files in it.
3. Run the script, and it will rename the subtitle files to match the names of the video files.
4. The renamed subtitle files will be copied to a new folder named `subfix`.

### Example Folder Structure

#### Before running the script:

/video_directory
├── video1.mkv
├── video2.mp4
├── sub/
├── subtitle1.srt
├── subtitle2.smi

#### After running the script:

/video_directory
├── video1.mkv
├── video2.mp4
├── sub/
├── subtitle1.srt
├── subtitle2.smi
├── subfix/
├── video1.srt
├── video2.smi

## Usage Instructions

1. Clone or download the script to your local machine.
2. Run the script using Python:

   ```bash
   python sync_subtitles_name_to_mov.py
   ```

3. When prompted, enter the directory path where your video files are located.

Error Handling
• If the number of video files and subtitle files do not match, the script will raise the following error:

```
ValueError: The number of video files and subtitle files does not match.
```

• Ensure that the directory paths provided are valid and accessible.

## Notes

• The script does not modify the original subtitle files in the sub folder. Instead, it creates copies in the subfix folder with the new names.

• Ensure that the subtitle files correspond to the video files in the same order, as the script matches them based on sorted file lists.

## License

This script is free to use and modify under the MIT License. Feel free to adapt it to your needs.
