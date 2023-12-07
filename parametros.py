def exemplo(default=None):
    print(default)

exemplo()
exemplo('str_1')
exemplo(default='a')

def exemplo(default=None, *args, **kwargs):
    print(args)
    print(kwargs)
    print(default)

exemplo()
exemplo(1, 2, 3, a=4, b=5)