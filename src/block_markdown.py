from parentnode import ParentNode
from leafnode import LeafNode

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


def block_type_paragraph_to_html(block):
    parentnode = ParentNode("p", [LeafNode(None, block)])
    return parentnode
