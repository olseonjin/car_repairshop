🚗 Car Repair Shop 프로젝트
공공데이터를 활용하여 전국의 자동차 정비소 정보를 조회, 관리할 수 있는 웹 애플리케이션입니다.
사용자는 지도 기반으로 정비소를 검색할 수 있으며, 관리자는 정비소 신청 내역을 검토하고 승인/거절할 수 있습니다.

📌 주요 기능
사용자 기능
로그인 / 회원가입
자동차 정비소 정보 검색 (지도 기반)
정비소 리뷰 작성
정비소 등록 요청
관리자 기능
관리자 인증을 통한 접근
정비소 리스트 관리 (등록/수정/삭제)
정비소 등록 요청 승인/거절
공공데이터 API 연동 동기화
🛠 기술 스택
Backend: Spring Boot, MyBatis
Frontend: JSP, JSTL, Bootstrap 5
Database: MySQL
API 연동: 공공데이터포털 자동차정비업체 API
Build Tool: Gradle
📁 프로젝트 구조
car_repair_shop/
├── build.gradle
├── src/
│   ├── main/
│   │   ├── java/com/boot/controller/     # 컨트롤러
│   │   ├── java/com/boot/service/        # 서비스 로직
│   │   ├── java/com/boot/dao/            # DAO 인터페이스
│   │   ├── resources/                    # 설정 및 Mapper
│   │   └── webapp/WEB-INF/views/         # JSP View
├── mybatis-config.xml
└── application.properties
⚙️ 실행 방법
MySQL에 데이터베이스 atom 생성
테이블 생성 SQL 실행 (repair_shop, user, review, repair_shop_request)
application.properties에서 DB 계정 정보 확인
./gradlew bootRun 또는 IDE로 실행
브라우저에서 http://localhost:8485/main 접속
🧩 공공데이터 API 정보
API명: 자동차정비업체 API
제공처: 공공데이터포털 (https://www.data.go.kr)
🙋 팀원 기여
기획 및 발표: 권준우 외 3인
백엔드 개발: Spring Boot 기반 CRUD 및 동기화 구현
프론트엔드 구성: JSP + Bootstrap 디자인 구성
