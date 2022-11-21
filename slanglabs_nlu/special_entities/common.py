# Relative Time

before_words = [
    "before today",
    "before",
    "sooner",
    "ago",
    "previous",
    "last",
    "since",
]

after_words = [
    "after",
    "later",
    "past",
    "post",
    "next",
    "from today",
    "from now",
    "coming",
    "this",
    "upcoming",
]

before_words_regex = '|'.join(before_words)
before_words_regex = '({})'.format(before_words_regex)
after_words_regex = '|'.join(after_words)
after_words_regex = '({})'.format(after_words_regex)
