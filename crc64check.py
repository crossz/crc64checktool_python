# -*- coding=utf-8

import sys
import logging
import crcmod
import argparse

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger('[crc64ecma checksum]')

def parse_argument():
    parser = argparse.ArgumentParser(description='crc64ecma hash check for supplied filename.')
    parser.add_argument('filename', help='file name')
    args = parser.parse_args()
    return args.filename

def calculate_file_crc64(file_name, block_size=64 * 1024, init_crc=0):
# def calculate_file_crc64(file_name, block_size=6, init_crc=0):
    """计算文件的 Hash
    :param file_name: 文件名
    :param block_size: 计算 HASH 的数据块大小，默认64KB
    :return 文件内容的 Hash 值
    """
    crc64 = crcmod.mkCrcFun(0x142F0E1EBA9EA3693, initCrc=init_crc, xorOut=0xffffffffffffffff, rev=True)

    with open(file_name, 'rb') as f:    
        while True:
            data = f.read(block_size)
            if not data:
                break
            if 'crc64_value' not in locals():
                crc64_value = crc64(data)
                # logger.debug(f'0.{crc64_value}')
            else:
                crc64_value = crc64(data, crc64_value)
                # logger.debug(f'{crc64_value}')

    return crc64_value

def main():
    #filename = "/Users/zhengxin/Downloads/Seagate Removable Disk/201228_NS500807_0366_AH7VYLBGXH.zip"
    filename = parse_argument()
    crc64value = calculate_file_crc64(filename)
    logger.info(f"{crc64value}")


if __name__ == '__main__':
    main()
