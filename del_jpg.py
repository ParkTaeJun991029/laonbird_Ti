import os

# 폴더 경로 설정
txt_folder = '/home/developer/ptj/output_label'
jpg_folder = '/home/developer/ptj/output_img'




# jpg 폴더의 파일 리스트 가져오기
jpg_files = os.listdir(jpg_folder)

# txt 폴더의 파일 리스트 가져오기
txt_files = os.listdir(txt_folder)

# jpg 파일에는 있지만 txt 파일에는 없는 파일들 삭제
for file_name in jpg_files:
    if file_name[:-4] + '.txt' not in txt_files:
        file_path = os.path.join(jpg_folder, file_name)
        os.remove(file_path)
        print(f'{file_name} 삭제 완료')
