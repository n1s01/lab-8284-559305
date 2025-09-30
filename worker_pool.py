#!/usr/bin/env python3

"""Simple worker pool for parallel task execution.

Provides a thin wrapper around ``concurrent.futures.ThreadPoolExecutor``
allowing submission of callables and collection of results.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterable, List, Any

def run_tasks(tasks: Iterable[Callable[[], Any]], max_workers: int = 4) -> List[Any]:
    """Execute *tasks* in parallel using a thread pool.

    Args:
        tasks: An iterable of callables with no arguments.
        max_workers: Maximum number of worker threads.

    Returns:
        List of results in the order tasks were completed.
    """
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_task = {executor.submit(task): task for task in tasks}
        for future in as_completed(future_to_task):
            results.append(future.result())
    return results

def map_tasks(func: Callable[[Any], Any], iterable: Iterable[Any], max_workers: int = 4) -> List[Any]:
    """Apply *func* to each item in *iterable* in parallel.

    Returns a list of results preserving the order of the input iterable.
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(func, iterable))