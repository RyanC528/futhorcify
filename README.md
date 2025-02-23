# FUTHORCify
Basic translator to turn written english to the futhorc script instead of latin due to random interss

Need a project to do some practist after not making as much as I hopped. As such I am structuring this project in a way I can expand based on intrence.
So parts of this project will be listed in phases, probably won't do all parts but I do better with structured 

REFERENCE INFO

GLYPH CHART,

English Sound - Futhorc letter - Futhor Glyph - Unicode
A                Ac               
B                Berc
C                Cen
D                Daeg
E                Eh
F                Feh
G                Geofu
H                Haegil
I                Is
J                Geal
K                Calc
L                Lagu
M                Mon
N                Naed
O                Os
P                Peord
Q                Cweorth
R                Rada
S                Sygil
T                Ti
U                Ur
V                Feh
W                Wyn
X                Icls
Y                Yr
Z                Sygil
Th               Thorn
Sh               Sygil 
Ch               Cen
NG               Ing

PHASES

Phase 1 - basic command line converter

  Logic should be simple since FUTHORC's 30 characters can be easily translated to the 26 English letters complication should simple
  Only pain in the ass would be TH, CH, SH, NG
  Wait no, C is a whore

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

Phase 2 - file converter

Phase 3 - Add GUI

Phase 4 - Add intermeddary to make output phonetic

Phase 5 - Webapp this shit

Phase 6 - Create method to add more writting systems.
