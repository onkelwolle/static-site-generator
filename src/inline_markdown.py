import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_text_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            list_of_text_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise ValueError("Invalid Markdown syntax, section not closed")
            for i in range(len(split_node)):
                if split_node[i] == "":
                    continue
                if i % 2 == 0:
                    list_of_text_nodes.append(
                        TextNode(split_node[i], text_type_text))
                else:
                    list_of_text_nodes.append(
                        TextNode(split_node[i], text_type))
    return list_of_text_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
