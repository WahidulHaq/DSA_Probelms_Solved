
import re
text =  'Welc&&&@@ome to Inter$$$$view 123'
 
# # output
# # emocleW ot weivretnI 321

words  = re.sub(r'[^a-zA-Z0-9 ]','',text)
words = words.split()
final= []
for word in words:
    reverse = ''
    for char in word:
        reverse = char + reverse
    final.append(reverse)
print(final)

char = ' '.join(final)
print(char)



