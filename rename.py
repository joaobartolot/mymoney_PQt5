import shutil

print('Witch file do you wanna change:\n')

print('1 ==> Sign in StyleSheet')
print('2 ==> Join StyleSheet\n')

userInput = str(input('>>> '))

if userInput == '1':
    print('\nFor witch type do you wanna change:\n')

    print('1 ==> CSS')
    print('2 ==> QSS\n')

    userInput = str(input('>>> '))

    if userInput == '1':

        shutil.move('signIn-stylesheet.qss', 'signIn-stylesheet.css')

    else:
        
        shutil.move('signIn-stylesheet.css', 'signIn-stylesheet.qss')

elif userInput == '2':
    print('\nFor witch type do you wanna change:\n')

    print('1 ==> CSS')
    print('2 ==> QSS\n')

    userInput = str(input('>>> '))

    if userInput == '1':

        shutil.move('register-stylesheet.qss', 'register-stylesheet.css')

    else:

        shutil.move('register-stylesheet.css', 'register-stylesheet.qss')

elif userInput == '1 and 2':
    print('\nFor witch type do you wanna change:\n')

    print('1 ==> CSS')
    print('2 ==> QSS\n')

    userInput = str(input('>>> '))

    if userInput == '1':

        shutil.move('signIn-stylesheet.qss', 'signIn-stylesheet.css')
        shutil.move('register-stylesheet.qss', 'register-stylesheet.css')

    else:

        shutil.move('signIn-stylesheet.css', 'signIn-stylesheet.qss')
        shutil.move('register-stylesheet.css', 'register-stylesheet.qss')
