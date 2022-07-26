
language = 'Python'

if language == 'Python':
    print('language is Python')
elif language == 'Java':
    print('language is Java')
else:
    print('No Match')

user ='Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
a =[1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print(a is b)
