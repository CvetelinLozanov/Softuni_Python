def manipulating_string(_type: str, _text: str):
    if _type == 'int':
        return manipulate_int_number(_text)
    elif _type == 'real':
        return manipulate_real_number(_text)
    elif _type == 'string':
        return  manipulate_string(_text)


def manipulate_string(_text):
    return f'${_text}$'


def manipulate_real_number(_text):
    text_to_num = float(_text)
    return f'{text_to_num * 1.5:.2f}'


def manipulate_int_number(_txt: str):
    text_to_integer = int(_txt)
    return text_to_integer * 2


type = input()
text = input()
print(manipulating_string(type, text))