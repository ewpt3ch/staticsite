import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newnodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newnodes.append(node)
            continue
        texts = node.text.split(delimiter)
        if len(texts) % 2 == 0:
            raise ValueError('markdown not valid, tags not closed')
        splitnodes = []
        for i in range(len(texts)):
            if texts[i] == '':
                continue
            if i % 2 == 0:
                splitnodes.append(TextNode(texts[i], TextType.TEXT))
            else:
                splitnodes.append(TextNode(texts[i], text_type))
        newnodes.extend(splitnodes)
    return newnodes

def extract_md_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_md_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    newnodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newnodes.append(node)
            continue
        origtext = node.text
        images = extract_md_images(node.text)
        if len(images) == 0:
            newnodes.append(node)
            continue
        for image in images:
            texts = origtext.split(f"![{image[0]}]({image[1]})", 1)
            if len(texts) != 2:
                raise ValueError("invalid markdown, tag not closed")
            if texts[0] != "":
                newnodes.append(TextNode(texts[0], TextType.TEXT))
            newnodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            origtext = texts[1]
        if origtext != "":
            newnodes.append(TextNode(origtext, TextType.TEXT))
    return newnodes

def split_nodes_link(old_nodes):
    newnodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newnodes.append(node)
            continue
        origtext = node.text
        links = extract_md_links(node.text)
        if len(links) == 0:
            newnodes.append(node)
            continue
        for link in links:
            texts = origtext.split(f"[{link[0]}]({link[1]})", 1)
            if len(texts) != 2:
                    raise ValueError("invalid markdown, tag not closed")
            if texts[0] != "":
                newnodes.append(TextNode(texts[0], TextType.TEXT))
            newnodes.append(TextNode(link[0], TextType.LINK, link[1]))
            origtext = texts[1]
        if origtext != "":
            newnodes.append(TextNode(origtext, TextType.TEXT))
    return newnodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def md_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    blocks = []
    for b in raw_blocks:
        if b != '':
            blocks.append(b.strip())

    return blocks

def extract_title(text):
    blocks = md_to_blocks(text)
    for block in blocks:
        if block.startswith('# '):
            return block.strip('# ')
    raise ValueError("no h1 in markdown")
