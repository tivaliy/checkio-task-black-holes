from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
# from checkio.referees import cover_codes
# from checkio.referees import checkers

from tests import TESTS


cover = """def cover(f, data):
    return f(list(tuple(d) for d in data))"""


def checker(right_answer, user_answer):
    # if not user_answer:
    #     return False, "Your answer is empty"
    if not isinstance(user_answer, (list, tuple)) or \
             any(not isinstance(line, (list, tuple)) for line in user_answer):
        return False, "It's not lists"
    if any(not isinstance(x, (float, int)) for line in user_answer for x in line):
        return False, "It's not numbers"
    precision = 0.01
    return all(abs(right_coord - user_coord) <= precision
             for right_line, user_line in zip(right_answer, user_answer)
               for right_coord, user_coord in zip(right_line, user_line)), None

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
    checker=checker).on_ready)

# api.add_listener(
#     ON_CONNECT,
#     CheckiOReferee(
#         tests=TESTS,
#         cover_code={
#             'python-27': cover,
#             'python-3': cover
#         },
#     ).on_ready)
