import os
import shutil

# Define the directory to organize
directory = "path/to/your/directory"  # Replace with your directory path

# Define file types and their corresponding folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".dmg"],
    "Others": []  # For files that don't match any category
}

def create_folders():
    """Create folders for each file type if they don't already exist."""
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

def organize_files():
    """Organize files into their respective folders."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find the appropriate folder for the file
        moved = False
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, folder_name)
                shutil.move(file_path, destination_folder)
                print(f"Moved {filename} to {folder_name}")
                moved = True
                break

        # If the file type is not recognized, move it to the "Others" folder
        if not moved:
            destination_folder = os.path.join(directory, "Others")
            shutil.move(file_path, destination_folder)
            print(f"Moved {filename} to Others")

def main():
    print("Starting file organization...")
    create_folders()
    organize_files()
    print("File organization complete!")

if __name__ == "__main__":
    main()
