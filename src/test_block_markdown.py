import unittest

from block_markdown import (markdown_to_blocks,
                            block_to_block_type,
                            block_type_code,
                            block_type_ordered_list,
                            block_type_unordered_list,
                            block_type_quote,
                            block_type_paragraph,
                            block_type_heading,
                            block_type_paragraph_to_html_node,
                            block_type_heading_to_html_node,
                            block_type_code_to_html_node,
                            block_type_quote_to_html_node,
                            block_type_unordered_list_to_html_node,
                            block_type_ordered_list_to_html_node,
                            markdown_to_html_node)


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
                         block_type_paragraph_to_html_node(block).to_html())

    def test_block_type_heading_to_html(self):
        block = "# heading"
        self.assertEqual("<h1>heading</h1>",
                         block_type_heading_to_html_node(block).to_html())

    def test_block_type_code_to_html(self):
        block = "```\ncode\n```"
        self.assertEqual("<code>\ncode\n</code>",
                         block_type_code_to_html_node(block).to_html())

    def test_block_type_quote_to_html(self):
        block = "> quote\n> more quote"
        self.assertEqual("<blockquote>quote more quote</blockquote>",
                         block_type_quote_to_html_node(block).to_html())

    def test_block_type_unordered_list_to_html(self):
        block = "* list\n* items"
        self.assertEqual("<ul><li>list</li><li>items</li></ul>",
                         block_type_unordered_list_to_html_node(block).to_html())
        block = "- list\n- items"
        self.assertEqual("<ul><li>list</li><li>items</li></ul>",
                         block_type_unordered_list_to_html_node(block).to_html())

    def test_block_type_ordered_list_to_html(self):
        block = "1. list\n2. items"
        self.assertEqual("<ol><li>list</li><li>items</li></ol>",
                         block_type_ordered_list_to_html_node(block).to_html())

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
