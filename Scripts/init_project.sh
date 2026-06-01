#!/bin/bash
# 漫畫專案安全重設與初始化腳本
echo "=== 開始進行漫畫專案工作區初始化重設 ==="

# 腳本所在目錄
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/../config.json"

# 1. 若環境設定檔不存在，先執行初始化設定
if [ ! -f "$CONFIG_FILE" ]; then
    echo "⚠️ 尚未偵測到環境設定檔，啟動環境設定程序..."
    python3 "$SCRIPT_DIR/config_manager.py"
fi

# 2. 從 config.json 中讀取專案根目錄
VAULT_ROOT=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['manga_projects_root'])")

if [ -empty "$VAULT_ROOT" ] || [ ! -d "$VAULT_ROOT" ]; then
    echo "❌ 錯誤：無法識別或找不到設定的專案根目錄：$VAULT_ROOT"
    exit 1
fi

WORKING_DIR="$VAULT_ROOT/Working"

# 3. 執行清理動作：直接刪除並重建暫存的 Working 工作區資料夾即可！
#    這將清除所有中間產生的世界觀設定、分鏡腳本、角色參考圖與頁面草稿。
if [ -d "$WORKING_DIR" ]; then
    echo "🧹 正在安全清理 Working/ 工作區目錄及其所有過程中間產物..."
    rm -rf "$WORKING_DIR"
fi

# 4. 重建乾淨的 Working/Images 工作區結構
mkdir -p "$WORKING_DIR/Images"

echo "🛡️ 目前專案根目錄下保留的最終 PDF 漫畫成果："
find "$VAULT_ROOT" -maxdepth 1 -name "*.pdf"

echo "✨ 專案工作區初始化完成！所有中間暫存檔已安全清除，乾淨的工作區已就緒。"
