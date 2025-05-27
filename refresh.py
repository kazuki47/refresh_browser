import pyautogui
import time

# リフレッシュ間隔（秒）
refresh_interval = 40  

try:
    print(f"{refresh_interval}秒ごとにブラウザをリフレッシュ")
    while True:
        # 少し待機してからリフレッシュ（
        time.sleep(2)
        pyautogui.click(150, 150)
        # Ctrl+R 
        pyautogui.hotkey('ctrl', 'r')
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - リフレッシュしました。")

        # 指定した間隔だけ待機
        time.sleep(refresh_interval)

except KeyboardInterrupt:
    print("\nスクリプトを終了します。")
except Exception as e:
    print(f"エラーが発生しました: {e}")