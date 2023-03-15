
def test_file_size(file_path, size):
    # 创建新文件
    with open(file_path, 'w') as f:
        f.seek(1024 * 1024 * size - 1)
        f.write('\x00')
    f.close()
