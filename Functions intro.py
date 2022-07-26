
#def hello_func(greeting, name='You'):
#    return 'Hello Function'

# print(hello_func().upper())

 #   return '{}, {}'.format(greeting, name)
#print(hello_func('Hi', name= 'Corey'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses= ['Math', 'Art']
info ={'name': 'John', 'Age': 25}

student_info(*courses,**info)
