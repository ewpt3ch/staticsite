from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'para'
    HEADING = 'head'
    CODE = 'code'
    QUOTE = 'quote'
    UNLIST = 'ulist'
    ORLIST = 'olist'

def md_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    blocks = []
    for b in raw_blocks:
        if b == '':
            continue
        b = b.strip()
        blocks.append(b)

    return blocks

def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith(('#', '##', '###', '####', '#####', '######')):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNLIST
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORLIST

    else:
        return BlockType.PARAGRAPH

