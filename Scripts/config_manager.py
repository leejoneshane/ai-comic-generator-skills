import os
import json
import sys

CONFIG_PATH = ".agent/ai-comic-generator-skills/config.json"

def load_or_create_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if "manga_projects_root" in config:
                    return config
        except Exception as e:
            print(f"⚠️ 讀取設定檔失敗：{e}，將重建設定。")

    # 預設儲存位置：Mac 的文件資料夾 (Documents)
    default_path = os.path.expanduser("~/Documents/AI 漫畫生成器")
    print("🚀 偵測到首次執行，正在進行環境設定...")
    print(f"預設漫畫專案儲存資料夾為：{default_path}")
    print("若不需要變更，請直接按下 Enter；若需要變更，請輸入新的絕對路徑：")
    
    user_input = ""
    # 若在非交互式或自動化測試環境下，可安全回退
    if sys.stdin.isatty():
        try:
            user_input = input().strip()
        except KeyboardInterrupt:
            print("\n❌ 操作已取消。")
            sys.exit(1)
    
    manga_root = user_input if user_input else default_path
    manga_root = os.path.abspath(os.path.expanduser(manga_root))
    
    # 建立目錄結構 (包含 Working 和 Working/Images)
    working_dir = os.path.join(manga_root, "Working")
    images_dir = os.path.join(working_dir, "Images")
    os.makedirs(images_dir, exist_ok=True)
    
    config = {"manga_projects_root": manga_root}
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"✨ 已成功將環境設定寫入：{CONFIG_PATH}")
        print(f"📂 專案根目錄已設定為：{manga_root}")
        print(f"🛠️ 暫存工作區已建立於：{working_dir}")
    except Exception as e:
        print(f"❌ 寫入設定檔失敗：{e}")
    
    return config

if __name__ == "__main__":
    load_or_create_config()
