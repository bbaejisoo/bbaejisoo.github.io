# 키보드, 마우스, Python으로 제어하기
# pip install pyautogui : 화면을 맘대로 조절이 가능하다.
import pyautogui

# 마우스커서를 아래의 좌표로 이동 후 클릭
pyautogui.moveTo(100,200)
pyautogui.click()
pyautogui.moveRel(200, 100)

# pyautogui.position()이라는 것으로 좌표 확인 가능
# import pyautogui
# 마우스 커서의 위치를 얻고 싶은 곳에서 실행
# pyautogui.positon()
pyautogui.moveTo(32, 140)
pyautogui.moveRel(1047, 394)

# 이동 후 내용 입력
pyautogui.moveTo(1047, 394)
pyautogui.click()
pyautogui.typewrite('abcde')
# 만약 한글을 입력하고자 할 때, 한영키를 눌러놓고 영어를 입력해야한다. 'dlqfur' => '입력'

# 'enter'가 실행된다. press
pyautogui.press('enter')

# 스크린샷 방법

pyautogui.screenshot('result.png')

# 계산기를 클릭 후 값을 계산
# 계산기를 클릭하기 위한 좌표
pyautogui.moveTo(100,200)
pyautogui.click()

x, y = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('+.png')
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('3.png')
pyautogui.click(x, y)
pyautogui.press('enter')




















