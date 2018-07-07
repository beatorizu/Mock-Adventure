#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller.core import rm

import os.path
import tempfile
import unittest


class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self):
        with open(self.tmpfilepath, 'w') as f:
            f.write('Delete me!')

    def test_rm(self):
        # Remove the file
        rm(self.tmpfilepath)
        # Test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath),
                         msg="Failed to remove the file.")
