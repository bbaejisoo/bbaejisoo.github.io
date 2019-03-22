###############################
# PC 카카오톡 로그인 응용
###############################
import subprocess
import pyautogui
import time

# 맥 전용
# kakao = subprocess.Popen(['open', '-a', 'KakaoTalk'])

# 카카오톡 경로
kakao = subprocess.Popen(["C:\\Program Files (x86)\\Kakao\\KakaoTalk\\KakaoTalk.exe"])
time.sleep(3)

from kakao_id_pw import ID, PW

pyautogui.typewrite(ID)
pyautogui.press('tab')
pyautogui.typewrite(PW)
pyautogui.press('tab')
pyautogui.press('enter')
