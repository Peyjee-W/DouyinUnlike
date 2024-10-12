import pyautogui
import time
import keyboard  # 用于监听键盘事件

# 等待5秒准备时间
time.sleep(5)

for _ in range(100):
    # 如果按下了 'ESC' 键，停止循环，想要停止循环请疯狂连按
    if keyboard.is_pressed('esc'):
        print("程序被中断")
        break

    # 点击红心位置坐标 (885, 487)，此处替换成你的坐标
    pyautogui.click(x=885, y=487)
    
    # 模拟按下键
    pyautogui.press('down')
    
    # 适当的延迟，每次点击间隔0.5秒
    time.sleep(0.5)

print("程序结束")
