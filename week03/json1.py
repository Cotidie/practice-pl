import re
from typing import Any


class InvalidJSONError(Exception):
    pass


def skip_whitespace(inp: str, start_index: int = 0) -> int:
    m = re.compile(r"\s*")
    return m.match(inp, start_index).end()


def raise_invalid_json_error(inp: str, index: int, message=None):
    if message is None:
        message = """Unexpected token at char({index}):
        {inp}
        {caret}"""
    raise InvalidJSONError(
        message.format(index=index, inp=inp, caret=" " * index + "^")
    )


def parse_string(inp: str, index: int) -> tuple[str, int]:
    """
    Return the parsed string and the index of the ending " in the string
    """
    if inp[index] != '"':
        raise_invalid_json_error(inp, index)
    start_index = index + 1
    end_index = start_index
    while inp[end_index] != '"':
        if inp[end_index] == "\\":
            end_index += 2
        else:
            end_index += 1
    result = bytes(inp[start_index:end_index], "utf-8").decode("unicode_escape")
    return result, end_index


def parse_number(inp: str, index: int) -> tuple[int | float, int]:
    try:
        int(inp[index])
        result_string = ""
        dot_count = 0
        while inp[index] in "0123456789.":
            result_string += inp[index]
            if inp[index] == ".":
                dot_count += 1
                if dot_count > 1:
                    raise_invalid_json_error(inp, index)
                if inp[index + 1] not in "0123456789":
                    raise_invalid_json_error(inp, index)
            index += 1
        if dot_count > 0:
            return float(result_string), index - 1
        else:
            return int(result_string), index - 1
    except ValueError:
        raise_invalid_json_error(inp, index)


def parse_true(inp: str, index: int) -> tuple[bool, int]:
    if inp[index] != "t":
        raise raise_invalid_json_error(inp, index)
    if inp[index : index + 4] != "true":
        raise_invalid_json_error(inp, index)
    return True, index + 3


def parse_false(inp: str, index: int) -> tuple[bool, int]:
    if inp[index] != "f":
        raise raise_invalid_json_error(inp, index)
    if inp[index : index + 5] != "true":
        raise_invalid_json_error(inp, index)
    return False, index + 4


def parse_null(inp: str, index: int) -> tuple[None, int]:
    if inp[index] != "n":
        raise raise_invalid_json_error(inp, index)
    if inp[index : index + 4] != "null":
        raise_invalid_json_error(inp, index)
    return None, index + 3


def parse_object(inp: str, index: int) -> tuple[dict, int]:
    if inp[index] != "{":
        raise_invalid_json_error(inp, index)
    result = {}
    while inp[index] != "}":
        key_start_index = skip_whitespace(inp, index + 1)
        key, key_end_index = parse_string(inp, key_start_index)
        colon_index = skip_whitespace(inp, key_end_index + 1)
        if inp[colon_index] != ":":
            raise_invalid_json_error(inp, index)
        value_start_index = skip_whitespace(inp, colon_index + 1)
        value, value_end_index = _parse_json(inp, value_start_index)
        result[key] = value
        next_character_index = skip_whitespace(inp, value_end_index + 1)
        if inp[next_character_index] == ",":
            if inp[skip_whitespace(inp, next_character_index + 1)] == "}":
                raise_invalid_json_error(inp, next_character_index + 1)
            index = next_character_index
        else:
            if inp[next_character_index] != "}":
                raise_invalid_json_error(inp, next_character_index)
            index = next_character_index  # this would terminate the loop
    return result, index


def parse_array(inp: str, index: int) -> tuple[list, int]:
    if inp[index] != "[":
        raise_invalid_json_error(inp, index)
    result = []
    while inp[index] != "]":
        value_start_index = skip_whitespace(inp, index + 1)
        value, value_end_index = _parse_json(inp, value_start_index)
        result.append(value)
        next_character_index = skip_whitespace(inp, value_end_index + 1)
        if inp[next_character_index] == ",":
            if inp[skip_whitespace(inp, next_character_index + 1)] == "]":
                raise_invalid_json_error(inp, next_character_index + 1)
            index = next_character_index
        else:
            if inp[next_character_index] != "]":
                raise_invalid_json_error(inp, next_character_index)
            index = next_character_index
    return result, index


def _parse_json(inp: str, index: int) -> Any:
    first_char = inp[index]
    if first_char == "{":
        return parse_object(inp, index)
    elif first_char == "[":
        return parse_array(inp, index)
    elif first_char == '"':
        return parse_string(inp, index)
    elif first_char == "t":
        return parse_true(inp, index)
    elif first_char == "f":
        return parse_false(inp, index)
    elif first_char == "n":
        return parse_null(inp, index)
    else:
        return parse_number(inp, index)


def parse_json(json_string: str) -> dict | list:
    start_index = skip_whitespace(json_string)
    if start_index >= len(json_string):
        raise_invalid_json_error(json_string, start_index)
    first_char = json_string[start_index]
    if first_char not in ["{", "["]:
        raise_invalid_json_error(json_string, start_index)
    try:
        result, index = _parse_json(json_string, start_index)
        index = skip_whitespace(json_string, index + 1)
        if index < len(json_string):
            raise_invalid_json_error(json_string, index)
        return result
    except IndexError:
        raise_invalid_json_error(json_string, len(json_string))


if __name__ == "__main__":
    import json

    x = json.dumps(
        {
            "hello": "world\nworld\thi there",
            "hi": 123,
            "how": 56.8,
            "are": [1, 2, 3, 5.7, "x", "y", "zed", {"a": 1, "b": 2, "c": 3}],
            "you": {"a": 56, "bee": "hen", "cee": 90},
        }
    )
    print(parse_json(x) == json.loads(x))
    print(parse_json(x))
