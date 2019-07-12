"""likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
"""
from typing import List

result_map = {
    0: "no one likes this",
    1: "{x[1]} likes this",
    2: "{x[1]} and {x[2]} like this",
    3: "{x[1]}, {x[2]} and {x[3]} like this"
}
result_default = "{x[1]}, {x[2]} and {x[0]} others like this"

def likes(names: List[str]) -> str:
    res_str = result_map.get(len(names), result_default)
    names.insert(0,len(names) - 2)    
    return res_str.format(x=names)
