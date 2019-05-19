# -*- coding: utf-8 -*-

    
def join(stroke_parts):
    return "".join(str(x) for x in stroke_parts)

    
def split(stroke):
    stroke_parts = []
    stroke_part = ""
    for char in stroke:
        if char is "[":
            if stroke_part:
                stroke_parts.append(stroke_part)
            stroke_part = "["
        elif char is "]":
            if stroke_part:
                stroke_part += char
                stroke_parts.append(stroke_part)
            stroke_part = ""
        else:
            stroke_part += char
    if stroke_part:
        stroke_parts.append(stroke_part)
    return stroke_parts 


def remove_markup(stroke):
    stripped_stroke = remove_excess_hyphens(stroke)
    stripped_stroke = stripped_stroke.replace("[e|", "")
    stripped_stroke = stripped_stroke.replace("[", "")
    stripped_stroke = stripped_stroke.replace("]", "")
    return stripped_stroke


def remove_excess_hyphens(stroke):
    # if there's a vowel or *, no hyphens are needed at all
    if "[e|" in stroke or "[*]" in stroke:
        return stroke.replace("-", "")
    # otherwise the first hyphen is left but all others are removed
    stroke_parts = split(stroke)
    first_hyphen_seen = False
    stripped_stroke_parts = []
    for stroke_part in stroke_parts:
        if stroke_part.startswith("[-"):
            if not first_hyphen_seen:
                first_hyphen_seen = True
                stripped_stroke_parts.append(stroke_part)
                continue
            stripped_stroke_parts.append(stroke_part.replace("[-", "["))
        else:
            stripped_stroke_parts.append(stroke_part)
    return join(stripped_stroke_parts)
    
