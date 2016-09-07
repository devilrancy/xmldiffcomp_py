from lxml import etree
import xmltodict  # pip install xmltodict

def normalise_dict(d):
    """
    Recursively convert dict-like object (eg OrderedDict) into plain dict.
    Sorts list values.
    """
    out = {}
    for k, v in dict(d).items():
        if hasattr(v, 'iteritems'):
            out[k] = normalise_dict(v)
        elif isinstance(v, list):
            out[k] = []
            for item in sorted(v):
                if hasattr(item, 'iteritems'):
                    out[k].append(normalise_dict(item))
                else:
                    out[k].append(item)
        else:
            out[k] = v
    return out


def xml_compare(book1,book2):
    """
    Compares two XML documents (as string or etree)

    Does not care about element order
    """
    if not isinstance(a, str):
        a = etree.tostring(a)
    if not isinstance(b, str):
        b = etree.tostring(b)
    a = normalise_dict(xmltodict.parse(a))
    b = normalise_dict(xmltodict.parse(b))
    print a - b
    return a == b
