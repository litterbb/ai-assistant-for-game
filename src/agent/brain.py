# src/agent/brain.py
class GameAgent:
    def __init__(self, config):
        self.config = config
        # ดึงรายการการกระทำที่ทำได้จากคอนฟิก
        self.available_actions = config.get("available_actions", [])

    def decide_action(self, state):
        """
        ฟังก์ชันตัดสินใจ (เวอร์ชัน Mock AI)
        ในอนาคตเราจะเปลี่ยนส่วนนี้ให้ส่ง prompt ไปถาม LLM
        """
        hp = state.get("hp", 100)
        enemy_nearby = state.get("enemy_nearby", False)
        inventory = state.get("inventory", [])

        # กฎการตัดสินใจแบบง่ายๆ (Mock Logic)
        if hp < 30 and "potion" in inventory:
            return {"action_type": "use_item", "item": "potion", "reason": "เลือดน้อย ต้องกินยา"}
        
        elif enemy_nearby:
            return {"action_type": "attack", "target": "enemy", "reason": "มีศัตรูอยู่ใกล้ ต้องโจมตี"}
        
        else:
            return {"action_type": "explore", "reason": "ไม่มีศัตรู เดินสำรวจต่อ"}