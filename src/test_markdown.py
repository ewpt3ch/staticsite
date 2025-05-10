import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_delimiter

class Testsplitnodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code` block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertListEqual(new_nodes,
                             [TextNode('This is text with a ', TextType.TEXT),
                              TextNode('code', TextType.CODE),
                              TextNode(' block', TextType.TEXT)]
                              )

    def test_ital(self):
        node = TextNode("This is text with a _italic_ block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertListEqual(new_nodes,
                             [TextNode('This is text with a ', TextType.TEXT),
                              TextNode('italic', TextType.ITALIC),
                              TextNode(' block', TextType.TEXT)]
                              )

    def test_bold(self):
        node = TextNode("This is text with a **bold** block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual(new_nodes,
                             [TextNode('This is text with a ', TextType.TEXT),
                              TextNode('bold', TextType.BOLD),
                              TextNode(' block', TextType.TEXT)]
                              )

    def test_all(self):
        node = TextNode("This is text with all **bold** `code` _italic_ block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual(new_nodes,
                             [TextNode('This is text with all ', TextType.TEXT),
                              TextNode('bold', TextType.BOLD),
                              TextNode(' `code` _italic_ block', TextType.TEXT)]
                              )

    def test_only(self):
        node = TextNode("**bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual(new_nodes,
                              [TextNode('bold', TextType.BOLD)]
                              )

    def test_notclosed(self):
        node = TextNode("bold**", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], '**', TextType.BOLD)

if __name__ == "__main__":
    unittest.main()
