import pytest

from hy.compat import PYODIDE

in_init = "chippy"


def kwtest(*args, **kwargs):
    return kwargs


def function_with_a_dash():
    pass


can_test_async = not PYODIDE
async_test = pytest.mark.skipif(
    not can_test_async, reason="`asyncio.run` not implemented"
)


async_exits = []
class AsyncWithTest:
    def __init__(self, val):
        self.val = val

    async def __aenter__(self):
        return self.val

    async def __aexit__(self, exc_type, exc, traceback):
        async_exits.append(self.val)


async def async_loop(items):
    import asyncio

    for x in items:
        yield x
        await asyncio.sleep(0)
