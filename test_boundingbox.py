import cv2

def draw_bounding_boxes(image_path, txt_file, output_image_path):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 바운딩 박스 정보를 읽어올 TXT 파일
    with open(txt_file, 'r') as f:
        lines = f.read().strip().split('\n')

    # 바운딩 박스 그리기
    for line in lines:
        class_id, x_center, y_center, width, height = line.split(' ')

        image_height, image_width, _ = image.shape
        x_min = int((float(x_center) - float(width)/ 2) * image_width)
        y_min = int((float(y_center) - float(height) / 2) * image_height)
        x_max = int((float(x_center) + float(width)/ 2) * image_width)
        y_max = int((float(y_center) + float(height) / 2) * image_height)

        # 클래스별 색상 설정
        class_id = class_id
        #class_colors = [(0, 255, 0), (255, 0, 0)]  # 클래스별 색상 지정
        #color = class_colors[class_id]

        # 바운딩 박스 그리기
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0,0,255), 2)
        cv2.putText(image, str(class_id) , (x_min,y_min-3), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    # 바운딩 박스가 그려진 이미지 저장
    cv2.imwrite(output_image_path, image)
    print(f"Drawn bounding boxes saved to: {output_image_path}")
    print(x_min)
    print(x_max)
    print(y_min)
    print(y_max)
# 이미지 파일 경로
image_file = '/home/developer/ptj/ai_pun/2D Bounding Box/test/images/AGS_DA_00C_BA_22090201_000021.jpg'

# 바운딩 박스 정보를 포함한 TXT 파일 경로
txt_file = '/home/developer/ptj/ai_pun/2D_yolo_format/test/AGS_DA_00C_BA_22090201_000021_yolo.txt'

# 바운딩 박스가 그려진 이미지 저장 경로
output_image_path = 'output_image.jpg'

# 이미지에 바운딩 박스 그리기 및 저장
draw_bounding_boxes(image_file, txt_file, output_image_path)
