def join(stroke_parts):
    return "".join(str(x) for x in stroke_parts)


def split(stroke):
    stroke_parts = []
    stroke_part = ""
    for char in stroke:
        if char == "[":
            if stroke_part:
                stroke_parts.append(stroke_part)
            stroke_part = "["
        elif char == "]":
            if stroke_part:
                stroke_part += char
                stroke_parts.append(stroke_part)
            stroke_part = ""
        else:
            stroke_part += char
    if stroke_part:
        stroke_parts.append(stroke_part)
    return stroke_parts


def remove_markup(strokes):
    strokes = strokes.split("/")
    stripped_strokes = []
    for stroke in strokes:
        stripped_stroke = remove_excess_hyphens(stroke)
        stripped_stroke = stripped_stroke.replace("[e|", "")
        stripped_stroke = stripped_stroke.replace("[", "")
        stripped_stroke = stripped_stroke.replace("]", "")
        stripped_strokes.append(stripped_stroke)
    return "/".join(stripped_strokes)


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


vowels = "AOEU"


def contains_vowel(stripped_stroke):
    for vowel in vowels:
        if vowel in stripped_stroke:
            return True
    return False


before_asterisk = "STKPWHRAO"


def reposition_asterisks(stripped_strokes):
    splitted_stripped_strokes = stripped_strokes.split("/")
    fixed_strokes = []
    for stripped_stroke in splitted_stripped_strokes:
        if "*" in stripped_stroke:
            if "-" in stripped_stroke:
                fixed_strokes.append(stripped_stroke.replace("-", "*"))
                break

            stripped_stroke = stripped_stroke.replace("*", "")
            # vowels_in_stroke=contains_vowel(stripped_stroke)

            index_for_asterisk = None
            current_before_asterisk = before_asterisk
            for i in range(len(stripped_stroke)):
                key = stripped_stroke[i]
                #    if vowels_in_stroke:
                if key in current_before_asterisk:
                    current_before_asterisk = get_all_after_letter(
                        current_before_asterisk, key
                    )
                    continue
                index_for_asterisk = i
                break
            fixed_strokes.append(insert_asterisk(stripped_stroke, index_for_asterisk))
        else:
            fixed_strokes.append(stripped_stroke)

    return "/".join(fixed_strokes)


def get_all_after_letter(letters, letter):
    filtered_letters = ""
    letter_reached = False
    for current_letter in letters:
        if current_letter is letter:
            letter_reached = True
            continue
        if letter_reached:
            filtered_letters = filtered_letters + current_letter
    return filtered_letters


def insert_asterisk(stripped_stroke, index):
    return stripped_stroke[:index] + "*" + stripped_stroke[index:]
