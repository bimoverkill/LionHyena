from sys import stderr

from ..config import CONFIG


def debug(strings: str, is_verbose=False, **kwargs):
    if CONFIG.DEBUG:
        if CONFIG.VERBOSE:
            print(strings, file=stderr, flush=True)
        else:
            if not is_verbose:
                print(strings, file=stderr, flush=True)

        stderr.flush()

