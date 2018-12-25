from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
import sys


def main_module():
    fname = input('Enter the file\'s name which is to be formatted :')

    try:
        rf = open(fname, 'r')
    except IOError:
        print(f"Couldn't read file {fname}")
        sys.exit()

    with rf:
        code = rf.read()

    L = input('\nPress\n->1 to insert line Numbers\n->Any other key for not : ')
    if L == '1':
        var = True
    else:
        var = False

    style_list= ['autumn', 'borland', 'bw', 'colorful', 'default', 'emacs',
                'fruity', 'manni', 'monokai', 'murphy', 'native', 'pastie',
                 'rrt', 'tango', 'trac', 'vim' ,'friendly', 'perldoc']

    check= True

    while check:
        # styl = input('\nSpecify style from this list:{}:\n'.format(style_list))
        styl = input(f"\nSpecify a style from this list :\n{style_list}\n")

        if styl in style_list:
            lexer = get_lexer_by_name("python", stripall=True)
            formatter = HtmlFormatter(linenos = var, cssclass = 'source', style=styl)
            formatter.noclasses = True
            with open('demo/result.html', "w") as f:
                result = highlight(code, lexer, formatter, f)
            check=False
            print('\nFormatted File is generated as- result.html')
        else:
            print('Please select style from the list only')


def main():
    main_module()
