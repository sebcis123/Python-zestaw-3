class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # wywołaj oryginalną funkcję i pobierz wynik
        result = self.func(*args, **kwargs)
        # jeśli wynik jest napisem to zamień na wielkie litery
        if isinstance(result, str):
            return result.upper()
        return result

@UppercaseDecorator
def say_hello():
    return "hello, world!"

print(say_hello())
