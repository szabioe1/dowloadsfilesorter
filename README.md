# File Organizer

This Python script helps you organize files in your "Downloads" folder into specific subfolders based on their types. It categorizes files into videos, images, documents, and "etc" based on their extensions and moves them to the appropriate folders.

## Prerequisites

Before using this script, you need to create the following folders in your "Downloads" directory:

- `videos` to store video files
- `images` to store image files
- `documents` to store document files
- `etc` to store files that do not match any of the specified types

## Supported File Types

The script categorizes files based on their file extensions. Here are the supported file types:

### Video Types

- .mp4
- .mp3
- .avi
- .mkv
- .mov
- .wmv
- .flv
- .m4v
- .ogg
- .wav
- .flac
- .aac
- .wma
- .mpeg
- (You can add more video types as needed)

### Picture Types

- .jpeg
- .jpg
- .png
- .gif
- .bmp
- .tiff
- .webp
- .svg
- .ico
- .heif
- .exif
- .pbm
- .pgm
- .ppm
- (You can add more picture types as needed)

### Document Types

- .pdf
- .doc
- .docx
- .xls
- .xlsx
- .ppt
- .pptx
- .rtf
- .zip
- .rar
- .tar
- .7z
- .txt
- (You can add more document types as needed)

## Usage

1. Create the necessary subfolders (videos, images, documents, etc) within your "Downloads" directory.
2. Copy the Python script (`organize_files.py`) to your desired location.
3. Run the script to organize your files.

**Note:** Make sure to modify the script's paths if your folder structure differs from the default setup.

## How It Works

The script uses the `magic` library to identify file types and categorizes them based on their extensions. If a file's extension matches one of the supported types, it's moved to the corresponding subfolder.

## Author

- Your Name
- Your Email
- Your GitHub Profile

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
