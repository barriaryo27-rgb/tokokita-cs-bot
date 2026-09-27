import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="CS Bot - TokoKita", page_icon="🛍️")

st.title("🛍️ TokoKita - Customer Service Bot")
st.caption("Chatbot AI berbasis Gemini API untuk menjawab pertanyaan pelanggan toko online")

# ------------------ Sidebar (parameter kreatif) ------------------
with st.sidebar:
    st.header("⚙️ Pengaturan")
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        value=os.getenv("GEMINI_API_KEY", ""),
        help="Dapatkan API key gratis di https://aistudio.google.com/apikey",
    )
    gaya_bahasa = st.selectbox("Gaya Bahasa", ["Santai", "Formal"])
    st.markdown("---")
    st.caption("Fitur: memori percakapan otomatis selama sesi berjalan.")
    if st.button("🗑️ Reset Percakapan"):
        st.session_state.messages = []
        st.session_state.pop("chat", None)
        st.rerun()

if not api_key:
    st.warning("Masukkan Gemini API Key di sidebar untuk memulai chat.")
    st.stop()

genai.configure(api_key=api_key)

# ------------------ Knowledge base sederhana (domain toko online) ------------------
FAQ_CONTEXT = """
Informasi Toko TokoKita:
- Jam operasional: Senin-Sabtu, 09.00-17.00 WIB
- Pengiriman: 2-4 hari kerja (dalam kota), 5-7 hari kerja (luar kota)
- Kebijakan retur: barang bisa dikembalikan maksimal 7 hari setelah diterima,
  dengan syarat barang belum dipakai dan kemasan masih asli
- Metode pembayaran: transfer bank, e-wallet (OVO, GoPay, DANA), COD (area tertentu)
- Cek status pesanan: minta nomor order ke pelanggan, arahkan ke halaman "Lacak Pesanan"
  di website, atau eskalasi ke CS manusia bila belum bisa ditemukan
"""

system_instruction = f"""
Kamu adalah customer service AI untuk toko online bernama TokoKita.
Gunakan gaya bahasa {gaya_bahasa.lower()} saat menjawab pelanggan.
Jawab berdasarkan informasi toko berikut. Jika pertanyaan di luar informasi ini,
jawab dengan sopan bahwa kamu akan meneruskan ke tim CS manusia.

{FAQ_CONTEXT}

Aturan menjawab:
- Ramah, singkat, dan jelas
- Jangan mengarang kebijakan yang tidak ada di atas
- Gunakan bahasa Indonesia
"""

model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=system_instruction,
)

# ------------------ State percakapan (fitur memory) ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ Input chat ------------------
if prompt := st.chat_input("Tanyakan sesuatu ke CS TokoKita..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Mengetik..."):
            try:
                response = st.session_state.chat.send_message(prompt)
                reply = response.text
            except Exception as e:
                reply = f"Maaf, terjadi kesalahan saat menghubungi Gemini API: {e}"
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
