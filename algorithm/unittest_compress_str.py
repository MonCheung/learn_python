import unittest
from compress_str import CompressString

class TestCompress(unittest.TestCase):
    def setUp(self):
        self.compressor = CompressString()  # 正确实例化

    def test_compress_str(self):
        self.assertEqual(self.compressor.compress(None), None)
        self.assertEqual(self.compressor.compress(''), '')
        self.assertEqual(self.compressor.compress('AABBCC'), 'AABBCC')
        self.assertEqual(self.compressor.compress('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(self.compressor.compress('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(self.compressor.compress('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')

if __name__ == '__main__':
    unittest.main()
