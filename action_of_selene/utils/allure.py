import os

import allure
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USER_NAME')
ACCESSKEY = os.getenv('ACCESS_KEY')


def attach_bstack_video(session_id):

    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(USERNAME, ACCESSKEY),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
