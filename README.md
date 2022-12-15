

# Kor_patent_electra
한국특허정보원의 KorPatELECTRA를 사용하여 문헌 유사도 계산, 특허 생명주기 및 원천성 분석을 수행하였습니다.






진행과정은 다음과 같습니다.

1) 특허 용어 및 전체 프로세스 확인 
전체적인 데이터의 품질 확인 및 프로젝트의 진행방향을 파악하기 위해서는 해당 과정이 필수라고 판단하였습니다.
![image](https://user-images.githubusercontent.com/73458088/207750778-06f0ab70-b3d3-4bee-be0b-4e677816ec24.png)

2) 특허 데이터 크롤링 - 기본 30만개 > 청구항/요약 11만개 > 최종 2016~2022 3만개

저희가 선정한 특허 (블록체인 및 머신러닝 기반으로 한 프랜차이즈 유통)의 CPC 번호의 메인 그룹까지 같은 특허를 크롤링하고(30만개), 서브 그룹까지 같은 특허를 다시 분류한 후, 그 분류한 서브 그룹의 청구항 및 요약을 크롤링하였습니다. (11만개) 여기에 저희는 2016~2022년 사이의 데이터만 유의미하다고 판단하였기에, 최종적으로 3만개를 추출해내었습니다.

3) 추출한 텍스트 데이터(요약 및 청구항)를 활용하여 선정한 특허와의 문헌 유사도를 분석한 후, 문헌 유사도가 75 % 이상인 특허만을 다시 추출하였습니다.
![image](https://user-images.githubusercontent.com/73458088/207750927-43d11783-87ad-4d9b-9b33-a377deb58928.png)


