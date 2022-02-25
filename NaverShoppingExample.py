# import time
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver # Selenium 3.x 버전을 사용하기
#
# browser = webdriver.Chrome('C:/chromedriver.exe') # 크롬 드라이버 경로
#
# browser.get("http://www.naver.com") # 브라우저 열기
# browser.implicitly_wait(10) # 로딩이 끝날 때 까지 10초 까지는 기다려줌
# browser.find_element_by_css_selector('a.nav.shop').click() # a태그에 nav와 shop이라는 class 선택자를 가지고 있는 것을 클릭 (쇼핑탭 클릭)
# time.sleep(2) # 2초 정도 기다림
# search = browser.find_element_by_css_selector('input.co_srh_input._input')
# search.click() # 검색칸 클릭
# search.send_keys("아이폰 13") # 검색어 입력
# search.send_keys(Keys.ENTER) # 엔터 치기
#
# # 상품목록이 다뜨도록 끝까지 아래로 스크롤(동적 리소스)
# # 직접 사이트에서 개발자 도구 연 다음 Console탭에서 window.scrollY 명령어로 맨 아래의 Y값이 몇인지 확인할 수도 있음
# before_h = browser.execute_script("return window.scrollY") # 스크롤 전 높이 (자바스크립트 명령어 실행) 0이다.
#
# while (True): # 맨 아래로 스크롤 내리기
#     browser.find_element_by_css_selector("body").send_keys(Keys.END) # 맨 아래로 갈수 있도록 키보드의 END키를 누름
#
#     time.sleep(1) # 스크롤 사이 페이지 로딩 시간 (동적 리소스를 가져오는 시간 기다림)
#
#     after_h = browser.execute_script("return window.scrollY") # 스크롤 후 높이
#
#     if (after_h == before_h):
#         break
#
#     before_h = after_h
#
# items = browser.find_elements_by_css_selector('.basicList_info_area__17Xyo') # 상품 정보 div 리스트 추출 (find_element가 아닌 find_elements 사용)
#
# for item in items:
#     name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
#     try:
#         price = item.find_element_by_css_selector('.price_num__2WUXn').text  # 제품 가격이 없는 것도 있음 => 오류발생 => 예외 처리 해야함
#     except:
#         price = "판매중단"
#     try:
#         link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href') # 자식 태그 선택
#     except:
#         link = "링크없음"
#
#     print(name, price, link)