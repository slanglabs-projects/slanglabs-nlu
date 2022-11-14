grammar Number;

// fragments
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

payments_utterance: prefix? (number_pattern (' '? WORD ' '?)? spl_discard?)? ((' '? WORD ' '?)+ number_pattern (' '? WORD ' '?)? spl_discard?)* suffix?;

real_estate_utterance: prefix? (range_pattern | (number_pattern (' '? WORD ' '?)? spl_discard?))? ((' '? WORD ' '?)+ (range_pattern | number_pattern (' '? WORD ' '?)? spl_discard?))* suffix?;

range_pattern: ' '? 'between' ' '? number_pattern CONJUNCTION number_pattern
    | ' '? 'between' ' '? number_pattern 'to ' number_pattern
    | ' '? number_pattern 'to ' number_pattern
    | ' '? 'of' ' '? number_pattern CONJUNCTION number_pattern;

number_pattern: (crores_format | lakhs_format | thousands_format | hundreds_format | tens_format | units_format);

crores_format: prefix_crores? (WORD_NUMBER_CRORES | spl_crores) CONJUNCTION? suffix_crores? CONJUNCTION? WORD_NUMBER_FRACTIONS? | NUMBER_CRORES;

lakhs_format: prefix_lakhs? (WORD_NUMBER_LAKHS | spl_lakhs) CONJUNCTION? suffix_lakhs? CONJUNCTION? WORD_NUMBER_FRACTIONS? | NUMBER_LAKHS;

thousands_format: prefix_thousands? (WORD_NUMBER_THOUSANDS | spl_thousands) CONJUNCTION? suffix_thousands? CONJUNCTION? WORD_NUMBER_FRACTIONS? | NUMBER_THOUSANDS
    | (WORD_NUMBER_TENS | NUMBER_TENS) (WORD_NUMBER_TENS | NUMBER_TENS)
    | NUMBER_THOUSANDS (hundreds_format | tens_format | units_format)
    | NUMBER_THOUSANDS;

hundreds_format: prefix_hundreds? (WORD_NUMBER_HUNDREDS) CONJUNCTION? suffix_hundreds? CONJUNCTION? WORD_NUMBER_FRACTIONS?
    | spl_hundreds
    | spl_hundreds_1
    | spl_hundreds_2
    | spl_hundreds_3
    | spl_hundreds_4
    | NUMBER_HUNDREDS
    | (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_UNITS | NUMBER_UNITS)
    | (WORD_NUMBER_UNITS | NUMBER_UNITS) (WORD_NUMBER_TENS | NUMBER_TENS);

tens_format: ((WORD_NUMBER_TENS units_format?) | (NUMBER_TENS units_format?)) CONJUNCTION? WORD_NUMBER_FRACTIONS?;

units_format: (WORD_NUMBER_UNITS | NUMBER_UNITS) CONJUNCTION? WORD_NUMBER_FRACTIONS?;

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
spl_crores: 'to ' WORD_NUMBER_CRORES;
spl_epilogue: 'to to ';
spl_discard: 'to ' WORD;

prefix: (' '? WORD ' '?)*;
suffix: (' '? WORD ' '?)*;

WORD_NUMBER_FRACTIONS: ' '? ('half' | 'quarter' | 'three fourth' | 'three fourths') ' '?;
WORD_NUMBER_UNITS: ' '? ('oh' | 'not' | 'zero' | 'one' | 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine') ' '?;
WORD_NUMBER_TENS:  ' '? ('ten' | 'eleven' | 'twelve' | 'thirteen'| 'fourteen'| 'fifteen' | 'sixteen' | 'seventeen' | 'eighteen' | 'nineteen'
     | 'twenty' | 'thirty' | 'forty' | 'fifty' | 'sixty' | 'seventy' | 'eighty' | 'ninety') ' '?;
WORD_NUMBER_HUNDREDS: ' '? ('hundred' | 'hundreds') ' '?;
WORD_NUMBER_THOUSANDS: ' '? ('thousand' | 'thousands') ' '?;
WORD_NUMBER_LAKHS: ' '? ('lakh' | 'lakhs' | 'lac' | 'lacs' | 'lax') ' '?;
WORD_NUMBER_CRORES: ' '? ('crore' | 'crores') ' '?;
CONJUNCTION: ' '? 'and' ' '?;
ART: ' '? ('a' | 'an' | 'the') ' '? -> skip;

NUMBER_UNITS: ' '? DIGIT ([.]DIGIT+)* ' '?;
NUMBER_TENS: ' '? DIGIT DIGIT ([.]DIGIT+)* ' '?;
NUMBER_HUNDREDS: ' '? DIGIT DIGIT DIGIT ([.]DIGIT+)* ' '?;
NUMBER_THOUSANDS: ' '? DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;
NUMBER_LAKHS: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;
NUMBER_CRORES: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT+ ([.]DIGIT+)* ' '?;

WHITESPACE: [ \t]+ -> skip;
WORD: LETTER+;
NUMBER: DIGIT+([.,]DIGIT+)?;
