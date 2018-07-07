#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller.core import RemovalService

from unittest import mock, TestCase


class RemovalServiceTestCase(TestCase):

    @mock.patch('controller.core.os.path')
    @mock.patch('controller.core.os')
    def test_rm(self, mock_os, mock_path):
        # Instantiate our service
        reference = RemovalService()

        # Set up the mock
        mock_path.isfile.return_value = False

        reference.rm('any path')

        # Test that the remove call was NOT called
        self.assertFalse(mock_os.remove.called,
                         msg='Failed to not remove the file if not present')

        # Make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm('any path')

        # Test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('any path')
