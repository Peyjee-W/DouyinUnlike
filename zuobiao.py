import pyautogui
import time

# 等待5秒确保鼠标位置稳定
time.sleep(5)

# 获取当前鼠标坐标
current_position = pyautogui.position()

# 打印坐标
print(f"当前鼠标坐标是: {current_position}")
