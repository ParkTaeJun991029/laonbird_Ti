# laonbird_Ti

# 내가 했던 업무
  1. 필요한 데이터 라벨링
  2. helmet,harness,fire,fall detection

## 필요한 데이터 라벨링
  - 사용한 툴은: labelImg
  - labelImg 특징은 class txt가 따로 있다 그리고 단축키가 편리하다
    
## helmet,harness,fire,fall detection
  - 첫번째 방법: helmet,harness,fire,fall을 classification으로만 detecet 하는 경우 이 경우 yolov8를 사용함
  - 두번째 방법: helmet,harness,fire는 classification으로 fall은 bounding box의 width-height를 이용하여 detect
  - 세번째 방법: helmet,harness,fire는 classification으로 fall은 pose estimation으로 활용하여 각 관절의 keypoint값을 gcn을 통하여 넘어지는 것을 예측
  - 네번째 방법: 첫번째 방법과 두번째 방법을 같이 사용
