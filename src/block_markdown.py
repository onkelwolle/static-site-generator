from parentnode import ParentNode
from leafnode import LeafNode

from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n\n")
    stripped_list_of_blocks = []
    for item in list_of_blocks:
        if item.strip() != "":
            stripped_list_of_blocks.append(item.strip())
    return stripped_list_of_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ") or
        block.startswith("## ") or
        block.startswith("### ") or
        block.startswith("#### ") or
        block.startswith("##### ") or
        block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("*"):
        for line in lines:
            if not line.startswith("*"):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("-"):
        for line in lines:
            if not line.startswith("-"):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def block_type_paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    parentnode = ParentNode("p", children)
    return parentnode


def block_type_heading_to_html_node(block):
    stripped_block = block.lstrip("#").lstrip()
    children = text_to_children(stripped_block)

    if block.startswith("# "):
        parentnode = ParentNode("h1", children)
    elif block.startswith("## "):
        parentnode = ParentNode("h2", children)
    elif block.startswith("### "):
        parentnode = ParentNode("h3", children)
    elif block.startswith("#### "):
        parentnode = ParentNode("h4", children)
    elif block.startswith("##### "):
        parentnode = ParentNode("h5", children)
    elif block.startswith("###### "):
        parentnode = ParentNode("h6", children)
    else:
        raise ValueError("Invalid heading level")
    return parentnode


def block_type_code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    children = text_to_children(block.lstrip("```").rstrip("```"))
    parentnode = ParentNode("code", children)
    return parentnode


def block_type_quote_to_html_node(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.lstrip(">").lstrip())
    parentnode = ParentNode("blockquote",
                            text_to_children(" ".join(stripped_lines)))
    return parentnode


def block_type_unordered_list_to_html_node(block):
    lines = block.split("\n")
    leafnodes = []
    for line in lines:
        children = text_to_children(line.lstrip("*").lstrip("-").lstrip())
        leafnodes.append(ParentNode("li", children))
    parentnode = ParentNode("ul", leafnodes)
    return parentnode


def block_type_ordered_list_to_html_node(block):
    lines = block.split("\n")
    leafnodes = []
    i = 1
    for line in lines:
        children = text_to_children(line.lstrip(f"{i}.").lstrip())
        leafnodes.append(ParentNode("li", children))
        i += 1
    parentnode = ParentNode("ol", leafnodes)
    return parentnode


def markdown_to_html_node(markdown):
    list_of_blocks = markdown_to_blocks(markdown)
    list_of_nodes = []
    for block in list_of_blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            list_of_nodes.append(block_type_paragraph_to_html_node(block))
        elif block_type == block_type_heading:
            list_of_nodes.append(block_type_heading_to_html_node(block))
        elif block_type == block_type_code:
            list_of_nodes.append(block_type_code_to_html_node(block))
        elif block_type == block_type_quote:
            list_of_nodes.append(block_type_quote_to_html_node(block))
        elif block_type == block_type_unordered_list:
            list_of_nodes.append(block_type_unordered_list_to_html_node(block))
        elif block_type == block_type_ordered_list:
            list_of_nodes.append(block_type_ordered_list_to_html_node(block))
        else:
            raise ValueError("Invalid block type")

    parentnode = ParentNode("div", list_of_nodes)
    return parentnode
