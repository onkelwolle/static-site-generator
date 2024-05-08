import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_with_some_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(
        ), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_with_nested_parent(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ])
        self.assertEqual(node.to_html(
        ), "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")


if __name__ == "__main__":
    unittest.main()
