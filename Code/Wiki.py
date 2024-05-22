import WebDriver as wd


print('Hi, do you want to get random article from wiki?')

yes = ['Да', 'да', 'YES', 'yes', 'Yes', 'ДА']

if (input() in yes):
    print('Catch it!')
    wd.randomwiki()
else:
    print('Good bye!')
