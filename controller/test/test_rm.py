#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller.core import rm

from unittest import mock, TestCase


class RmTestCase(TestCase):

    @mock.patch('controller.core.os.path')
    @mock.patch('controller.core.os')
    def test_rm(self, mock_os, mock_path):

        # Set up the mock
        mock_path.isfile.return_value = False

        rm('any path')

        # Test that the remove call was NOT called
        self.assertFalse(mock_os.remove.called,
                         msg='Failed to not remove the file if not present')

        # Make the file 'exist'
        mock_path.isfile.return_value = True

        rm('any path')

        # Test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('any path')
