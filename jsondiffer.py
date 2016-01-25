#!/usr/bin/python

class MyDiffer(object):
    
    def __ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self.__ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self.__ordered(x) for x in obj)
        else:
            return obj

    def __compare(self, first, second):
        if type(first) != type(second):
            return False
        else:
            return repr(self.__ordered(first)) == repr(self.__ordered(second))

    def __diff_dict(self, first, second):
        result = {}
        if isinstance(first, dict):
            for key in first:
                value_in_first = first[key]
                value_in_second = second[key]
                subresult = self.__diff_dict(value_in_first, value_in_second)
                if subresult is None or len(subresult) > 0:
                    result[key] = subresult
        else:
            if not self.__compare(first, second):
                return second
        return result

    def diff(self, first, second):
        result = self.__diff_dict(first, second)
        return result

