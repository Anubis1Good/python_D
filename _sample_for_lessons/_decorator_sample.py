def my_decorator(fridge: list):
    def outer(func):
        def wrapper(thing):
            print('Открыть холодильник')
            if fridge:
                old_thing = fridge.pop()
                print(f'Вытащить {old_thing}')
            func(thing)
            fridge.append(thing)
            print('Закрыть холодильник')
        return wrapper
    return outer

stinol_sts_200 = []

@my_decorator(stinol_sts_200)
def insert_some(what):
    print(f'Положить {what}')


insert_some('слона')
insert_some('жирафа')



