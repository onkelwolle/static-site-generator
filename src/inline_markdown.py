import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
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


def split_nodes_image(old_nodes):
    list_of_text_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            list_of_text_nodes.append(old_node)
        else:
            list_of_text_nodes.extend(
                split_nodes_image_recursive(old_node.text))
    return list_of_text_nodes


def split_nodes_image_recursive(text, list_of_text_nodes=None):
    if list_of_text_nodes is None:
        list_of_text_nodes = []

    extracted_img_tuples = extract_markdown_images(text)
    if len(extracted_img_tuples) == 0:
        if text != "":
            list_of_text_nodes.append(TextNode(text, text_type_text))
    else:
        extracted_img_tuple = extracted_img_tuples[0]
        split_text = text.split(
            f"![{extracted_img_tuple[0]}]({extracted_img_tuple[1]})", 1)
        if split_text[0] != "":
            list_of_text_nodes.append(
                TextNode(split_text[0], text_type_text))
        list_of_text_nodes.append(
            TextNode(extracted_img_tuple[0], text_type_image, extracted_img_tuple[1]))
        split_nodes_image_recursive(split_text[1], list_of_text_nodes)
    return list_of_text_nodes


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_link(old_nodes):
    list_of_text_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            list_of_text_nodes.append(old_node)
        else:
            list_of_text_nodes.extend(
                split_nodes_links_recursive(old_node.text))
    return list_of_text_nodes


def split_nodes_links_recursive(text, list_of_text_nodes=None):
    if list_of_text_nodes is None:
        list_of_text_nodes = []

    extracted_img_tuples = extract_markdown_links(text)
    if len(extracted_img_tuples) == 0:
        if text != "":
            list_of_text_nodes.append(TextNode(text, text_type_text))
    else:
        extracted_link_tuple = extracted_img_tuples[0]
        split_text = text.split(
            f"[{extracted_link_tuple[0]}]({extracted_link_tuple[1]})", 1)
        if split_text[0] != "":
            list_of_text_nodes.append(
                TextNode(split_text[0], text_type_text))
        list_of_text_nodes.append(
            TextNode(extracted_link_tuple[0], text_type_link, extracted_link_tuple[1]))
        split_nodes_links_recursive(split_text[1], list_of_text_nodes)

    return list_of_text_nodes
