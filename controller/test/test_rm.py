#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller.core import RemovalService, UploadService

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


class UploadServiceTestCase(TestCase):

    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # Build our depedencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # Call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete('my uploaded file')

        # Check that it called the rm method of any RemovalService
        mock_rm.assert_called_with('my uploaded file')

        # Check that it called the rm method of __our__ removal_service
        removal_service.rm.assert_called_with('my uploaded file')
