#!/usr/bin/python3
def from_json_string(my_str):
    import json

    if my_str is None:
        return None
    else:
        return(json.loads(my_str))
