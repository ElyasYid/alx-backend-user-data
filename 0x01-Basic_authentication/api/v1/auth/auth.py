#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        lenp = len(path)
        if lenp == 0:
            return True

        slpa = True if path[lenp - 1] == '/' else False

        tmpa = path
        if not slpa:
            tmpa += '/'

        for xcl in excluded_paths:
            lenx = len(xcl)
            if lenx == 0:
                continue

            if xcl[lenx - 1] != '*':
                if tmpa == xcl:
                    return False
            else:
                if xcl[:-1] == path[:lenx - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
