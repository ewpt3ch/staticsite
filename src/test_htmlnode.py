import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "a nice paragraph we have here", None, {"style": "bold"})
        self.assertEqual(f' style="bold"', node.props_to_html())

if __name__ == "__main__":
    unittest.main()
