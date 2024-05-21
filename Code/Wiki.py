import Hello as hi
import WebDriver as wd

hi.hello()
yes = ['Да', 'да', 'YES', 'yes', 'Yes', 'ДА']
if ('да' in yes):
    print('Catch it!')
    wd.randomwiki()
else:
    print('Good bye!')
