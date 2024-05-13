import Hello as hi
import WebDriver as wd

hi.hello()
answer = input()
if (answer == 'Да' or answer == 'да' or answer == 'yes' or answer == 'Yes'):
    print('Держи!')
    wd.randomwiki()
else:
    print('Ну и иди нахуй')
