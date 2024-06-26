import os
from pathlib import Path
from block_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    replaced_template = template.replace(
        "{{ Title }}", extract_title(markdown))

    html_nodes = markdown_to_html_node(markdown)

    replaced_template = replaced_template.replace(
        "{{ Content }}", html_nodes.to_html())

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    dest_file = open(dest_path, "w")
    dest_file.write(replaced_template)
    dest_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    items_in_dir = os.listdir(dir_path_content)
    for item in items_in_dir:
        from_path = os.path.join(dir_path_content, item)
        to_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path, template_path, to_path)
        else:
            generate_pages_recursive(from_path, template_path, to_path)
