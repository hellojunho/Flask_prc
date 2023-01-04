# Flask와 Mysql 연동하는 폴더

## csv, json데이터를 Mysql에 Import하기
`Mysql`을 실행시키고, 원하는 데이터베이스로 들어간다.  
다음에는 해당 스키마에서 마우스 우클릭을 하면 `Table Data Import Wizard`가 있는데, 이 버튼을 클릭한다.    
![image](https://user-images.githubusercontent.com/104587537/204124480-9ff5b235-cec7-4fa7-bca5-2e711283d431.png)  
그 다음에 내가 mysql에 넣고싶은 json 혹은 csv 파일의 경로를 입력하고 NEXT를 누른다.  
![image](https://user-images.githubusercontent.com/104587537/204124502-21b49959-84bd-4ab4-8544-a9fe2efaeb0a.png)  
그리고 새로운 테이블을 생성하여 파일을 삽입할 것인지, 기존에 내가 만든 테이블에 삽입할 것인지 정한다.  
![image](https://user-images.githubusercontent.com/104587537/204124562-43868b38-851d-4674-bb46-364b6454a5f6.png)    
이 다음에는 내가 삽입하려는 파일의 칼럼들의 자료형을 확인하고 완료하면 정상적으로 mysql에 들어갈 것이다.  

---

## vsCode와 Mysql 연동
vsCode에는 `마켓플레이스` 배너가 있다.   
![image](https://user-images.githubusercontent.com/104587537/204124168-9c6d082a-55ef-4105-a2ca-34359411eb40.png) <-- 이렇게 생겼다.  

그러면 ![image](https://user-images.githubusercontent.com/104587537/204124202-cd47f93b-73b3-4eaf-9853-bc8604f7f633.png) 이렇게 생긴게 있을텐데 이걸 설치하자.

설치를 하고나면, ![image](https://user-images.githubusercontent.com/104587537/204124228-007aa31d-4aa0-4e99-8819-cea3efbc53da.png) 이렇게 생긴 배너가 생성이 되었을텐데, 자신의 Mysql의 Database와 맞는 이름, 포트 등을 설정하면 이제 vsCode에서도 Mysql의 스키마와 테이블들을 볼 수 있다.  

---


## 갑자기 MYSQL에서 오류가 발생한다면?
갑자기 `mysql unable to connect to localhost`이라는 문구가 나오며 로컬호스트에 연결할 수 없다고 알림창이 떴다.  
어떻게 해야할까?    
![image](https://user-images.githubusercontent.com/104587537/210555184-9bab796c-43f0-4f43-b73d-278151d51c50.png)  

[해결방법]  
1. `제어판>시스템및보안>관리도구>서비스`로 들어간다.  
![image](https://user-images.githubusercontent.com/104587537/210555472-a8a6bd22-6443-4ab1-93e7-f762fe25cb34.png)   
![image](https://user-images.githubusercontent.com/104587537/210555626-2fc223f0-7d5d-4e29-bd62-947d47a4ea31.png)  
2. `서비스`에서 `MYSQL`을 찾는다.  
![image](https://user-images.githubusercontent.com/104587537/210555757-d36740d8-25f5-4058-8710-25b2a1a85cb1.png)  
3. `다시시작`을 누르고, MYSQL을 실행시키면 정상적으로 동작한다.  