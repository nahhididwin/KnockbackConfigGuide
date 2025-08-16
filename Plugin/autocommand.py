print("Running autocommand.py")

#C:\Users\Admin\code.place\Anticheat\trapplayer\run.bat


import subprocess
import time
import random
import os

def run_bat_and_interact(bat_file_path):


    process = subprocess.Popen(
        [bat_file_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        text=True,
        bufsize=1
    )



    try:

        process.stdin.write("start\n")
        process.stdin.flush() 
        print("Đã gửi lệnh 'start'")


        print("Đang đợi 10 giây...")
        time.sleep(10)

        while True:


            delay = random.randint(3, 5)
            print(f"Đang đợi {delay} giây trước khi gửi 'chat ditmeonlyduu'...")
            time.sleep(delay)



            process.stdin.write("chat ditmeonlyduu\n")
            process.stdin.flush()
            print("Đã gửi 'chat ditmeonlyduu'")








            delay = random.randint(3, 5)
            print(f"Đang đợi {delay} giây trước khi gửi 'chat /tp a'...")
            time.sleep(delay)



            process.stdin.write("chat /tp a\n")
            process.stdin.flush()
            print("Đã gửi 'chat /tp a'")



# chat restart = restart bot
           


# sau "online:" ; rồi phân cách bằng ","; cho /list để xem list player.



    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    finally:

        process.stdin.close()
        process.wait()
        print("Chương trình kết thúc.")


# Đường dẫn đến file run.bat :v
BAT_FILE_PATH = r"C:\Users\Admin\code.place\Anticheat\trapplayer\run.bat"

if __name__ == "__main__":
    if not os.path.exists(BAT_FILE_PATH):
        print(f"Lỗi: Không tìm thấy file {BAT_FILE_PATH}")
    else:
        run_bat_and_interact(BAT_FILE_PATH)








