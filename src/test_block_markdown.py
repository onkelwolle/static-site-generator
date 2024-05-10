import unittest

from block_markdown import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
