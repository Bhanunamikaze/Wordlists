filepath = "wordlists/names.txt"
alphachar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open(filepath) as fp:
    lines = fp.read().splitlines()
with open(filepath, "r") as fp:
  for line in lines:
    AlphaName =  ["{}{}".format(i,line) for i in alphachar]
    NameAlpha =  ["{}{}".format(line,i) for i in alphachar]
    print('\n'.join(AlphaName))
    print('\n'.join(NameAlpha))
