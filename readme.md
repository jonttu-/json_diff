# Python JSON differ

## Description
This is an example project to find and print differences in two JSON inputs.

## Requirements
python

## Contents
Included is the actual class that does the diff (jsondiffer.py) as well as a test suite (jsondiffer_tests.py)

## Usage example
<pre><code>
>>> import jsondiffer
>>> differ = jsondiffer.MyDiffer()
>>> result = differ.diff({"foo":{"bar":"baz1","biz":"foo"}}, {"foo":{"bar":"baz","biz":"foo"}})
>>> print result
{'foo': {'bar': 'baz'}}
</pre></code>

## Tests
To execute the included unit tests:

    $ python json_differ_tests.py


