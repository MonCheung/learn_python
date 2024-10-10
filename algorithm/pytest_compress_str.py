import pytest
from compress_str import CompressString

#实例化导入的CompressString类
compressor = CompressString()

def test_compress_none():
    assert compressor.compress(None) == None

def test_compress_empty_string():
    assert compressor.compress('') == ''

def test_compress_no_reduction():
    assert compressor.compress('AABBCC') == 'AABBCC'

def test_compress_with_reduction():
    assert compressor.compress('AAABCCDDDDE') == 'A3BC2D4E'
    assert compressor.compress('BAAACCDDDD') == 'BA3C2D4'
    assert compressor.compress('AAABAACCDDDD') == 'A3BA2C2D4'

if __name__ == '__main__':
    #指定文件路径，只执行当前测试脚本
    pytest.main(['algorithm/pytest_compress_str.py','--html=algorithm/report.html'])
