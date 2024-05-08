import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is a italic text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node with an url", "bold", "https://bood.dev")
        node2 = TextNode("This is a text node with an url", "bold", "https://bood.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()