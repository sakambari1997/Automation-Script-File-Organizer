import os
import shutil

# --------- File type mapping ---------
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c"]
}

# --------- Get file category ---------
def get_category(file_ext):
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

# --------- Organize Files ---------
def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ The folder path does not exist.")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            category = get_category(ext)

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            new_path = os.path.join(category_folder, file_name)
            shutil.move(file_path, new_path)

            print(f"✅ Moved: {file_name} --> {category}/")

    print("\n🎉 Folder organization complete!")

# --------- Run Script ---------
if __name__ == "__main__":
    target_folder = input("Enter the folder path to organize: ").strip()
    organize_folder(target_folder)
