#### Exercise for *args ####
def print_args(*args):
    i = 1
    for arg in args:
        print(f'the {i}th arg is {arg}')
        i+=1

#### Exercise for **kwargs ####
def print_kwargs(**kwargs):
    for key, value in kwargs.items():    # kwargs.items() return: dict_items([(key, value), ..., (key, value)])
        print(f'{key}: {value}')
        
        
if __name__ == '__main__':
    args = ['Donghui', 'Li', 'Yifan', 'Wang']
    print_args(*args)
    kwargs = {
        'First Name': 'Donghui',
        'Last Name': 'Li',
        'Email': 'lidh96@gmail.com'
    }
    print_kwargs(**kwargs)