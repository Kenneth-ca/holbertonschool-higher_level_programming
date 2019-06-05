#!/usr/bin/python3
def to_json_string(my_obj):
    import json

    if my_obj is None:
        return None
    else:
        return(json.dumps(my_obj))
