import unittest

from block_markdown import (markdown_to_blocks,
                            block_to_block_type,
                            block_type_code,
                            block_type_ordered_list,
                            block_type_unordered_list,
                            block_type_quote,
                            block_type_paragraph,
                            block_type_heading,
                            block_type_paragraph_to_html,
                            block_type_heading_to_html)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        self.assertEqual([
            'This is **bolded** paragraph',
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
            '* This is a list\n* with items'
        ],
            markdown_to_blocks(markdown))

    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_type_paragraph_to_html(self):
        block = "paragraph"
        self.assertEqual("<p>paragraph</p>",
                         block_type_paragraph_to_html(block).to_html())

    def test_block_type_heading_to_html(self):
        block = "# heading"
        self.assertEqual("<h1>heading</h1>",
                         block_type_heading_to_html(block).to_html())


if __name__ == "__main__":
    unittest.main()
