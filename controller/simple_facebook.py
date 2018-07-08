#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook


class SimpleFacebook(object):

    def __init__(self, oauth_token):
        self.graph = facebook.GraphAPI(oauth_token)

    def post_message(self, message):
        """Posts a message to Facebook wall."""
        self.graph.put_object('me', 'feed', message=message)
