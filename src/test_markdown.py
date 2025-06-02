import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_delimiter, extract_md_images, \
                    extract_md_links, split_nodes_image, split_nodes_link,\
                    text_to_textnodes

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

    def test_extract_md_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif")], extract_md_images(text))

    def test_extract_md_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], extract_md_links(text))

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        print(nodes)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
