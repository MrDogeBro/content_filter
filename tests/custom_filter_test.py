import unittest
import content_filter

class TestCustomFilter(unittest.TestCase):
    def custom_filter_test(self):
        self.assertEqual(content_filter.checkMessage("fuck"), True)
        self.assertEqual(content_filter.checkMessage("bitch"), True)
        self.assertEqual(content_filter.checkMessage("ass"), True)
        self.assertEqual(content_filter.checkMessage("nigger"), True)
        self.assertEqual(content_filter.checkMessage("dildo"), True)
        self.assertEqual(content_filter.checkMessage("testing"), False)
        self.assertEqual(content_filter.checkMessage("check"), False)
        self.assertEqual(content_filter.checkMessage("wtf"), False)
        self.assertEqual(content_filter.checkMessage("how u"), False)
        
        content_filter.useCustomList(['testing', 'check', 'wtf', 'how u'])
        self.assertEqual(content_filter.checkMessage("fuck"), False)
        self.assertEqual(content_filter.checkMessage("bitch"), False)
        self.assertEqual(content_filter.checkMessage("ass"), False)
        self.assertEqual(content_filter.checkMessage("nigger"), False)
        self.assertEqual(content_filter.checkMessage("dildo"), False)
        self.assertEqual(content_filter.checkMessage("testing"), True)
        self.assertEqual(content_filter.checkMessage("check"), True)
        self.assertEqual(content_filter.checkMessage("wtf"), True)
        self.assertEqual(content_filter.checkMessage("how u"), True)
        self.assertEqual(content_filter.checkMessage("shit"), False)
        self.assertEqual(content_filter.checkMessage("pussy"), False)
        self.assertEqual(content_filter.checkMessage("dick"), False)