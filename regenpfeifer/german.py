"""Shared German language data: vowels, diphthongs and prefix inventories.

These lists are used by more than one module -- the syllable splitter and the
word emphasizer both need the vowels, and the same prefixes show up in both --
so they live here instead of being repeated.

The prefix groups are deliberately kept separate rather than merged into one
list, because they answer different questions about the same strings. The
emphasizer's groups say whether a prefix takes the stress; the splitter's says
whether a string is a prefix at a given position. `er` is in both, `zu` is only
a stress question, `unter` is only a boundary question -- so each consumer
takes the view it needs.
"""

VOWELS = ("a", "e", "i", "o", "u", "ä", "ö", "ü")

# Order matters: the first diphthong found in a word carries the stress.
DIPHTHONGS = ("au", "äu", "eu", "ei", "ey", "ai", "ay")

# Inseparable prefixes: never stressed, so the stress falls on the stem.
NEVER_EMPHASIZED_PREFIXES = ("be", "ent", "er", "ver", "zer")

# Additionally unstressed in past participles (gegeben) and in verb forms.
PAST_PARTICIPLE_PREFIX = "ge"
NEVER_EMPHASIZED_VERB_PREFIXES = ("miss", "wider")

# Usually stressed themselves rather than passing the stress to the stem.
USUALLY_EMPHASIZED_PREFIXES = ("dar", "da", "her", "hin", "vor", "zu")

# Separable prefixes, which take the stress (aufbauen -> [e|au]fbauen).
EMPHASIZED_PREFIXES = (
    "ab",
    "an",
    "auf",
    "aus",
    "bei",
    "ein",
    "empor",
    "fort",
    "los",
    "mit",
    "nach",
    "nieder",
    "weg",
    "weiter",
    "wieder",
)

# Prefixes ending in a left connector (er/an). Before a vowel these keep the
# consonant in the preceding syllable (ver|ein, über|all) where a word-internal
# er/an hands it to the following onset (Ja|nu|ar).
#
# Curated, NOT derived from the lists above: whether a string is a prefix
# depends on the word, not just the spelling. `weiter` is a prefix in
# weiterarbeiten but the stem of weitere, and `zer` is a prefix in zerreiben
# but not in Zeremonie -- so membership here is a judgement per entry.
LEFT_CONNECTOR_PREFIXES = (
    "er",
    "an",
    "ver",
    "her",
    "über",
    "ueber",
    "unter",
    "inter",
    "hinter",
    "wider",
    "wieder",
    "außer",
    "ausser",
)
