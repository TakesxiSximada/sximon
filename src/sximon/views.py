# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.response import Response


@view_config('slack.outcomming', renderer='json')
def outcomming(request):
    """
    token=XXXXXXXXXXXXXXXXXX
    team_id=T0001
    team_domain=example
    channel_id=C2147483705
    channel_name=test
    timestamp=1355517523.000005
    user_id=U2147483697
    user_name=Steve
    text=googlebot: What is the air-speed velocity of an unladen swallow?
    trigger_word=googlebot:
    """
    res = Response(body='test', content_type='application/json')
    return res
