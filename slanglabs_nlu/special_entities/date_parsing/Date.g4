grammar Date;

// fragments
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

// parser support
//utterance: prefix? date_pattern suffix?
//    | prefix? date_pattern (' '? WORD ' '?)* date_pattern suffix?
//    | prefix? date_pattern (' '? WORD ' '?)* date_pattern (' '? WORD ' '?)* date_pattern suffix?;

utterance: prefix? date_pattern? ((' '? WORD ' '?)* date_pattern)* suffix?;
// utterance: prefix? (date_pattern ((' '? WORD ' '?)* date_pattern?))? suffix?;

date_pattern: relative_form | year_form | month_form | week_form | day_form | literal_form;

// literal_form: NUMBER;
literal_form: DATE_NUMBER;

relative_form: relative_year | relative_month | relative_week | relative_day;

year_form: month_form year time?
    | year month_form time?
    | (ORDINAL | ORDINALSTR) MOTY year
    | year;
year: NEXT_YEAR
    | PREV_YEAR
    | CURR_YEAR
    | LITERAL_YEAR;
relative_year: RELATIVE_PREFIX? ART? NUMBER? (RELATIVE_YEAR | (RELATIVE_YEAR_NEXT | RELATIVE_YEAR_PREV) (day | week | month)?);

month_form: ART? (NUMBER | ORDINAL | ORDINALSTR) 'of'? (month | MOTY) 'at'? time?
    | month (NUMBER | ORDINAL | ORDINALSTR) 'at'? time?
    | ART? (NUMBER | ORDINAL | ORDINALSTR) 'at'? time?
    | day 'of'? (month | MOTY)
    | double_ordinal_month
    | literal_month
    | month
    | MOTY;
month: NEXT_MONTH | PREV_MONTH | CURR_MONTH;
relative_month: RELATIVE_PREFIX? ART? NUMBER? (RELATIVE_MONTH | (RELATIVE_MONTH_NEXT | RELATIVE_MONTH_PREV) (day | week)?);
literal_month: NUMBER MOTY | MOTY NUMBER | MOTY (ORDINAL | ORDINALSTR);
double_ordinal_month: ART? (ORDINAL | ORDINALSTR) (ORDINAL | ORDINALSTR) 'month'
    | ART? (ORDINAL | ORDINALSTR) 'month' (ORDINAL | ORDINALSTR);

week_form: week | day? 'of'? week 'at'? time? | week day? 'at'? time?;
week: NEXT_WEEK | PREV_WEEK | CURR_WEEK | NEXT_WEEKEND | PREV_WEEKEND;
relative_week: RELATIVE_PREFIX? ART? NUMBER? (RELATIVE_WEEK | (RELATIVE_WEEK_NEXT | RELATIVE_WEEK_PREV) (day | month)?);

day_form: day 'at'? time? | time? day | day | time day?;
day: DOTW | NEXT_DAY | PREV_DAY | CURR_DAY | NEXT2_DAY | PREV2_DAY | relative_day;
relative_day: (
    (RELATIVE_PREFIX? (ART | NUMBER) (RELATIVE_DAY | (RELATIVE_DAY_NEXT | RELATIVE_DAY_PREV) day?))
    | RELATIVE_PREFIX? ART? (RELATIVE_DAY | (RELATIVE_DAY_NEXT | RELATIVE_DAY_PREV) day?));

time: TIME_RANGE | ' '? NUMBER tod | ' '? NUMBER ' '? 'o clock' | ' '? TIME tod?;
tod: ('am' | 'pm' | 'noon' | 'afternoon' | 'morning' | 'evening' | 'night');

prefix: (' '? WORD ' '?)*;
suffix: (' '? WORD ' '?)*;

// lexer support
NEXT_DAY: ' '? ('tomorrow' | ART? NEXT+ 'day' | ART? NEXT+ DOTW) ' '?;
PREV_DAY: ' '? ('yesterday' | ART? PREV+ 'day' | ART? PREV+ DOTW) ' '?;
CURR_DAY: (' '? ('today' | 'tonight' | 'now' | 'this ' DOTW) ' '?) | (' '? 'today\'s' ' '? 'date'? ' '?);
NEXT2_DAY: ' '? ART? 'day after tomorrow' ' '?;
PREV2_DAY: ' '? ART? 'day before yesterday' ' '?;
RELATIVE_DAY: ' '? ('days' | 'day') ' '?;
RELATIVE_DAY_NEXT: RELATIVE_DAY RELATIVE_NEXT;
RELATIVE_DAY_PREV: RELATIVE_DAY RELATIVE_PREV;

DOTW: ' '? (
    'sunday'
    | 'monday'
    | 'tuesday'
    | 'wednesday'
    | 'thursday'
    | 'friday'
    | 'saturday'
) ' '?;

NEXT_WEEK: ART? NEXT+ 'week' ' '? | ART? NEXT+ DOTW ' '?;
PREV_WEEK: ART? PREV+ 'week' ' '? | ART? PREV+ DOTW ' '?;
CURR_WEEK: 'this week' ' '?;
RELATIVE_WEEK: ' '? ('weeks' | 'week' | 'fortnight' | 'fortnights') ' '?;
RELATIVE_WEEK_NEXT: RELATIVE_WEEK RELATIVE_NEXT;
RELATIVE_WEEK_PREV: RELATIVE_WEEK RELATIVE_PREV;
NEXT_WEEKEND: ART? (NEXT | ' '? 'this' ' '?)? 'weekend' ' '?;
PREV_WEEKEND: ART? PREV? 'weekend' ' '?;

NEXT_MONTH: ART? NEXT+ 'month' ' '? | ART? NEXT+ MOTY ' '?;
PREV_MONTH: ART? PREV+ 'month' ' '? | ART? PREV+ MOTY ' '?;
CURR_MONTH: ' '? 'this month' ' '?;
MOTY: ' '? (
    'january' | 'jan'
    | 'february' | 'feb'
    | 'march' | 'mar'
    | 'april' | 'apr'
    | 'may'
    | 'june' | 'jun'
    | 'july' | 'jul'
    | 'august' | 'aug'
    | 'september' | 'sep' | 'sept'
    | 'october' | 'oct'
    | 'november' | 'nov'
    | 'december' | 'dec'
    ) ' '?;
RELATIVE_MONTH: ' '? ('months' | 'month') ' '?;
RELATIVE_MONTH_NEXT: RELATIVE_MONTH RELATIVE_NEXT;
RELATIVE_MONTH_PREV: RELATIVE_MONTH RELATIVE_PREV;

NEXT_YEAR: ART? NEXT+ 'year';
PREV_YEAR: ART? PREV+ 'year';
CURR_YEAR: ' '? 'this year' ' '?;
LITERAL_YEAR: ' '? ('19' | '20')DIGIT DIGIT ' '?;
RELATIVE_YEAR: ' '? ('years' | 'year') ' '?;
RELATIVE_YEAR_NEXT: RELATIVE_YEAR RELATIVE_NEXT;
RELATIVE_YEAR_PREV: RELATIVE_YEAR RELATIVE_PREV;

RELATIVE_NEXT: ' '? ('from' | 'after' | 'later') ' '? -> skip;
RELATIVE_PREV: ' '? ('before' | 'earlier' | 'ago' | 'back') ' '? -> skip;
RELATIVE_PREFIX: ' '? 'in' ' '? -> skip;

NEXT: ' '? ('next' | 'following' | 'coming' | 'upcoming') ' '? -> skip;
PREV: ' '? ('last' | 'previous' | 'past') ' '? -> skip;

ART: (' a ' | ' an ' | ' the ') -> skip;
CONJUNCTION: (' to ' | ' at ' | ' of ') -> skip;

AM: ' '? ('morning' | 'am') ' '? -> skip;
PM: ' '? ('evening' | 'night' | 'pm') ' '? -> skip;
NOON: ' '? ('afternoon' | 'noon') ' '? -> skip;

ORDINAL: ' '? NUMBER('th'|'st'|'nd'|'rd') ' '?;

ORDINALSTR: ' '? 'first' ' '?
     | ' '? 'second' ' '?
     | ' '? 'third' ' '?
     | ' '? 'fourth' ' '?
     | ' '? 'fifth' ' '?
     | ' '? 'sixth' ' '?
     | ' '? 'seventh' ' '?
     | ' '? 'eighth' ' '?
     | ' '? 'ninth' ' '?
     | ' '? 'tenth' ' '?
     | ' '? 'eleventh' ' '?
     | ' '? 'twelfth' ' '?
     | ' '? 'thirteenth' ' '?
     | ' '? 'fourteenth' ' '?
     | ' '? 'fifteenth' ' '?
     | ' '? 'sixteenth' ' '?
     | ' '? 'seventeenth' ' '?
     | ' '? 'eighteenth' ' '?
     | ' '? 'nineteenth' ' '?
     | ' '? 'twentieth' ' '?
     | ' '? 'twenty first' ' '?
     | ' '? 'twenty second' ' '?
     | ' '? 'twenty third' ' '?
     | ' '? 'twenty fourth' ' '?
     | ' '? 'twenty fifth' ' '?
     | ' '? 'twenty sixth' ' '?
     | ' '? 'twenty seventh' ' '?
     | ' '? 'twenty eighth' ' '?
     | ' '? 'twenty ninth' ' '?
     | ' '? 'thirtieth' ' '?
     | ' '? 'thirty first' ' '?;

WHITESPACE: [ \t]+ -> skip;
PUNCT: [,.'"]+ -> skip;
DATE_NUMBER: ' '? DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT? ' '?;
NUMBER: ' '? DIGIT+ ' '?;
WORD: LETTER+;
TIME: NUMBER ':' NUMBER;
TIME_RANGE: TIME CONJUNCTION? TIME;
