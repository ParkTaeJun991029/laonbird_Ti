import os

def class_change(dataset_folder):
    # 데이터셋 폴더 내의 모든 텍스트 파일에 대해
    for root, dirs, files in os.walk(dataset_folder):
        for filename in files:
            if filename.endswith('.txt'):
                filepath = os.path.join(root, filename)
                
                # 텍스트 파일 열기
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                
                # 클래스 레이블 수정
                modified_lines = []
                for line in lines:
                    elements = line.strip().split(' ')
                    class_label = elements[0]
                    
                    # 클래스 레이블이 0인 경우 1로 수정
                    if class_label == '80':
                        elements[0] = '0'
                    

                          
                    
                    modified_line = ' '.join(elements)
                    modified_lines.append(modified_line)
                
                # 수정된 내용으로 텍스트 파일 덮어쓰기
                with open(filepath, 'w') as file:
                    file.write('\n'.join(modified_lines))

def main():
    import sys
    args = sys.argv[1:]
    for arg in args:
        class_change(arg)

if __name__ == '__main__':
    main()
