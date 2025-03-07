# FUTHORCify
Basic translator to turn written english to the futhorc script instead of latin due to random interss

Need a project to do some practist after not making as much as I hopped. As such I am structuring this project in a way I can expand based on intrence.
So parts of this project will be listed in phases, probably won't do all parts but I do better with structured 

REFERENCE INFO

GLYPH CHART,

English Sound - Futhorc letter - Futhor Glyph - Unicode
A                Ac               ᚪ  
B                Berc             ᛒ
C                Cen              ᚳ
D                Daeg             ᛞ
E                Eh               ᛖ
F                Feh              ᚠ
G                Geofu            ᚷ
H                Haegil           ᚻ
I                Is               ᛁ
J                Geal             ᛡ 
K                Calc             ᛣ
L                Lagu             ᛚ
M                Mon              ᛗ
N                Naed             ᚾ
O                Os               ᚩ
P                Peord            ᛈ
Q                Cweorth          ᛢ
R                Rada             ᚱ
S                Sygil            ᛋ
T                Ti               ᛏ
U                Ur               ᚢ
V                Feh              ᚠ
W                Wyn              ᚹ
X                Icls             ᛉ
Y                Yr               ᚣ
Z                Sygil            ᛋ
Th               Thorn            ᚦ
Sh               N/A
Ch               N/A
NG               Ing              ᛝ

PHASES

Phase 1 - basic command line converter

  Logic should be simple since FUTHORC's 30 characters can be easily translated to the 26 English letters complication should simple
  Only pain in the ass would be TH, NG
  Wait no, C is a whore
  Figured out C, but there is no z or v, use unused vowel symbols for phase 1
  V ->  ᛟ
  Z ->  ᚫ

  Main -

    reference HASH{
      latin glyph: futhorc glyph unicode
    }

    for input text
      if char is a space
        append to output
        
      else if two letter sounds
        pop both letter offs
        reference both to has
        append to output
        
      else
        reference hash
        append to output

      output output text

Phase 2 - file converter - I made this without updating updating read me

    everything stored in text_files, with in and output files

Phase 3 - Add GUI

  thought this was later, starting to draw things

Phase 4 - Add intermeddary to make output phonetic 

  using library called eng-to-ipa. Returns CMU Pronuncations

Phase 5 - Webapp this shit

Phase 6 - Create method to add more writting systems.
