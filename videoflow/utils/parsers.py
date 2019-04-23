def parse_label_map(path_to_labels: str):
    '''
    Arguments:
    - path_to_labels (str): path to pbtx file

    Returns:
    - dict of form { id(int) : label(str)}
    '''
    with open(path_to_labels, "r") as f:
        text = f.read()
    entry_pairs = []
    a = text.find('item')
    while a != -1:
        b = text.find('id:', a)
        b1 = text.find('\n', b)
        index = int(text[b + len("id:"): b1])
        c = text.find('name:', a)
        c3 = text.find('\n', c)
        c1 = max(text.find("'", c), text.find('"', c))
        c2 = max(text.find("'", c1), text.find('"', c1))
        klass_name = text[c1 + 1: c2]
        entry_pairs.append((index, klass_name))
        a = text.find('item', c)
    return dict(entry_pairs)
