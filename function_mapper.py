#uses generator functions to call multiple functions multiple times
SUCCESS = 1
WARNING = 0
ERROR = -1
INFO = 2

def function1():
    for x in range(10):
        if x % 2 == 0:
            yield ('message', SUCCESS)
        else:
            yield ('error message', ERROR)

def function2():
    for x in range(10):
        if x % 2 == 0:
            yield ('warning', WARNING)
        else:
            yield ('info', INFO)


mapping= {
    'function1' : function1,
    'function2' : function2
}

for mod,func in mapping.items():
    print('Calling {} '.format(mod))
    print(func)
    for status, message in func():
        if status == SUCCESS:
            print(message, 'green')
        elif status == WARNING:
            print(message, 'yellow')
        elif status == ERROR:
            print(message, 'red')
        elif status == INFO:
            print(message)