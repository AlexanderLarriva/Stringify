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
        result += f'{replacer * (spaces_count-1)}}}'
        return result
    else:
        raise ValueError(f'Unsupported value type: {type(value)}')
    

data = { "hello": "world", "is": True, "nested": { "count": 5 } }
   
# print(stringify(data, replacer=' ', spaces_count=1))

print(stringify(data, 'Z', 2))