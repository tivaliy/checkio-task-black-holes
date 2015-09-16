from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS


cover = """def cover(f, data):
    return f(list(tuple(d) for d in data))"""
# cover = """def cover(func, data):
#     cdata = list(tuple(d) for d in data)
#     res = func(cdata)
#     if not isinstance(res, list):
#         raise TypeError("Must be a list.")
#     return res, str(res)
# """


def checker(data, user_data):
    # user_result, str_result = user_data
    for t in user_data:
        if not isinstance(t, tuple):
            return False, (False, "You should return a list of tuples.")
    return True, (True, "Great")


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
        checker=checker,
    ).on_ready)