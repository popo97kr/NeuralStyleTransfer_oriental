# Neural Style Transfer using CycleGAN: from photo to oriental paintings

2020년 1학기 고려대학교 컴퓨터학과 졸업프로젝트  (**고려대학교 캡스톤 경진대회 우수상 수상**)

## 프로젝트 명

CycleGAN을 사용한 Neural Style Transfer: 수묵화를 중심으로

## 프로젝트 목적

선과 여백을 중요시하는 동양화의 특성을 살려 실사 사진을 동양화로 변환시킬 수 있는 cycleGAN 모델을 구현한다. 

## 파일 설명

- cyclegan_final.ipynb : code for constructing and training cyclegan
  - library used : **Keras**

- generator_final.json : saved model structure of cyclegan
- generator_final.h5 : saved model weights of cyclegan
- django : website files for photo-translation-to-oriental service
  - framework used : **Django**

## Training Process

- epoch 0
  
  ![epoch0batch0](https://user-images.githubusercontent.com/45965766/89705383-e4321d00-d997-11ea-9eb5-b3a48c5b4e8e.png)

- epoch 20

  ![epoch10batch0](https://user-images.githubusercontent.com/45965766/89705398-02981880-d998-11ea-96aa-4d226cc448f0.png)

- epoch 50

  ![epoch50batch450](https://user-images.githubusercontent.com/45965766/89705422-49860e00-d998-11ea-9059-e78dc5632697.png)

- epoch 100

  ![epoch100batch150](https://user-images.githubusercontent.com/45965766/89705536-40497100-d999-11ea-883f-ff6b368b2b3a.png)

- epoch 200

  ![epoch198batch150](https://user-images.githubusercontent.com/45965766/89705474-a4b80080-d998-11ea-8387-eec03bb838e9.png)
  ![epoch199batch0](https://user-images.githubusercontent.com/45965766/89705513-feb8c600-d998-11ea-8e3b-f6f41b2ca01b.png)

### Website

- 최종적으로 누구나 자신의 사진를 집어넣어 동양화로 변환된 이미지를 생성받을 수 있도록 image translation 웹사이트를 구축하였다.
- Framework used: **Django**

Website Preview)
![KakaoTalk_20200808_153806988](https://user-images.githubusercontent.com/45965766/89705729-72a79e00-d99a-11ea-97c5-55d410bb6fc8.png)

