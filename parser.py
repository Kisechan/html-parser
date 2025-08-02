from bs4 import BeautifulSoup
import os

def extract_span_texts(html_file, output_file):
    try:
        # 读取HTML文件
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 查找所有的<span>标签
        span_tags = soup.find_all('span')

        # 提取每个<span>标签的文本内容
        texts = [span.get_text(strip=True) for span in span_tags if span.get_text(strip=True)]

        # 将文本内容写入输出文件，每个元素一行
        with open(output_file, 'w', encoding='utf-8') as file:
            for text in texts:
                file.write(text + '\n')

        print(f"成功提取 {len(texts)} 个<span>标签文本到 {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")

# 使用示例
if __name__ == "__main__":
    # 输入HTML文件路径
    html_file = 'draft.html'  # 替换为你的HTML文件路径
    # 输出文件路径
    output_file = 'output.txt'

    # 检查输入文件是否存在
    if not os.path.exists(html_file):
        print(f"错误: 文件 {html_file} 不存在")
    else:
        extract_span_texts(html_file, output_file)