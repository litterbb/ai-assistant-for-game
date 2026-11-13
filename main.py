# main.py
import json
import time
from src.agent.brain import GameAgent

def load_game_config(game_name):
    """โหลดไฟล์คอนฟิกของเกม"""
    config_path = f"configs/games/{game_name}.json"
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ ไม่พบไฟล์คอนฟิก: {config_path}")
        return None

def main():
    print("=== 🤖 AI Game Assistant เริ่มทำงาน ===")
    
    # 1. โหลดคอนฟิกเกม (สมมติว่าเราเล่นเกมชื่อ demo_game)
    game_config = load_game_config("demo_game")
    if not game_config:
        return

    # 2. เริ่มต้น Agent (สมองของ AI)
    agent = GameAgent(game_config)
    print(f"🎮 โหลดเกม: {game_config['name']} สำเร็จ")

    # 3. จำลองสถานะเกม (ในอนาคตส่วนนี้จะมาจากการอ่านหน้าจอจริง)
    # สมมติว่าเราเจอสถานะ: เลือดเหลือ 20 (ต่ำมาก) และมีมอนสเตอร์อยู่ใกล้
    simulated_game_state = {
        "hp": 20, 
        "enemy_nearby": True,
        "inventory": ["potion", "sword"]
    }

    # 4. ลูปการทำงานหลัก (Perceive -> Think -> Act)
    print("\n--- 🔄 เริ่มรอบการทำงาน ---")
    
    print(f"👁️ [Perception] อ่านสถานะเกม: {simulated_game_state}")
    
    # ส่งสถานะให้ Agent ตัดสินใจ
    action = agent.decide_action(simulated_game_state)
    
    print(f"🧠 [Brain] AI ตัดสินใจ: {action}")
    
    # 5. ดำเนินการ (ในอนาคตส่วนนี้จะเป็นการจำลองกดปุ่มจริง)
    print(f"🎮 [Action] กำลังดำเนินการ: {action['action_type']}...")
    print("--- จบรอบการทำงาน ---\n")

if __name__ == "__main__":
    main()