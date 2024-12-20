from pyrogram import Client
import time

# Masukkan detail API Anda
api_id = 20786693  # Ganti dengan API ID Anda
api_hash = "6eebbb7d9f9825a2d200c034bfbb7102"  # Ganti dengan API HASH Anda
SESSION = "BQAhIHQASYWkm2DM8P3kRBEXF0KF34ow1nLh8KlM5mu-2UZVYL2d8mhd3orXD-981HAX6Lmdvkj6T3Dxt28_ocQ36n7Ci6HKeyUbM3VHtKGvWt6ervWSaufwWabtlG6F2338n6Nlla5zzAKCi5Vlqqj1yKIk3n-SMi0f89PZDjx3JKpIhzJh7XHrJyc_6AJbAMjDpmF0oGGwwvBt28Becw8orOxpMbO45iDmvWntzXYDF7NV6mNlq5VFFLWs0G6Wf1xh1f_ttXmlZQnse-lDYKU1WD3wpPXpBXhWzSimtAv4VSMYw3rxv5ud1qucZRxdsgtBrZvSk0CzIIFAsXZzlv2zL2lFIwAAAAB_3fViAA"

# Buat instance Pyrogram Client
app = Client("my_userbot", api_id=api_id, api_hash=api_hash, session_string=SESSION)

# Fungsi utama userbot
def userbot():
    with app:
        print("Userbot is running...")

        while True:
            try:
                # Kirim pesan ke @chatbot
                app.send_message("@chatbot", "Halo, ini pesan otomatis dari userbot!")
                print("Pesan terkirim ke @chatbot")
                time.sleep(3)  # Tunggu 3 detik

                # Kirim perintah /next
                app.send_message("@chatbot", "/next")
                print("Perintah /next terkirim")
                time.sleep(5)  # Tunggu 5 detik sebelum mengirim pesan lagi
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(10)  # Tunggu sebelum mencoba ulang jika terjadi error

# Jalankan userbot
if __name__ == "__main__":
    userbot()
