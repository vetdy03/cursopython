

class Laptop:
    """clase empleada para saer si tiene hdd o ssd"""
    has_ssd = True

if __name__ == '__main__':
    laptop_sergio = Laptop() ## instanciando
    print(laptop_sergio.has_ssd)
    print(dir(laptop_sergio))
    print(dir(laptop_sergio.__doc__))