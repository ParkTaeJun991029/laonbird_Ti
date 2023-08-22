import os

def get_unique_class_labels_from_yolo_txt_files(folder_path):
    class_labels = set()
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    for txt_file in txt_files:
        with open(os.path.join(folder_path, txt_file), "r") as f:
            lines = f.readlines()

        for line in lines:
            label = line.strip().split(" ")[0]
            class_labels.add(label)

    return class_labels

if __name__ == "__main__":
    folder_path = "/home/developer/ptj/method1_test/task1&2_train"  # 실제 폴더 경로로 변경해야 합니다.
    unique_class_labels = get_unique_class_labels_from_yolo_txt_files(folder_path)
    print("Unique class labels in YOLO format txt files:", unique_class_labels)
