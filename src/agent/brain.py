# src/agent/brain.py
import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

class GameAgent:
    def __init__(self, config):
        self.config = config
        self.available_actions = config.get("available_actions", [])
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ ไม่พบ GEMINI_API_KEY ในไฟล์ .env")
            
        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=10000) 
        )

    def decide_action(self, state):
        prompt = f"""
        คุณคือ AI ผู้ช่วยเล่นเกม
        ข้อมูลเกม: {self.config.get('name')} - {self.config.get('description')}
        การกระทำที่ทำได้: {self.available_actions}
        
        สถานะเกมปัจจุบัน:
        {json.dumps(state, ensure_ascii=False)}
        
        จากสถานะนี้ จงเลือกการกระทำที่ดีที่สุดเพียง 1 อย่าง 
        และตอบกลับเป็นรูปแบบ JSON เท่านั้น (ห้ามมีข้อความอื่นปน) โดยมีรูปแบบดังนี้:
        {{
            "action_type": "ชื่อการกระทำ",
            "reason": "เหตุผลสั้นๆ ที่คุณเลือกทำสิ่งนี้"
        }}
        """

        print("   ⏳ กำลังส่งข้อมูลให้ Gemini คิด...")
        
        try:
            # เปลี่ยนชื่อโมเดลเป็น 1.5-flash ซึ่งเสถียรและฟรีสำหรับทุกคน
            response = self.client.models.generate_content(
                model='gemini-3.8-flash',
                contents=prompt,
            )
            
            raw_text = response.text
            cleaned_text = raw_text.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_text)
            
        except Exception as e:
            print(f"\n❌ เกิดข้อผิดพลาด: {e}\n")
            return {"action_type": "explore", "reason": "ระบบ AI ขัดข้องชั่วคราว"}