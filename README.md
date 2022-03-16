# recruitment-news
(네이버 X 라인) 신입 개발자 모집 공고 자동 알리미

### 프로젝트 소개
아래 두 파일만 참고하시면 됩니다. 
(아래 두개를 제외한 다른 파일들은 공부용으로 올려놓았습니다.)
* DynamicResourceCrawler.py 
* .github/workflows/config.yml 

<br>

**사용 기술 스택**|
---|
Python|
Github Action|
Github Issue|
Selenium|

<br>

깃허브 액션을 통해 지정한 시간에 동적 리소스 크롤러가 자동적으로 동작하여 이슈가 발생하면 메일로 알림이 오게 하였습니다.

<br>

(KST 기준 오후 6시에 한 번 크롤러가 자동적으로 작동하여 데이터를 수집합니다.)
```python
def isDateInRange(created_at):
    suffix_kst = '.000001+09:00' # UTC의 기준시간보다 9시간이 빠르다는 의미이다. KST==UTC+09:00
    created_at = parse(created_at + suffix_kst)  # 이 크롤러가 작동할 서버의 타임 존은 UTC(Github)로 날짜 생성시 KST 타임으로 변환 해주어야함
    yesterday = today - datetime.timedelta(1) # 1 days ago 표현

    return (today > created_at) and (created_at > yesterday) # 대상 게시글은 24시간 전 ~ 작동 시간
```

<br>

#### 크롤러 실행 결과
![라인 네이버 프로그램 실행결과 1개](https://user-images.githubusercontent.com/43543906/155842674-1b7c04cd-50a4-41e5-b26a-6095ce7ed152.png)

<br>

#### 깃허브 이슈 생성
![개발자모집깃허브이슈](https://user-images.githubusercontent.com/43543906/155842741-8646c876-0cd9-4d88-a1ac-403f3a0176db.png)

<br>

----------------------------------------------------------------------------
* [참고 링크] 네이버 커리어 (https://recruit.navercorp.com/naver/job/list/developer)
* [참고 링크] 라인 커리어 (https://careers.linecorp.com/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia&fi=Server-side)
* [참고 링크] 깃허브 액션 레퍼런스 (https://github.com/features/actions)
* [참고링크] 셀레니움 기본 사용법 (https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/)

<br>

> 경희대학교 소프트웨어융합학과 구현서 [mnb9139@khu.ac.kr]

