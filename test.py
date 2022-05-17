import pyautogui
import pyperclip
import time

if __name__ == "__main__":
    # 等待5秒光标移动
    time.sleep(5)
    for line in open(r"test.txt", encoding="utf-8"):
        # test.txt 文章文件
        for i in line:
            pyperclip.copy(i)
            pyautogui.typewrite('{}'.format(i))
