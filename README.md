# 1**팀 얼굴 추출 방법 및 구현 보고서**

**지도 교수 : 심재창**

팀장 : 이영훈

팀원 : 이승구, 민규동

------

## 개요

**대표적으로 쓰이는 3가지 얼굴 객체 검출 모델을 활용하여, 같은 동영상을 처리하는데에 소요되는 시간 차이를 비교 분석하는 실험을 진행하였습니다. GPU의 실험환경은 모두 Nvidia GTX 1060 3GB에서 실험을 진행하였습니다. 비교 분석 하고자 하는 얼굴 객체 모델은 다음과 같습니다.**

------

### 1. Haar cascade

> Haar feature-based cascade classifiers를 사용한 객체 감지는 Paul Viola와 Michael Jones가 2001년에 "Rapid Object Detection using a Boosted Cascade of Simple Features" 논문에서 제안한 효과적인 객체 감지 방법입니다.

### **2. Dlib**

> Dlib는 OpenCV와 유사하게 이미지 프로세싱 커뮤니티에서 폭넓게 도입하고 있는 강력한 라이브러리입니다. 연구자는 주로 이 라이브러리의 얼굴 탐지(detection)와 정렬(alignment) 모듈을 사용합니다. 이를 넘어 dlib는 즉시 사용가능한 강력한 얼굴인식(recognition) 모듈도 제공합니다.

### **3. Mtcnn**

> MTCNN은 3개의 neural network(P-Net, R-Net, O-Net)로 이루어져 있습니다. 이때 각 net에서 face classification과 bbox regression, face landmark localization 과정을 진행하면서 동시에 학습시키는 방식(joint learning )을 사용하였습니다.

- 비교 분석 하고자 하는 모델은 Haar Cascade, Dlib, Mtcnn 을 활용하여 비교 실험을 진행하였습니다.
- Harr와 Dlib, 두 모델은 머신러닝 기반 모델이고 Mtcnn은 딥러닝 기반 모델로 Mtcnn이 오래 걸리리라 예상히고 실험을 진행하였습니다.
- 소스코드 내에서 time 모듈을 활용하여 시간을 측정하였습니다.
---
|  | 실행 시간 | 에러율 | 비고 |
| --- | --- | --- | --- |
| Haar Cascade | 71s | 16.00% | 거짓양성 검출, 민규동 미검출 |
| Dlib | 78s | 1% 미만 |  |
| Mtcnn | 397s | 1% 미만 | 민규동 미검출 |

---
## 결론
Mtcnn이 제일 정확하다고 예상하였지만 Haar cascade와 Mtcnn은 턱선이 뚜렷하게 보이지 않는 얼굴 객체는 검출되지 않았습니다. 이는 학습데이터에 턱선이 안보이는 데이터가 적음으로 예상됩니다. 
거짓양성 검출, 민규동 미검출된 점과 실행시간, 에러율을 고려하였을 때 위 실험환경에서는 Dlib이 가장 좋은 결과를 보여주었습니다.




