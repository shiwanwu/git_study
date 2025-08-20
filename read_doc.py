import win32com.client
import os


def read_doc_file(file_path):
    """
    使用pywin32读取Word文档内容，逐行返回

    参数:
        file_path (str): Word文档的完整路径

    返回:
        list: 包含文档每一行的列表，或错误信息
    """
    word = None
    try:
        # 创建Word应用程序对象
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # 打开Word文档
        doc = word.Documents.Open(file_path)

        # 获取所有段落
        paragraphs = doc.Paragraphs

        # 将每个段落的内容添加到列表中
        lines = [para.Range.Text.strip() for para in paragraphs]

        # 关闭文档，不保存更改
        doc.Close(False)

        return lines

    except Exception as e:
        # 捕获并返回任何异常
        return [f"读取文件时出错: {str(e)}"]

    finally:
        # 确保Word应用程序被关闭
        if word is not None:
            try:
                word.Quit()
            except:
                pass


def write_doc_file(output_path, lines):
    """
    将内容写入新的Word文档

    参数:
        output_path (str): 输出文档的完整路径
        lines (list): 要写入的行列表

    返回:
        str: 成功/错误信息
    """
    word = None
    try:
        # 创建Word应用程序对象
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # 创建新文档
        doc = word.Documents.Add()

        # 添加每一行到文档中
        for line in lines:
            # 检查行是否为空
            if line.strip():
                # 添加段落
                doc.Content.Text += line + "\n"

        # 保存文档
        doc.SaveAs(output_path)

        # 关闭文档
        doc.Close(False)

        return f"文档已成功保存到: {output_path}"

    except Exception as e:
        return f"写入文件时出错: {str(e)}"

    finally:
        # 确保Word应用程序被关闭
        if word is not None:
            try:
                word.Quit()
            except:
                pass


def main():
    # 输入和输出文件路径
    input_file = r"D:\resume\sv.doc"
    output_file = r"D:\resume\sv_copy.doc"

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件不存在 - {input_file}")
        return

    # 读取输入文件
    print("正在读取文档...")
    lines = read_doc_file(input_file)

    # 检查是否读取成功
    if isinstance(lines, list) and len(lines) > 0:
        # 检查是否有错误信息
        if lines[0].startswith("读取文件时出错"):
            print(lines[0])
            return

        print(f"成功读取 {len(lines)} 行内容")

        # 写入输出文件
        print("正在写入新文档...")
        result = write_doc_file(output_file, lines)
        print(result)
    else:
        print("读取文档时出错")


if __name__ == "__main__":
    main()
