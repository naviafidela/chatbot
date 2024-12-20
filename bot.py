from pyrogram import Client
import time

# Masukkan detail API Anda
api_id = 123456  # Ganti dengan API ID Anda
api_hash = "abcdef1234567890abcdef1234567890"  # Ganti dengan API HASH Anda

# Buat instance Pyrogram Client
app = Client("my_userbot", api_id=api_id, api_hash=api_hash)

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
