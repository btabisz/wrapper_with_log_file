import datetime


def create_wrapper_with_log_file(file_path):
    def create_wrapper(function_to_wrap):
        def wrapper(*args, **kwargs):
            function = function_to_wrap(*args, **kwargs)
            file = open(file_path, 'a')
            file.write('-'*40+"\n")
            file.write("Started at {}\n".format(datetime.datetime.now()))
            file.write('Function name: "{}"\n\n'.format(function_to_wrap.__name__))
            file.write(' '.join("{}".format(x) for x in args))
            file.write('\n')
            file.write(' '.join("{}".format(x, y) for x, y in kwargs))
            file.write('\n')
            file.close()

            return function
        return wrapper
    return create_wrapper


@create_wrapper_with_log_file(r'c:\temp\stock_quantity_wrapper_log.txt')
def change_stock_quantity(product, quantity, employee):
    print('"{}" storage quantity changed to {} - {}'.format(product, quantity, employee))
    return


@create_wrapper_with_log_file(r'c:\temp\change_product_name_wrapper_log.txt')
def change_product_name(old_name, new_name, employee):
    print('Product "{}" changed name to "{}" - {}'.format(old_name, new_name, employee))
    return


print(change_stock_quantity('apple', 50, 'Jan Kowalski'))
print(change_product_name('apple', 'banana', 'Maciej Nowak'))
