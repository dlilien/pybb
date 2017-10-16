#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 dlilien <dlilien@berens>
#
# Distributed under terms of the MIT license.

"""
This is a little library. It has some functions we may want to import.
"""


def list_to_strs(input_list):
    """Try to convert every item in a list like object to a string"""
    return [str(val) for val in input_list]


def fancy_print(input_dict):
    """Print a nice version of a dictionary"""
    for name, value in input_dict.items():
        print('Name:', name)
        print('Value:', value)


def main():
    """Normally we just would have no main for our libraries, but this shows an exception and escape character"""
    raise Exception('This shouldn\'t be executed, it is only for importing functions!')


if __name__ == '__main__':
    main()
