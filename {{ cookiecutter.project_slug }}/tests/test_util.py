# -*- coding: utf-8 -*-
# vim: set ft=python ts=4 sw=4 expandtab:

from sample.util import upper_case


class TestUtil:
    def test_upper_case(self):
        assert upper_case(None) is None
        assert upper_case("") == ""
        assert upper_case("a") == "A"
        assert upper_case("Hello") == "HELLO"
