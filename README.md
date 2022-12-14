

# Kor_patent_electra
한국특허정보원의 KorPatELECTRA를 사용하여 문헌 유사도 계산, 특허 생명주기 및 원천성 분석을 수행하였습니다.






진행과정은 다음과 같습니다.

1) 특허 용어 및 전체 프로세스 확인 
전체적인 데이터의 품질 확인 및 프로젝트의 진행방향을 파악하기 위해서는 해당 과정이 필수라고 판단하였습니다.
![image](https://user-images.githubusercontent.com/73458088/207750778-06f0ab70-b3d3-4bee-be0b-4e677816ec24.png)

2) 특허 데이터 크롤링 - 기본 30만개 > 청구항/요약 11만개 > 최종 2016~2022 3만개

저희가 선정한 특허 (블록체인 및 머신러닝 기반으로 한 프랜차이즈 유통)의 CPC 번호의 메인 그룹까지 같은 특허를 크롤링하고(30만개), 서브 그룹까지 같은 특허를 다시 분류한 후, 그 분류한 서브 그룹의 청구항 및 요약을 크롤링하였습니다. (11만개) 여기에 저희는 2016~2022년 사이의 데이터만 유의미하다고 판단하였기에, 최종적으로 3만개를 추출해내었습니다.

3) 추출한 텍스트 데이터(요약 및 청구항)를 활용하여 선정한 특허와의 문헌 유사도를 분석한 후, 문헌 유사도가 75 % 이상인 특허만을 다시 추출하였습니다.

해당 과정은 다음과 같습니다.

![image](https://user-images.githubusercontent.com/73458088/207750927-43d11783-87ad-4d9b-9b33-a377deb58928.png)


4) 추출한 특허들을 활용하여 S-curve 및 기술혁신 주기 그래프를 그려보았으며, TCT 지수 또한 계산하였습니다.

S-curve 같은 경우에는 Logistic Model과 Gompertz 모델을 사용하였으며, 해당 모델의 지수 및 Performance는 다음과 같습니다.

![image](https://user-images.githubusercontent.com/73458088/207751394-d1c39553-579d-4108-8c57-066fed01ac40.png)



<S-curve의 Graph>

![image](https://user-images.githubusercontent.com/73458088/207751482-e12c9d71-0560-45c9-9bfe-7a18c13c2d70.png)


  
  
<기술혁신 주기 Graph>

![image](https://user-images.githubusercontent.com/73458088/207751506-92de150c-3608-440f-880d-2d4a0859918d.png)

  
  

<TCT 지수 값>

![image](https://user-images.githubusercontent.com/73458088/207751524-e22e8453-b63d-43c6-b375-eabcc19ffe2c.png)


선택한 특허의 TCT 값이 작으므로, 최근 선행 기술에 기반을 두고 있다고 추론하였습니다. TCT 값이 작으므로, 앞서 예측한 대로 2016 ~ 2022 년 사이의 기술을 기반으로, 상세 분석을 통해 해당 특허 기술의 원천성 분석을 수행하였습니다


5) 최종 원천성 분석 및 기술 수명 주기 분석

기술 수명 주기 분석에서는 S-curve 및 기술혁신 주기 그래프를 그려보았을 때, 다음과 같이 판단하였습니다.
- 기술순환주기(TCT 분석)에서는 선행 기술이 매우 가깝다고 추론
- S-curve에서는 2030년(Logistic), 2050년(Gompertz)까지
해당 특허 및 기술이 성장기에 있을 것으로 판단
- 기술혁신주기에서는 계속해서 우상향으로 특허 출원인 수 및 특허
수가 증가

원천성 분석 같은 경우에는 피인용/인용 관계를 도식화 해보았고, TCT 값을 기반으로 도식화 해보니 다음과 같았습니다. 도식화한 인용 / 피인용 관계를 통해서 원천 기술이 무엇인지 추론할 수 있습니다.

![image](https://user-images.githubusercontent.com/73458088/207751971-e29d62b1-ca4e-4d5a-ad2e-6e00b85311f6.png)






# 폴더 정리

- Crawling 폴더에는 전체 30만건, 11만건 의 크롤링 코드가 존재합니다. (Selenium X)
- Sentence_Similarity에서는 선정한 특허와 다른 특허들의 청구항 + 요약의 텍스트 유사도를 계산하였습니다
- Data_analysis 폴더에서는 데이터 전처리, EDA 및 S-curve 및 기술 혁신 주기 그래프를 그렸습니다.
- Visulization 폴더에서는 선정한 특허를 웹페이지에 띄울려고 시도하였습니다. 시도는 성공하였으나, 발표에서 시간상의 이유로 생략하였습니다. (Bootstrap 기본 template을 사용하였으며, 해당 template은 https://startbootstrap.com/theme/sb-admin-2 에서 다운 받으실 수 있습니다. (github 최대 input 용량 제한으로 인해서 폴더에는 넣지 못했습니다)






