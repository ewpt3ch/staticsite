import unittest

from blocks import md_to_blocks, block_to_block_type, BlockType

class Testsplitnodes(unittest.TestCase):

    def test_md_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = md_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_md_to_blocks_toomanylines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
"""
        blocks = md_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_onelinepara(self):
        block = "This is **bolded** paragraph"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_block_heading(self):
        block = "# this is a heading"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_block_code(self):
        block = "```\nthis is a code\nblock on many line\n```"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.CODE)

    def test_block_quote(self):
        block = "> this is a\n> quote"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.QUOTE)

    def test_block_ul(self):
        block = "- this is\n- an unordered\n- list"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.UNLIST)

    def test_block_ol(self):
        block = "1. this is\n2. an ordered\n3. list"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ORLIST)

if __name__ == "__main__":
    unittest.main()
