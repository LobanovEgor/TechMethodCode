import Hello as hi
import WebDriver as wd

hi.hello()
answer = input()
yes = ['Да', 'да', 'YES', 'yes', 'Yes', 'ДА']
if (answer in yes):
    print('Держи!')
    wd.randomwiki()
else:
    print('Тогда до новых встреч!')
