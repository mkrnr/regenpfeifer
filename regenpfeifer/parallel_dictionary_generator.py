"""Parallel drop-in for dictionary_generator — byte-identical output, multi-core.

Each word's strokes are computed independently across worker processes; the
order-sensitive "first word to claim an outline wins" dedup is then applied in the
ORIGINAL word order, so the result is identical to the sequential generator. This
relies on stroke_generator's deterministic (order-independent) matching.

    python -m regenpfeifer.parallel_dictionary_generator <wordlist.csv> <out.json>
"""

import json
import os
import sys
import time
from collections import OrderedDict
from multiprocessing import Pool, cpu_count

from regenpfeifer.stroke_generator import StrokeGenerator

_ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

_stroke_generator = None


def _read_words(path):
    # Match dictionary_generator.read_word_list: a repeated word keeps its first
    # position and its last type.
    words = OrderedDict()
    with open(path, encoding="utf8") as f:
        for line in f:
            parts = line.rstrip("\n").split(",")
            if len(parts) >= 2:
                words[parts[0]] = parts[1]
    return list(words.items())


def _init(word_list_path):
    global _stroke_generator
    words = _read_words(word_list_path)
    # len>3 filters only the compound-split vocabulary, exactly like the
    # sequential generator's __main__; every word still gets generated.
    _stroke_generator = StrokeGenerator([w for w, t in words if len(w) > 3])


def _work(word_and_type):
    word, word_type = word_and_type
    try:
        strokes = _stroke_generator.generate(word, word_type.split(" ")[0])
    except Exception as exc:
        # Isolate per-word failures so one malformed word can't abort a
        # multi-hour run; treat a failure as "no strokes" and report it.
        print(f"  skipped {word!r}: {exc}", file=sys.stderr)
        strokes = []
    return (word, strokes)


def generate(word_list_path, output_path, workers=None):
    words = _read_words(word_list_path)
    custom_translations_path = os.path.join(
        _ASSET_DIR, "dictionaries", "custom_translations.json"
    )
    with open(custom_translations_path, encoding="utf8") as f:
        custom_translations = json.load(f)
    custom_translated_words = set(custom_translations.values())

    start = time.time()
    results = []
    with Pool(processes=workers, initializer=_init, initargs=(word_list_path,)) as pool:
        for i, result in enumerate(pool.imap(_work, words, chunksize=500)):
            results.append(result)
            if (i + 1) % 10000 == 0:
                elapsed = time.time() - start
                print(
                    f"  {i + 1}/{len(words)} words in {elapsed:.0f}s", file=sys.stderr
                )

    dictionary = dict(custom_translations)
    for word, strokes_list in results:
        if word in custom_translated_words:
            continue
        for strokes in strokes_list:
            if strokes not in dictionary:
                dictionary[strokes] = word

    with open(output_path, "w", encoding="utf8") as f:
        json.dump(dict(sorted(dictionary.items())), f, indent=0, ensure_ascii=False)
    print(
        f"{len(words)} words, {workers or cpu_count()} workers -> "
        f"{len(dictionary)} entries in {time.time() - start:.0f}s"
    )


if __name__ == "__main__":
    generate(sys.argv[1], sys.argv[2])
