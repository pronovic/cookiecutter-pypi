# vim: set ft=python ts=4 sw=4 expandtab:

"""
Utility functionality.
"""


def upper_case(value: str | None) -> str | None:
    if value is not None:
        return value.upper()
    return None
