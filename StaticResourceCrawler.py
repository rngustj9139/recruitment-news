# import requests # 지정한 url을 호출하고 돌려받은 응답을 담기 위함
# from bs4 import BeautifulSoup # Beautiful Soup은 HTML 구문 분석하기 위함
# from github import Github, Issue # github에 issue를 생성하기 위함
# import datetime # 현재 시각과 시간 포멧팅을 하기 위함
# from pytz import timezone # 타임 존을 사용하기 위함
# from dateutil.parser import parse # 문자열 날짜를 date로 변환하기 위함
# import os # 환경 변수를 사용하기 위함
#
# kst = timezone('Asia/Seoul')
# today = datetime.datetime.now(kst)
# # print(today)
#
# def isDateInRange(created_at):
#     suffix_kst = '.000001+09:00' # (UTC의 기준시간보다 9시간이 빠르다는 의미이다. KST=UTC+09:00)
#     created_at = parse(created_at + suffix_kst) # (이 크롤러가 작동할 서버의 타임 존은 UTC(Github)로 날짜 생성시 KST 타임으로 변환 해주어야함)
#     yesterday = today - datetime.timedelta(1) # 1 days ago 표현
#
#     return (today > created_at) and (created_at > yesterday) # 대상은 24시간 전 ~ 작동 시간
#
# # naver career 파싱 시작
# site = "https://recruit.navercorp.com/naver/job/list/developer"
# res = requests.get(site)   # naver career 사이트를 호출하여 응답을 받아온다.
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')   # bs4를 이용하여 응답 결과를 html tag 타입으로 파싱한다.
# print(soup)
# title_list = soup.select(".list_con > .crd_tit")   # 게시글 리스트를 추출(list 형식)
# print(title_list)
# date_list = soup.select(".crd_date")
# tag_list = soup.select(".tag_area")
# issueBody = ''
#
# for x, y, z in zip(title_list, date_list, tag_list):
#     title = x.text # 태그 안의 텍스트 요소를 가져온다
#     published_at = y.text # 태그 안의 텍스트 요소를 가져온다.
#     published_at = published_at[0:10].replace('.', '-') + " 00:00:00" # 글 등록 시간은 가져오기 불가능하기 때문에 0시(자정)라고 가정
#     item = published_at + ' ' + str(title).replace("\n", "").replace(' ', '').strip() + '<br/>\n'
#     tags = soup.select("z > a")
#
#     allTags = []
#     for tag in tags:
#         allTags += tag.text
#
#     if('경력' not in allTags and isDateInRange(published_at)):
#         issueBody += item
#     else:
#         print('[filtered]', item)
#
# print('-----------------------------------------------------------')
#
# issueTitle = "신입 모집 글 모음(%s)" %(today.strftime("%Y년 %m월 %d일 %H시"))
# print(issueTitle)
# print(issueBody)
#
# #print(os.environ)
# GITHUB_TOKEN = os.environ['TOKEN_GITHUB'] # 시스템 환경변수에 깃허브 토큰 저장되어있음
# REPO_NAME = "recruitment-news"
# repo = Github(GITHUB_TOKEN).get_user().get_repo(REPO_NAME)
# if issueBody != '' and REPO_NAME == "recruitment-news":
#     res = repo.create_issue(title=issueTitle, body=issueBody)
#     print(res)
