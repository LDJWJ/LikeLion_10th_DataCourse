# Correlation between GDP and Fatal/Recovery Rate
- __DATE__ : 2021.06.21~06.24
- __MEMBERS__ : Nameun @DestinyKim
- __SUBJECT__ : Correlation between GDP and fatal/recovery rate


# GDP 상위 7개 국가와 코로나 국가 간의 상관관계

## 목표 >

###### GDP 금액으로 유추해 보는 코로나에 대처하는 국가들의 상관관계

#### 참조링크

###### 1. 코로나 실시간 상황판 
    * https://coronaboard.kr/
###### 2. GDP 금액과 국가 순위 
    * http://search.daum.net/searchnil_suggest=btn&w=tot&DA=SBC&q=%EC%84%B8%EA%B3%84+gdp+%EC%88%9C%EC%9C%84

## 과정 >

###### 1) GDP 데이터를 추출한다.
###### 2) 코로나 실시간 상황판에서 데이터를 추출한다.
###### 3) 국가이름으로 데이터를 병합하기 위해 코로나 데이터에서 국가 코드를 제거한다.
###### 4) 두 데이터를 병합한다.
###### 5) 병합된 데이터의 GDP금액을 숫자형으로 치환한다.
###### 6) 시각화 한다.

## 결과 >

![result](C:\Users\Jongho\Documents\Practice)

## 해석 및 향후 개선 사항 >

* GDP가 높으면 생활수준이 높아 질병에 대한 대처가 신속할 것으로 예상하여, 완치율이 높을 것이라 생각하였다. 그러나, GDP와 코로나 완치율이 음의 상관관계로 확인된 것으로 미루어, GDP가 높아도 코로나에 대한 대처는 아직까지 미흡한 것으로 보인다.
  
* 데이터 전처리에 있어서 많은 애로사항이 있었다.
    * 국가코드 제거, GDP 금액의 한글 제거 후 숫자로 치환
  
* NaN 값으로 인해 데이터 시각화가 너무 단순하게 처리된 거 같아 데이터를 의미있는 값으로 변경 후 재시각화를 해야겠다.
