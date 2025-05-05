import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_delimiter

class Testsplitnodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code` block", TextType.TEXT)
        self.assertEqual(
if __name__ == "__main__":
    unittest.main()
