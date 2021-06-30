import oss2
import argparse

def parse_argument():
    parser = argparse.ArgumentParser(description='crc64ecma hash check for supplied filename.')
    parser.add_argument('filename', help='file name')
    args = parser.parse_args()
    return args.filename

def calculate_file_crc64(file_name, block_size=64 * 1024, init_crc=0):
    """计算文件的MD5
    :param file_name: 文件名
    :param block_size: 计算MD5的数据块大小，默认64KB
    :return 文件内容的MD5值
    """
    with open(file_name, 'rb') as f:
        crc64 = oss2.utils.Crc64(init_crc)
        while True:
            data = f.read(block_size)
            if not data:
                break
            crc64.update(data)

    return crc64.crc

def main():
    #filename = "/Users/zhengxin/Downloads/Seagate Removable Disk/201228_NS500807_0366_AH7VYLBGXH.zip"
    filename = parse_argument()
    crc64value = calculate_file_crc64(filename)
    print(f"crc64ecma: {crc64value}" )


if __name__ == '__main__':
    main()
