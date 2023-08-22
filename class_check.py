import os

def extract_class_labels_from_txt_files(root_folder):
    class_labels = set()
    
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        class_label = line.strip().split()[0]
                        class_labels.add(class_label)
                        
    return class_labels

# 큰 폴더를 지정해주세요.
root_folder = '/home/developer/ptj/class_change'

class_labels = extract_class_labels_from_txt_files(root_folder)
print("중복을 제거한 class label들:")
print(class_labels)
