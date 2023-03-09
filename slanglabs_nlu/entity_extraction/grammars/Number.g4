grammar Number;

// fragments
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

numbers_utterance: prefix? discards* (number_pattern (' '* (WORD | CONJUNCTION) ' '*)? spl_discard?)? ((' '* (WORD | CONJUNCTION) ' '*)+ number_pattern? (' '* (WORD | CONJUNCTION)' '*)? spl_discard?)* discards* suffix?;
discards: (spl_discard (' '* (WORD | CONJUNCTION)' '*)*);

ranges_utterance: prefix? (range_pattern | (number_pattern (' '? WORD ' '?)? spl_discard?))? ((' '? WORD ' '?)+ (range_pattern | number_pattern (' '? WORD ' '?)? spl_discard?))* suffix?;

range_pattern: ' '? 'between' ' '? number_pattern CONJUNCTION number_pattern
    | ' '? 'between' ' '? number_pattern 'to ' number_pattern
    | ' '? number_pattern 'to ' number_pattern
    | ' '? 'of' ' '? number_pattern CONJUNCTION number_pattern;

number_pattern: (billions_format | crores_format | millions_format | lakhs_format | thousands_format | hundreds_format | tens_format | units_format | literal_format);

literal_format: (' '? (WORD_NUMBER_UNITS | NUMBER_UNITS) ' '?)+ fractional_format?;

billions_format: prefix_lakhs? (WORD_NUMBER_BILLIONS | spl_billions) CONJUNCTION? suffix_lakhs? CONJUNCTION? fractional_format? | NUMBER_BILLIONS;

crores_format: prefix_crores? (WORD_NUMBER_CRORES | spl_crores) CONJUNCTION? suffix_crores? CONJUNCTION? fractional_format? | NUMBER_CRORES;

lakhs_format: prefix_lakhs? (WORD_NUMBER_LAKHS | spl_lakhs) CONJUNCTION? suffix_lakhs? CONJUNCTION? fractional_format? | NUMBER_LAKHS;

millions_format: prefix_lakhs? (WORD_NUMBER_MILLIONS | spl_millions) CONJUNCTION? suffix_lakhs? CONJUNCTION? fractional_format? | NUMBER_MILLIONS;

thousands_format: prefix_thousands? (WORD_NUMBER_THOUSANDS | spl_thousands) CONJUNCTION? suffix_thousands? CONJUNCTION? fractional_format? | NUMBER_THOUSANDS
    | (WORD_NUMBER_TENS | NUMBER_TENS) (WORD_NUMBER_TENS | NUMBER_TENS)
    | NUMBER_THOUSANDS (hundreds_format | tens_format | units_format)
    | NUMBER_THOUSANDS
    | prefix_thousands (' '? 'k' (' ' | EOF));

hundreds_format: prefix_hundreds? (WORD_NUMBER_HUNDREDS) CONJUNCTION? suffix_hundreds? CONJUNCTION? fractional_format?
    | spl_hundreds
    | spl_hundreds_1
    | spl_hundreds_2
    | spl_hundreds_3
    | spl_hundreds_4
    | NUMBER_HUNDREDS
    | (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_UNITS | NUMBER_UNITS)
    | (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_TENS | NUMBER_TENS)
    | (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_TENS | NUMBER_TENS) (WORD_NUMBER_UNITS | NUMBER_UNITS);

tens_format: ((WORD_NUMBER_TENS units_format?) | (NUMBER_TENS units_format?)) CONJUNCTION? fractional_format?;

units_format: (WORD_NUMBER_UNITS | NUMBER_UNITS) CONJUNCTION? fractional_format?;

fractional_format: WORD_NUMBER_FRACTIONS
    | (' '? ('point' | 'dot') ' '? (WORD_NUMBER_UNITS | NUMBER_UNITS)*)
    | (' '? ('point' | 'dot') ' '? ((WORD_NUMBER_TENS units_format?) | (NUMBER_TENS units_format?)));

prefix_crores: (units_format | tens_format | hundreds_format | thousands_format | lakhs_format);
suffix_crores: (units_format | tens_format | hundreds_format | thousands_format | lakhs_format);

prefix_lakhs: (units_format | tens_format | hundreds_format | thousands_format);
suffix_lakhs: (units_format | tens_format | hundreds_format | thousands_format);

prefix_thousands: (units_format | tens_format | hundreds_format);
suffix_thousands: (units_format | tens_format | hundreds_format);

prefix_hundreds: (units_format | tens_format);
suffix_hundreds: (units_format | tens_format);

spl_tens: 'to ' (WORD_NUMBER_UNITS | NUMBER_UNITS) ' '?;
spl_hundreds: 'to ' (WORD_NUMBER_TENS | NUMBER_TENS) ' '? | 'to ' WORD_NUMBER_HUNDREDS;
spl_hundreds_1: spl_tens (WORD_NUMBER_UNITS | NUMBER_UNITS);
spl_hundreds_2: (WORD_NUMBER_UNITS | NUMBER_UNITS) spl_tens;
spl_hundreds_3: (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_UNITS | NUMBER_UNITS) spl_epilogue;
spl_hundreds_4: spl_tens spl_epilogue;
spl_thousands: 'to ' WORD_NUMBER_THOUSANDS;
spl_lakhs: 'to ' WORD_NUMBER_LAKHS;
spl_millions: 'to ' WORD_NUMBER_MILLIONS;
spl_crores: 'to ' WORD_NUMBER_CRORES;
spl_billions: 'to ' WORD_NUMBER_BILLIONS;
spl_epilogue: 'to to ';
spl_discard: ('to ' ' '* WORD)
    | (' '* ('amounting' | 'want' | 'wanting' | 'like' | 'liking') ' '*) 'to ';

prefix: (' '? (WORD | CONJUNCTION) ' '?)*;
suffix: (' '? (WORD | CONJUNCTION) ' '?)*;

WORD_NUMBER_FRACTIONS: (' '? ('half' | 'quarter' | 'three fourth' | 'three fourths') ' '?);

WORD_NUMBER_UNITS: ' '? ('o' | 'oh' | 'not' | 'zero' | 'one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine') (' ' | EOF);
WORD_NUMBER_TENS:  ' '? ('ten' | 'eleven' | 'twelve' | 'thirteen'| 'fourteen'| 'fifteen' | 'sixteen' | 'seventeen' | 'eighteen' | 'nineteen'
     | 'twenty' | 'thirty' | 'forty' | 'fifty' | 'sixty' | 'seventy' | 'eighty' | 'ninety') (' ' | EOF);
WORD_NUMBER_HUNDREDS: ' '? ('hundred' | 'hundreds') (' ' | EOF);
WORD_NUMBER_THOUSANDS: ' '? ('thousand' | 'thousands') (' ' | EOF);
WORD_NUMBER_LAKHS: ' '? ('lakh' | 'lakhs' | 'lac' | 'lacs' | 'lax') (' ' | EOF);
WORD_NUMBER_MILLIONS: ' '? ('million' | 'millions') (' ' | EOF);
WORD_NUMBER_CRORES: ' '? ('crore' | 'crores') (' ' | EOF);
WORD_NUMBER_BILLIONS: ' '? ('billion' | 'billions') (' ' | EOF);
CONJUNCTION: ' '? ('and' | 'of') (' ' | EOF);
ART: ('a' | 'an' | 'the') -> skip;
PUNCT: (',' | '\'' | '"' | '!' | '?') -> skip;

NUMBER_UNITS: ' '? DIGIT ([.]DIGIT+)* ' '?;
NUMBER_TENS: ' '? DIGIT DIGIT ([.]DIGIT+)* ' '?;
NUMBER_HUNDREDS: ' '? DIGIT DIGIT DIGIT ([.]DIGIT+)* ' '?;
NUMBER_THOUSANDS: ' '? DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;
NUMBER_LAKHS: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;
NUMBER_MILLIONS: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;
NUMBER_CRORES: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;
NUMBER_BILLIONS: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;

WHITESPACE: [ \t]+ -> skip;
WORD: LETTER+;
NUMBER: DIGIT+([.,]DIGIT+)?;
