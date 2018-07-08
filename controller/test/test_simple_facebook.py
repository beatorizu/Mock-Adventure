#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller import simple_facebook

from unittest import mock, TestCase


class SimpleFacebookTestCase(TestCase):

    @mock.patch.object(simple_facebook.facebook.GraphAPI, 'put_object')
    def test_post_message(self, mock_put_object):
        sf = simple_facebook.SimpleFacebook('fake oauth token')
        sf.post_message('Konnichiwa, Sekai!')

        # Verify
        mock_put_object.assert_called_with('me', 'feed',
                                           message='Konnichiwa, Sekai!')
