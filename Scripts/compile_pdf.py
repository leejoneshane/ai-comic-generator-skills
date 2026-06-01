import os
import re
import sys
from PIL import Image

def natural_sort_key(s):
    # 自然排序算法，確保 comic_page_10.png 排在 comic_page_2.png 後面
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def compile_comic_to_pdf(vault_path, output_pdf_name="Final_Comic_Book.pdf"):
    images_dir = os.path.join(vault_path, "Images")
    if not os.path.exists(images_dir):
        print(f"❌ 找不到 Images 資料夾：{images_dir}")
        return False
    
    # 搜尋所有已審查定稿的漫畫頁面
    page_files = [f for f in os.listdir(images_dir) if (f.startswith("comic_page_") or f.startswith("page_")) and f.lower().endswith((".png", ".jpg", ".jpeg"))]
    
    if not page_files:
        print("❌ 沒有找到任何已生成的漫畫頁面！")
        return False
        
    # 自然排序頁數
    page_files.sort(key=natural_sort_key)
    print(f"🔄 偵測到 {len(page_files)} 頁漫畫，排序如下：")
    for f in page_files:
        print(f"  - {f}")
        
    # 載入並轉換為 RGB 格式
    images = []
    for file in page_files:
        img_path = os.path.join(images_dir, file)
        img = Image.open(img_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        images.append(img)
        
    # 打包導出為單一 PDF 檔案
    output_path = os.path.join(vault_path, output_pdf_name)
    images[0].save(output_path, "PDF", save_all=True, append_images=images[1:])
    print(f"✨ 漫畫已成功打包導出至：{output_path}")
    return True

if __name__ == "__main__":
    vault_root = "/Users/shane/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI 漫畫生成器"
    output_name = "Final_Comic_Book.pdf"
    if len(sys.argv) > 1:
        output_name = sys.argv[1]
        if not output_name.endswith(".pdf"):
            output_name += ".pdf"
    
    compile_comic_to_pdf(vault_root, output_name)
