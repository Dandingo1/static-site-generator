import unittest

from htmlnode import HtmlNode
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
        first_node = TextNode("This is a text node", TextType.TEXT)
        second_node = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(first_node, second_node)    
    
    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()