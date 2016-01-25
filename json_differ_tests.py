#!/usr/bin/python

import unittest
import jsondiffer
import json

class MyTest(unittest.TestCase):

    def setUp(self):
        self.differ = jsondiffer.MyDiffer()

    def test_simple_diff(self):
        first={"foo":{"bar":"baz","biz":"foo"},
               "fiz":{"foo":"baz"},
               "bar":"baz",
               "baz":["foo","bar"]
               }
        second={"foo":{"bar":"baz1","biz":"foo"},
                "fiz":{"foo":"baz"},
                "bar":"baz",
                "baz":["foo1"]
                }
        diffed_json = self.differ.diff(first, second)
        self.assertEqual(repr(diffed_json), "{'foo': {'bar': 'baz1'}, 'baz': ['foo1']}")

    def test_nested_diff(self):
        first={"foo":{"bar":"baz","biz":"foo"},
               "fiz":{"foo":"baz", "faa":{"fii":"fom"}},
               "bar":"baz",
               "baz":["foo","bar"]
               }                    
                                                            # SHOULD REMAIN
        second={"foo":{"bar":"baz1","biz":"foo"},           #'foo': {'bar': 'baz1'}
                "fiz":{"foo":"baz", "faa":{"fii":"fam"}},   #{'fiz': {'faa': {'fii': 'fam'}}
                "bar":"baz",
                "baz":["foo1"]                              #'baz': ['foo1']}"
                }
                                                            # FINAL
                                                            #"{'fiz': {'faa': {'fii': 'fam'}, 'foo': 'baz'}, 'foo': {'biz': 'foo', 'bar': 'baz1'}, 'baz': ['foo1']}"
        diffed_json = self.differ.diff(first, second)
        self.assertEqual(repr(diffed_json), "{'fiz': {'faa': {'fii': 'fam'}}, 'foo': {'bar': 'baz1'}, 'baz': ['foo1']}")

    def test_large_file(self):
        first = json.load(open("sample.json"))
        second = json.load(open("sample2.json"))
        diffed_json = self.differ.diff(first, second)
        self.assertEqual(repr(diffed_json), "{u'email': u'smithmorrison@eternis.com', u'tags': [u'commodo', u'tempor', u'amet', u'sint', u'pariatur', u'consequat', u'mollit']}")

    def test_none_values(self):
        first={"foo":None,
               "fiz":{"foo":"baz", "faa":{"fii":"fom"}},
               "bar":"baz",
               "baz":["foo","bar"]
               }                    
                                                            # SHOULD REMAIN
        second={"foo":{"bar":"baz1","biz":"foo"},           #'foo': {'bar': 'baz1', 'biz':'foo'}
               "fiz":{"foo":"baz", "faa":{"fii":"fom"}},
                "bar":None,                                 #'bar':None
                "baz":[None]                                #'baz': [None]}"
                }
                                                            # FINAL
                                                            #"{'foo': {'bar': 'baz1', 'biz':'foo'}, 'bar':'baz', 'baz': [None]}"
        diffed_json = self.differ.diff(first, second)
        self.assertEqual(repr(diffed_json), "{'bar': None, 'foo': {'biz': 'foo', 'bar': 'baz1'}, 'baz': [None]}")


if __name__ == '__main__':
    unittest.main()