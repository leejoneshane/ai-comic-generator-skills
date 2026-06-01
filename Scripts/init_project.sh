#!/bin/bash
# 漫畫專案安全重設與初始化腳本
echo "=== 開始進行漫畫專案初始化重設 ==="

VAULT_ROOT="/Users/shane/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI 漫畫生成器"

# 1. 進入儲存庫根目錄
cd "$VAULT_ROOT" || { echo "❌ 錯誤：找不到儲存庫根目錄！"; exit 1; }

# 2. 刪除所有中間 Markdown 筆記檔（因核心指南均已整合至 Skills/ 目錄中，故清空根目錄的所有中間筆記）
echo "🧹 正在清理根目錄中的中間 Markdown 筆記檔..."
find . -maxdepth 1 -name "*.md" -delete

# 清理教育應用或其他子目錄中的 Markdown，如果有
if [ -d "教育應用" ]; then
    echo "🧹 清理教育應用目錄..."
    rm -rf "教育應用"/*
fi

# 3. 清理 Images 資料夾中的所有過程圖片（角色設定圖、漫畫頁面），但保留 Images 資料夾本身
if [ -d "Images" ]; then
    echo "🧹 正在清理 Images/ 下的所有過程圖稿與設定圖..."
    rm -rf "Images"/*
else
    mkdir -p "Images"
fi

# 4. 保留所有最終 PDF 檔案，輸出目前已保留的成品清單
echo "🛡️ 保留之最終 PDF 漫畫成果："
find . -maxdepth 1 -name "*.pdf"

echo "✨ 專案初始化完成！所有中間暫存檔已安全清除，乾淨的開發環境已就緒。"
