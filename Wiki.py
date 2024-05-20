import Hello as hi
import WebDriver as wd

hi.hello()
yes = ['Да', 'да', 'YES', 'yes', 'Yes', 'ДА']
if (input() in yes):
    print('Держи!')
    wd.randomwiki()
else:
    print('Тогда до новых встреч!')
