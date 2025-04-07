import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        first_node = TextNode("This is a text node", TextType.BOLD)
        second_node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(first_node, second_node)

    def test_url_none(self):
        first_node = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(first_node.url, None)

    def test_diff_text_type(self):
        first_node = TextNode("This is a text node", TextType.NORMAL)
        second_node = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(first_node, second_node)

if __name__ == "__main__":
    unittest.main()