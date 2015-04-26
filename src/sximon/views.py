# -*- coding: utf-8 -*-
from pyramid.view import view_config


@view_config(route_name='slack.outcomming', request_method='POST', renderer='json')
def outcomming(request):
    """
    ```
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
    ```


    commands
    !say delete [NAME]  # 名言削除
    !say list [NAME]  # 名言リスト
    !NAME [TEXT]  # 名言登録
    !birthday DATE [NAME]  # 誕生日登録
    !fortune [NAME]  # 結果表示
    !fortune best  # トップの結果を表示
    !fortune worst  # 末尾の結果を表示
    !count [NAME]  # カウンター計測
    ++NAME  # インクリメント
    --NAME  # デクリメント
    """
    import ipdb; ipdb.set_trace()
    token = request.POST.get('token', '')
    team_id = request.POST.get('team_id', '')
    team_domain = request.POST.get('team_domain', '')
    channel_id = request.POST.get('channel_id', '')
    channel_name = request.POST.get('channel_name', '')
    timestamp = request.POST.get('timestamp', '')
    user_id = request.POST.get('user_id', '')
    user_name = request.POST.get('user_name', '')
    text = request.POST.get('text', '')
    trigger_word = request.POST.get('trigger_word', '')

    text = text.strip()
    words = '!', '++', '--'
    if any(text.startswith(word) for word in words):



    return {'text': 'message text'}
