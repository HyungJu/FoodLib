# FoodLib

sudo pip3 install -r require.txt

import hyungju.food

hyungju.food.GetFood("학교주소",모드)

모드  : 0 -> 급식,칼로리 (리스트로)  
     : 1 -> 급식만  (리스트로)
	 : 2 -> 칼로리만  (리스트로)


예: hyungju.food.GetFood("http://yongma.ms.kr/tablemenu/menu.do",2)

리턴 : ['768']

예 : hyungju.food.GetFood("http://yongma.ms.kr/tablemenu/menu.do",0)

리턴 : ['무농약차수수밥', '육개장', '두부구이/양념장', '명엽채볶음', '포기김치', '바나나', '768']

예 : hyungju.food.GetFood("http://yongma.ms.kr/tablemenu/menu.do",)

리턴 : ['무농약차수수밥', '육개장', '두부구이/양념장', '명엽채볶음', '포기김치', '바나나']

