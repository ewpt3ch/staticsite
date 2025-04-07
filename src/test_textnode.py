import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.123.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.321.com")
        self.assertNotEqual(node, node2)

    def test_texttype_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text_noteq(self):
        node = TextNode("This is a node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_noteq(self):
        node = TextNode("This is a node", TextType.CODE, "123.www.com")
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a node", TextType.CODE, "123.www.com")
        self.assertEqual(
                "TextNode(This is a node, code, 123.www.com)", repr(node)
                )







if __name__ == "__main__":
    unittest.main()
