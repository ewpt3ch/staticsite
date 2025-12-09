import os

from shutil import rmtree
from mdtohtml import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def gen_page_recurse(src, temp, dest):
    tree = os.listdir(src)
    print(tree)
    for item in tree:
        print(item)
        if os.path.isfile(os.path.join(src, item)):
            generate_page(os.path.join(src, item),
                          temp,
                          os.path.join(dest, "index.html"))
        else:
            os.mkdir(os.path.join(dest, item))
            gen_page_recurse(os.path.join(src, item),
                             temp,
                             os.path.join(dest, item))


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
