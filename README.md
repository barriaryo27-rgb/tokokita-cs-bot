# TokoKita - Customer Service Chatbot (Gemini API)

Final project Hacktiv8 — LLM-Based Tools and Gemini API Integration.

## Use Case
Chatbot customer service untuk toko online **TokoKita**. Bot menjawab pertanyaan
seputar jam operasional, pengiriman, kebijakan retur, metode pembayaran, dan
status pesanan, berdasarkan basis pengetahuan sederhana yang ditanamkan di system
instruction.

## Parameter Kreatif
- **Gaya bahasa**: Santai / Formal (dipilih lewat sidebar)
- **Domain pengetahuan**: FAQ toko online (pengiriman, retur, pembayaran)
- **Fitur tambahan**: memory percakapan otomatis selama sesi (menggunakan
  `model.start_chat()` dari Gemini sehingga histori chat ikut dikirim setiap turn)

## Tech Stack
- Python 3.10+
- Streamlit (UI)
- Gemini API (`google-generativeai`, model `gemini-1.5-flash`)

## Cara Menjalankan
1. Clone repo ini dan masuk ke foldernya
2. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```
3. Salin `.env.example` menjadi `.env`, lalu isi dengan API key Gemini kamu
   (dapatkan gratis di https://aistudio.google.com/apikey):
   ```bash
   cp .env.example .env
   ```
4. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```
5. Buka browser di `http://localhost:8501`, masukkan API key di sidebar
   (kalau belum otomatis terbaca dari `.env`), lalu mulai chat.

## Screenshot
Tambahkan screenshot UI kamu di sini setelah menjalankan aplikasi, misalnya:

```
![Screenshot UI](screenshot.png)
```

## Struktur Project
```
.
├── app.py              # Aplikasi utama Streamlit + integrasi Gemini API
├── requirements.txt     # Daftar dependency
├── .env.example         # Contoh konfigurasi API key
├── .gitignore
└── README.md
```
