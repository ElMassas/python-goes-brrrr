import os
import pstats
import cProfile
import functools
from typing import Any, Callable
from time import perf_counter
from loguru import logger
from io import StringIO


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logger.debug(
            f"Execution of function: {func.__name__} took {run_time:.2f} seconds."
        )
        return value

    return wrapper


def profile(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        profiler = cProfile.Profile()
        value = profiler.runcall(func, *args, **kwargs)

        s = StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
        ps.print_stats()
        logger.debug(f"Profile of function: {func.__name__}\n{s.getvalue()}")

        return value

    return wrapper


def elapsed(start_time):
    return start_time - perf_counter()


# Check if we're in a development environment
is_development = os.getenv("ENV") == "development"


# Define a noop decorator for production
def noop_decorator(func):
    return func


# Choose the appropriate decorator based on the environment
decorator = benchmark if is_development else noop_decorator
