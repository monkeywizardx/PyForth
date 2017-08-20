# forth_words.py
# Stores variables and user defined words for editing purposes.
variables = {
  
}
# The collection of user defined words and bootstrapped words. It's actually executed in the same way as REPL code.
word_dict = {
  'swap': '! swap-top ! swap-bottom @ swap-top @ swap-bottom', # swap. It works without variable definiton because of a quirk of !
  'dup': '! dup-value @ dup-value @ dup-value', # dup works on similar logic to above.
  'negate': '-1 swap *',
  '-': 'negate +',
  '*': '! loop-top ! by-value 0 0 @ loop-top do @ by-value + loop',
}
