---
name: comic-project-initializer
description: 漫畫專案初始化與清理器 (Project Initializer)，負責在開啟新漫畫專案時，安全清除所有上一次生成的中間產物與快取檔案，並保留最終的 PDF 成果。
---

# 🧹 Comic Project Initializer (專案初始化與中間檔清理器)

> [!NOTE] 角色定位
> 您是 **Project Initializer (專案環境維護專家)**。您的核心任務是在使用者要展開「全新漫畫主題」的創作時，扮演清理大腦，執行 **微創安全重設（Micro-Reset）**。您會安全清除所有上一次生成的中間暫存檔案（如世界觀、角色設定、分鏡腳本、Images 快取圖），**並絕對保留最終導出的 PDF 成果檔案**，以防範數據遺失。

---

## 🧹 1. 安全清理與初始化流程 (Workflow)

為防範誤刪使用者辛苦創作的最終成果，本系統採用 **「Working 資料夾工作區與根目錄分離」** 的微創清理架構，確保絕對的安全防護：

```mermaid
graph TD
    Trigger["🧹 收到工作區重設指令"] --> Warn["⚠️ 出現二次安全確認 (Double Check)"]
    Warn -->|確認重設| Clean["🛠️ 開始微創清理作業"]
    
    subgraph Files_Deletion ["❌ 安全刪除項目 (Wiped completely)"]
        D1["Working/ 暫存工作區目錄"]
        D2["Working/Images/ 過程快取圖片"]
        D3["Working/ 內所有世界觀與分鏡 Markdown/JSON"]
    end
    
    subgraph Files_Preservation ["🛡️ 絕對保留項目 (Preserved outside Working)"]
        P1["根目錄下的所有 PDF 漫畫書 (*.pdf)"]
        P2["Skills/ 資料夾下的所有 AI 開發技能"]
        P3["Scripts/ 及環境設定檔 config.json"]
    end
    
    Clean --> Files_Deletion
    Clean --> Files_Preservation
    Files_Deletion --> Success["🎉 工作區重建，環境就緒，可啟動新漫畫"]
```

---

## 💻 2. 自動化初始化指令序列 (CLI Cleanup Commands)

當使用者授權重設時，AI 代理會在背景執行以下安全清理腳本（與 `Scripts/init_project.sh` 一致）：

```bash
#!/bin/bash
# 漫畫專案安全重設與初始化腳本
echo "=== 開始進行漫畫專案工作區初始化重設 ==="

# 自動定位目前腳本所在目錄與設定檔
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/../config.json"

# 1. 讀取專案根目錄
VAULT_ROOT=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['manga_projects_root'])")
WORKING_DIR="$VAULT_ROOT/Working"

# 2. 執行清理動作：直接刪除暫存的 Working 工作區目錄即可，絕不波及外部的 PDF 成品！
if [ -d "$WORKING_DIR" ]; then
    echo "🧹 正在安全清理 Working/ 工作區目錄及其所有過程中間產物..."
    rm -rf "$WORKING_DIR"
fi

# 3. 重建乾淨的 Working/Images 工作區結構
mkdir -p "$WORKING_DIR/Images"

echo "🛡️ 目前專案根目錄下保留的最終 PDF 漫畫成果："
find "$VAULT_ROOT" -maxdepth 1 -name "*.pdf"

echo "✨ 專案工作區初始化完成！所有中間暫存檔已安全清除，乾淨的工作區已就緒。"
```

---

## 🚀 3. 推薦指令與使用者操作 (Usage)

在您準備創作全新的漫畫，並且已經將上一部漫畫打包成 PDF 存檔後，您可以直接對我說：

* 🗣️ **「請重設漫畫專案環境，開啟新的主題」**
  > （AI 代理會主動向您發起確認：`這將徹底刪除 Working/ 工作區目錄，清空所有上一次生成的中間 Markdown 腳本與 Images 過程圖片，但會絕對保留您所有的 PDF 成品、環境設定 config.json 與 Skills/ 核心技能套件，請問確認要執行嗎？`。在您確認後，系統會自動在背景呼叫此 Initializer，一秒重置環境，準備迎接口本、角色與畫面的全新生成！）
