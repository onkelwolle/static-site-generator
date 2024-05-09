import unittest

from inline_markdown import (split_nodes_delimiter,
                             extract_markdown_images,
                             extract_markdown_links,
                             split_nodes_image,
                             split_nodes_link)
from textnode import (TextNode,
                      text_type_text,
                      text_type_bold,
                      text_type_italic,
                      text_type_code,
                      text_type_link,
                      text_type_image)


class TestInlineMarkdown(unittest.TestCase):

    def test_split_with_code(self):
        node = TextNode(
            "This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        self.assertEqual([
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ], new_nodes)

    def test_split_with_bold(self):
        node = TextNode(
            "This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

        self.assertEqual([
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ], new_nodes)

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(
            [
                ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
            ],
            extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"

        self.assertEqual(
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another")
            ],
            extract_markdown_links(text))

    def test_split_nodes_two_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and some more text",
            text_type_text,
        )

        self.assertEqual([
            TextNode("This is text with an ", "text", None),
            TextNode(
                "image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", "text", None),
            TextNode("second image", "image",
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode(" and some more text", "text", None)
        ],
            split_nodes_image([node]))

    def test_split_nodes_only_image(self):
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text,
        )

        self.assertEqual([
            TextNode(
                "image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        ],
            split_nodes_image([node]))

    def test_split_nodes_two_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text,
        )

        self.assertEqual([
            TextNode("This is text with a ", "text", None),
            TextNode("link", "link", "https://www.example.com"),
            TextNode(" and ", "text", None),
            TextNode("another", "link", "https://www.example.com/another")
        ],
            split_nodes_link([node]))


if __name__ == "__main__":
    unittest.main()
