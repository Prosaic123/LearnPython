import os

class FileUtils:
    @staticmethod
    def read_file(file_path):
        """读取文件内容"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        """写入内容到文件"""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def list_files(directory):
        """列出指定目录下的所有文件"""
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
