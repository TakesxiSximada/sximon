# -*- coding: utf-8 -*-
import os
import re
import json
import time
import random
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    request.redis.set('aaa', str(time.time()))
    name = request.redis.get('aaa')
    return Response('Hello {}!'.format(name))


kageyama_negative_words = [
    'この程度がお判りにならないとは、失礼ですが{name}様はアホでいらっしゃいますか?',
    '失礼ですが{name}様。 ひょっとして{name}様の目は節穴でございますか？',
    '失礼ながら{name}様、やはりしばらくの間、引っ込んでいてくださいますか？',
    '失礼ながら{name}様、このまま逮捕あそばされ、少々反省していただけますか?',
    '{name}様は相変わらずアホでいらっしゃいますね。いい意味で。',
    'それでも{name}様はプロでございますか。ズブの素人よりもレベルが低くていらっしゃいます。',
    '{name}様は冗談をおっしゃっているのでございますか？もし、そうであるならば、『ウ～ケ～る～』でございます。',
    '{name}様。お言葉を返すようで恐縮ですが、{name}様の方こそどこに目ン玉をお付けになってらっしゃるのでございますか？',
    'チャンチャラおかしくって、横っ腹が痛うございます。',
    '失礼ながら{name}様。{name}様はどアホでございますか？',
    '失礼ながら{name}様。{name}様の目はやはり節穴でございましたか。',
    '{name}さまの推理力はやはりずぶの素人以下でございましたか。',
    'そこまでレベルが低いというのであれば私、本気で「ウケる～」でございます。',
    '大変失礼ながら、{name}様の単純さは、まさに幼稚園児レベルかと思われます。',
    'お言葉を返すようで恐縮ですが、{name}様のほうこそ、どこに目ン玉お付けになっていらっしゃるのでございますか？',
    'これだけの情報を得ておきながら、まるで真相に辿り着けないとは、{name}様は、頭がお悪いのではございませんか?',
    'まさに、{name}様のおっしゃったとおりでございます。確かに、{name}様の凡庸な閃きなど、誰かに話すほどのものではございません。聞くだけ時間の無駄でございました',
    'なぜ、{name}様は数多くを経験しながら、一ミリも進歩なさらないのでございますか？ひょっとして、わざとでございますか？',
    '{name}様はわたくしと比べて目だけはよろしいものと思っておりましたが、どうやら見当違いでございました。目の前にあるヒントにまるでお気づきにならないとは……わたくし{name}様には心の底からガッカリでございます',
    '{name}様、いま少しばかり脳みそをご使用になられてはいかがでございますか',
    '失礼ながら、{name}様。この程度の謎で頭を悩ませておいでとは、{name}様は本当に役立たずでございますね',
    '失礼ながら、{name}様は無駄にディナーをお召し上がりになっていらっしゃいます',
    '{name}様。失礼ながら、{name}様は穀潰しの暇人でございますか？',
    ]
get_negative_word = lambda: random.choice(kageyama_negative_words)


def slack_outcomming_talk(request):
    """
    """
    text = request.POST['text'].encode('utf8')
    user_name = request.POST['user_name']

    keywords = [
        '影',
        '山',
        'kageyama',
        'い',
        '?',
        '？',
        ]

    if user_name == 'slackbot' or not any(keyword in text for keyword in keywords):
        return Response()

    fmt = get_negative_word()
    if 'おはよう' in text:
        fmt = 'おはようございます、{}様。'
    elif 'おやすみ' in text:
        fmt = 'おやすみなさいませ、{}様。'
    elif 'ただいま' in text:
        fmt = 'おかえりなさいませ、{}様。'
    elif '帰り' in text:
        fmt = 'お待ちしております、{}様。'
    elif '帰る' in text:
        fmt = 'お待ちしております、{}様。'
    elif 'かえる' in text:
        fmt = 'お待ちしております、{}様。'
    elif 'かえり' in text:
        fmt = 'お待ちしております、{}様。'
    elif 'お願い' in text:
        fmt = '承りました。'
    elif 'おねがい' in text:
        fmt = '承りました。'
    msg = fmt.format(name=user_name)

    return Response(
        body=json.dumps({'text': msg}),
        content_type='application/json',
        )


def slack_outcomming_trigger(request):
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
    text = request.POST['text'].encode('utf8')
    user_name = request.POST['user_name']
    trigger = request.POST.get('trigger_word', '')

    if user_name == 'slackbot':
        return Response()

    target_words = [
        '^\+\+',
        '^\-\-',
        '^\!',
        'kageyama',
        '影',
        '山',
        ]

    for target_word in target_words:
        regx = re.compile('(?P<trigger>{})'.format(target_word))
        matching = regx.search(text)
        if matching:
            trigger = matching.group('trigger')
            break

    if not trigger:
        return Response()

    msg = ''
    print(trigger)
    if trigger == '++':
        regx = re.compile(r'^\+\+(?P<name>\S+)')
        matching = regx.search(text)
        if matching:
            name = matching.group('name')
            count = request.redis.hget(int, name)
            count = int(count) if count else 0
            count += 1
            request.redis.hset(int, name, count)
            msg = '{name}様は通算 {count} になりました。'.format(name=name, count=count)
    elif trigger == '--':
        regx = re.compile(r'^\-\-(?P<name>\S+)')
        matching = regx.search(text)
        if matching:
            name = matching.group('name')
            count = request.redis.hget(int, name)
            count = int(count) if count else 0
            count -= 1
            request.redis.hset(int, name, count)
            fmt = '{name}様は通算 {count} になりました。' + get_negative_word()
            msg = fmt.format(name=name, count=count)
    elif trigger == '!':
        regx_say = re.compile(r'^\!say\s+(?P<command>\S+)\s+(name)')
        matching = regx_say.search(text)
        fmt = get_negative_word()
        msg = fmt.format(name=user_name)

        if matching:
            command = matching.group('command')
            name = matching.group('name')
            if command == 'create':
                if not request.redis.hexists(list, name):
                    request.redis.hset(list, name)
                    msg = '手配致しました。'
                else:
                    fmt = '{name}様は既に登録されています。' + get_negative_word()
                    msg = fmt.format(name=name)
        else:  # ユーザ名
            regx_user_say = re.compile(r'^\!(?P<user_name>\S+)\s*(?P<message>.*)')
            matching = regx_user_say.search(text)
            print('A'*30)
            print(matching.group('message') if matching else 'NO MATCH')
            print('B'*30)
            if matching:
                user_name = matching.group('user_name')
                message = matching.group('message').strip()
                if message:
                    request.redis.sadd(user_name, message)
                    msg = '手配致しました。'
                else:
                    msg = request.redis.srandmember(user_name)
    if not msg:
        return Response()

    return Response(
        body=json.dumps({'text': msg}),
        content_type='application/json',
        )


def get_bluemix_redis_credential(settings):
    clean = lambda s: s.strip('"').strip("'").strip('"')
    function_name = clean(settings['sximon.bluemix.redis.name'])
    service_name = clean(settings['sximon.bluemix.redis.master'])
    db = clean(settings['sximon.bluemix.redis.db'])

    text = os.environ['VCAP_SERVICES']
    data = json.loads(text)
    for redis_settings in data[function_name]:
        if redis_settings.get('name', None) == service_name:
            credentials = redis_settings['credentials']
            url = 'redis://:{secret}@{host}:{port}/{db}'.format(
                secret=credentials['password'],
                host=credentials['host'],
                port=credentials['port'],
                db=db,
                )

            return {
                'redis.url': url,
                'redis.max_connections': None,
                }


def main(global_config, **local_config):
    """This function returns a Pyramid application.
    """
    settings = dict(global_config)
    settings.update(local_config)

    settings.update(get_bluemix_redis_credential(settings))  # update settings for pyramid_redis

    config = Configurator(settings=settings)
    for plugin in settings.get('plugins', '').split():
        config.include(plugin)

    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    config.add_route('slack.outcomming.talk', '/slack/outcomming/talk')
    config.add_view(slack_outcomming_talk, route_name='slack.outcomming.talk')

    config.add_route('slack.outcomming.trigger', '/slack/outcomming/trigger')
    config.add_view(slack_outcomming_trigger, route_name='slack.outcomming.trigger')

    config.include('pyramid_redis')

    config.scan()
    return config.make_wsgi_app()

if __name__ == '__main__':
    PORT = int(os.getenv('VCAP_APP_PORT', 8000))
    app = main()
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()
