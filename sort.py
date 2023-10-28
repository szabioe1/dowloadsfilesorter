import os
import magic
import shutil

video_types = [
    ".mp4",
    ".mp3",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".m4v",
    ".ogg",
    ".wav",
    ".flac",
    ".aac",
    ".wma",
    ".mpeg"
]


picture_types = [
    ".jpeg",
    ".jpg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
    ".svg",
    ".ico",
    ".heif",
    ".exif",
    ".pbm",
    ".pgm",
    ".ppm"
]

document_types = [
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".rtf",
    ".zip",
    ".rar",
    ".tar",
    ".7z",
    ".txt"
]



def check_file_types(folder_path):
    # Create a Magic object to identify file types
    mime = magic.Magic()

    # List all files in the specified folder
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        ## Check if the file exists and is a regular file
        if os.path.isfile(file_path):
            file_type = mime.from_file(file_path)

            # Extract the file extension and check if it's in the video_types list
            file_extension = os.path.splitext(file)[1].lower()
            # Puts the file into /videos if its a video
            if file_extension in video_types:
                move_file(file_path, videos_folder)
            # Puts the file into /images if its an image
            elif file_extension in picture_types:
                move_file(file_path, images_folder)
            # Puts the file into /documents if its a document
            elif file_extension in document_types:
                move_file(file_path, documents_folder)
            elif file_extension not in video_types and file_extension not in picture_types and file_extension not in document_types:
                move_file(file_path, etc_folder)

def move_file(file_path, target_folder):
    # Get the filename from the full path
    filename = os.path.basename(file_path)
    target_path = os.path.join(target_folder, filename)
    
    # Move the file to the target folder
    shutil.move(file_path, target_path)
    print(f"{filename} moved to {target_folder}")

if __name__ == "__main__":
    videos_folder = os.path.expanduser("~") + "/Downloads/videos"
    downloads_folder = os.path.expanduser("~") + "/Downloads"
    images_folder = os.path.expanduser("~") + "/Downloads/images"
    documents_folder = os.path.expanduser("~") + "/Downloads/documents"
    etc_folder = os.path.expanduser("~") + "/Downloads/etc"
    check_file_types(downloads_folder)
