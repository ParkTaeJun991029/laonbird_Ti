import os

def delete_empty_txt_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                if not content:
                    os.remove(file_path)
                    print(f"Deleted empty file: {file_path}")

if __name__ == "__main__":
    folder_path = "/home/developer/ptj/coco_human"  # 대상 폴더의 경로를 지정해주세요.
    delete_empty_txt_files(folder_path)
