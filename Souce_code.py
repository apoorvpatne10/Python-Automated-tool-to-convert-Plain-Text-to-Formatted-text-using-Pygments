from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

file_name=input('Enter the File name:')

with open(file_name, "r") as rf:
    code = rf.read()

f = open('Buffer_file.html', "w")
L =(input('\nPress\n1 to insert line Numbers\nAny other key for not:'))
if L=='1':
    var=True
else:
    var=False
styl_list= ['autumn',
             'borland',
             'bw',
             'colorful',
             'default',
             'emacs',
             'friendly',
             'fruity',
             'manni',
             'monokai',
             'murphy',
             'native',
             'pastie',
             'perldoc',
             'rrt',
             'tango',
             'trac',
             'vim']
check= True
while check:
    STYL=input('\nSpecify style from this list:{}:\n'.format(styl_list))
    if STYL in styl_list:
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter(linenos=var,
                                  cssclass='source',
                                  style=STYL)
        formatter.noclasses = True
        result = highlight(code, lexer, formatter, f)
        check=False
        print('\nSuccess!...Your Formatted File is generated as- Buffer_file.html')
    else:
        print('Please select style from list only')
f.close()


