from github import Github, Issue # github에 issue를 생성하기 위함 (+ 깃허브 액션 사용)
import datetime # 현재 시각과 시간 포멧팅을 하기 위함
from pytz import timezone # 타임 존을 사용하기 위함
from dateutil.parser import parse # 문자열 날짜를 date로 변환하기 위함
import os # 환경 변수를 사용하기 위함
import time # 셀레니움에 딜레이를 주기위해 사용
from selenium import webdriver # 동적 리소스 크롤링 시에는(or 로그인) requests 대신 selenium을 사용해야 한다. (Selenium 3.x 버전을 사용하기)
from selenium.webdriver.common.keys import Keys # 셀레니움 사용시 키보드의 엔터키와 END키를 사용하기 위해 사용
from webdriver_manager.chrome import ChromeDriverManager # 리눅스 위에서 크롬드라이버 절대경로를 못찾으므로 이를 해결하기 위해 ChromeDriverManager 사용 (pip install webdriver-manager)

kst = timezone('Asia/Seoul') # KST == Korea Standard Time
today = datetime.datetime.now(kst)
print(today)
print("================================================================")

def isDateInRange(created_at):
    suffix_kst = '.000001+09:00' # (UTC의 기준시간보다 9시간이 빠르다는 의미이다. KST==UTC+09:00)
    created_at = parse(created_at + suffix_kst) # (이 크롤러가 작동할 서버의 타임 존은 UTC(Github)로 날짜 생성시 KST 타임으로 변환 해주어야함) (parse를 통해 문자열 날짜를 DATE로 변환한다.)
    yesterday = today - datetime.timedelta(2) # 2 days ago 표현

    return (today > created_at) and (created_at > yesterday) # 대상 게시글은 48시간 전 ~ 작동 시간

try:
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("lang=ko_KR")
    options.add_argument('headless') # headless로 옵션을 설정해야 리눅스 위에서 오류가 발생하지 않는다.
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--no-sandbox")

    titleList = []
    dayAndTimeList = []

    #===Naver career 크롤링 시작===
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    # browser = webdriver.Chrome('C:/chromedriver.exe', chrome_options=options) # 크롬 드라이버 경로
    site = "https://recruit.navercorp.com/naver/job/list/developer"
    browser.get(site) # 브라우저 열기
    browser.maximize_window()
    browser.implicitly_wait(10) # 로딩이 끝날 때 까지 10초 까지는 기다림
    browser.find_element_by_css_selector('button.more_btn').click() # 더보기 클릭
    time.sleep(1)
    browser.find_element_by_css_selector('button.more_btn').click() # 더보기 클릭
    time.sleep(1)

    elements = browser.find_elements_by_css_selector('.card_list > ul > li')

    for element in elements:
        name = element.find_element_by_css_selector('.crd_tit').text
        dayAndTime = element.find_element_by_css_selector('.crd_date').text

        # print([name], [dayAndTime])
        titleList.append(name)
        dayAndTimeList.append(dayAndTime)
    #===Naver career 크롤링 끝===

    #===Line career 크롤링 시작===
    site = "https://careers.linecorp.com/jobs?ca=Engineering&ci=Seoul,Bundang&co=East%20Asia"
    browser.get(site) # 브라우저 열기
    browser.maximize_window()
    browser.implicitly_wait(100) # 로딩이 끝날 때 까지 10초 까지는 기다림
    time.sleep(2) # 조금 더 딜레이

    elements = browser.find_elements_by_css_selector('.job_list > li')

    for element in elements:
        name = element.find_element_by_css_selector('a > .title').text
        dayAndTime = element.find_element_by_css_selector('a > .date').text

        # print([name], [dayAndTime])
        titleList.append(name)
        dayAndTimeList.append(dayAndTime)
    #===Line career 크롤링 끝===

    issueBody = ''

    for x, y in zip(titleList, dayAndTimeList):
        if (y[13:17] == "채용시까지"):
            published_at = y[0:10]
            published_at = published_at.replace('.', '-') + " 00:00:00"  # 글 등록 시간은 가져오기 불가능하기 때문에 0시(자정)라고 가정
        else:
            published_at = y[0:10]
            published_at = published_at.replace('.', '-') + " 00:00:00"  # 글 등록 시간은 가져오기 불가능하기 때문에 0시(자정)라고 가정

        item = str(published_at) + ' ' + str(x).replace("\n", "").replace(' ', '').strip()

        if ('Robotics' not in str(x) and isDateInRange(str(published_at))):
            issueBody += item
        else:
            print('[filtered]', item)

    print('================================================================')

    issueTitle = "개발자 모집 글 모음(%s)" % (today.strftime("%Y년 %m월 %d일 %H시"))
    print(issueTitle)
    print(issueBody)

    # print(os.environ)
    GITHUB_TOKEN = os.environ[
        'TOKEN_GITHUB']  # 시스템 환경변수에 깃허브 토큰 저장되어있음 (Expires on Wed, May 11 2022) (만료되면 깃허브 settings-developer settings-personal access token에서 다시 토큰 생성하고 환경변수 등록해야함)
    REPO_NAME = "recruitment-news"
    repo = Github(GITHUB_TOKEN).get_user().get_repo(REPO_NAME)
    if (issueBody != '' and REPO_NAME == "recruitment-news"):
        res = repo.create_issue(title=issueTitle, body=issueBody)
        print(res)
except Exception as e:
    print(e)
    browser.quit()
finally:
    print("finally...")
    browser.quit()



