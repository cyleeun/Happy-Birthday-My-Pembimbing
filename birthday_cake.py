import os
import time
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_cake():
    frames = [
        """
        ┏━━━━━━━━━━━━━━━━━━┓
        ┃ 🎂 ULANG TAHUN 🎂 ┃
        ┗━━━━━━━━━━━━━━━━━━┛
               🕯️  🕯️  🕯️
              ╱────────╲
             │  🎂🎂🎂🎂  │
             │ 🎂 KAKE 🎂 │
             │  🎂🎂🎂🎂  │
              ╲────────╱
        """,
        """
        ┏━━━━━━━━━━━━━━━━━━┓
        ┃ 🎂 ULANG TAHUN 🎂 ┃
        ┗━━━━━━━━━━━━━━━━━━┛
              🕯️  🔥  🕯️
              ╱────────╲
             │  🎂🎂🎂🎂  │
             │ 🎂 KAKE 🎂 │
             │  🎂🎂🎂🎂  │
              ╲────────╱
        """,
        """
        ┏━━━━━━━━━━━━━━━━━━┓
        ┃ 🎂 ULANG TAHUN 🎂 ┃
        ┗━━━━━━━━━━━━━━━━━━┛
             🕯️  🕯️  🕯️
              ╱────────╲
             │  🎂🎂🎂🎂  │
             │ 🎂 KAKE 🎂 │
             │  🎂🎂🎂🎂  │
              ╲────────╱
        """
    ]
    
    for _ in range(6):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.5)

def print_message(name):
    messages = [
        "✨ Selamat Ulang Tahun! ✨",
        f"🎉 Selamat Ulang Tahun {name}! 🎉",
        "🎈 Semoga hari spesialmu penuh kebahagiaan! 🎈",
        "🌟 Terima kasih telah lahir dan membuat dunia lebih indah! 🌟",
        "🎁 Semoga semua impianmu menjadi kenyataan! 🎁"
    ]
    
    for msg in messages:
        print(f"\n{msg}")
        time.sleep(1)

if __name__ == "__main__":
    name = input("Masukkan nama orang yang berulang tahun: ")
    
    clear_screen()
    animate_cake()
    
    clear_screen()
    print(f"\n{'='*50}")
    print(f"{'🎂 SELAMAT ULANG TAHUN 🎂':^50}")
    print(f"{'='*50}\n")
    
    print_message(name)
    
    print(f"\n{'='*50}")
    print(f"{'Semoga selalu bahagia dan sehat selalu! 💝':^50}")
    print(f"{'='*50}\n")
