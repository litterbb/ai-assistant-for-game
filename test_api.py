import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print(f"🔑 ตรวจพบ Key ขึ้นต้นด้วย: {api_key[:10] if api_key else 'ไม่พบ Key'}...")

try:
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=30000) # เพิ่มเวลาเป็น 30 วินาที
    )
    
    print("⏳ กำลังทดสอบเชื่อมต่อ (รอสูงสุด 30 วินาที)...")
    
    # ลองใช้ชื่อโมเดลที่ระบบแนะนำใน Error ครั้งล่าสุด
    response = client.models.generate_content(
        model='gemini-3.8-flash', 
        contents='พิมพ์คำว่า Hello'
    )
    print(f"✅ เชื่อมต่อสำเร็จ! AI ตอบกลับว่า: {response.text}")
    
except Exception as e:
    print(f"\n❌ เชื่อมต่อล้มเหลว: {e}")