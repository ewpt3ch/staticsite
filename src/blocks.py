def md_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    blocks = []
    for b in raw_blocks:
        if b == '':
            continue
        b = b.strip()
        blocks.append(b)

    return blocks
