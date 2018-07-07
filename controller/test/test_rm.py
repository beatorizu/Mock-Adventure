#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller.core import rm

from unittest import mock, TestCase


class RmTestCase(TestCase):

    @mock.patch('controller.core.os')
    def test_rm(self, mock_os):
        rm('any path')
        # Test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('any path')
