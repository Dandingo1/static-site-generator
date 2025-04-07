import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HtmlNode(
            "a", 
            "Click Me!", 
            None, 
            { 
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', html_node.props_to_html()
        )
    
    def test_values(self):
        html_node = HtmlNode("div", "Hello World")
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(html_node.value, "Hello World")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_props_none(self):
        html_node = HtmlNode("a", "Click Me!", None, None)
        self.assertEqual("", html_node.props_to_html())

    def test_repr(self):
        html_node = HtmlNode("a", "Click Me!", None, None)
        string_html_node = "HtmlNode(a, Click Me!, children: None, None)"
        self.assertEqual(string_html_node, html_node.__repr__())

if __name__ == "__main__":
    unittest.main()