"""
MIT License

Copyright (c) 2022 『 𝑺𝜞𝜩𝜩𝜨𝜦𝜯𝜢 𝜝𝜢𝜜𝑺𝜤 』 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import regex


def regex_searcher(regex_string, string):
    try:
        search = regex.search(regex_string, string, timeout=6)
    except (TimeoutError, Exception):
        return False
    return search


def infinite_loop_check(regex_string):
    loop_matches = [
        r"\((.{1,}[\+\*]){1,}\)[\+\*].",
        r"[\(\[].{1,}\{\d(,)?\}[\)\]]\{\d(,)?\}",
        r"\(.{1,}\)\{.{1,}(,)?\}\(.*\)(\+|\* |\{.*\})",
    ]
    for match in loop_matches:
        match_1 = regex.search(match, regex_string)
        if match_1:
            return True
    return False
