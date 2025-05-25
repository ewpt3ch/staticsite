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
    return(newnodes + splitnodes)

def extract_md_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_md_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
