def stringify(value, replacer=' ', spaces_count=1):
    if isinstance(value, str):
        return value
    elif isinstance(value, bool):
        return str(value)
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, dict):
        indent = replacer * spaces_count
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}{k}: {stringify(v, replacer, spaces_count+1)}\n'
# result += f'{indent}{k}: {replacer}{stringify(v, replacer, spaces_count+2)}\n'
        result += f'{replacer * (spaces_count-1)}}}'
        return result
    else:
        raise ValueError(f'Unsupported value type: {type(value)}')
 

data = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}

# data = { "hello": "world", "is": True, "nested": { "count": 5 } }
# data = True   

# print(stringify(data, replacer=' ', spaces_count=1))

print(stringify(data, '|-', 2))
