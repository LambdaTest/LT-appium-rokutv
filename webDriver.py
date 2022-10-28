import requests
import json
from time import sleep
import copy
from typing import Any, Dict, List, Union

_W3C_CAPABILITY_NAMES = frozenset([
    'acceptInsecureCerts',
    'browserName',
    'browserVersion',
    'pageLoadStrategy',
    'platformName',
    'proxy',
    'setWindowRect',
    'strictFileInteractability',
    'timeouts',
    'unhandledPromptBehavior',
    'webSocketUrl'
])

_OSS_W3C_CONVERSION = {
    'acceptSslCerts': 'acceptInsecureCerts',
    'version': 'browserVersion',
    'platform': 'platformName'
}

_EXTENSION_CAPABILITY = ':'

class WebDriver:
    # hub url to be used for test execution
    hub_url: str

    def __init__(self, hub_url: str, caps):

        # set hub url
        print(hub_url)
        self._set_hub_url(hub_url)

        # convert capabilities to w3c format
        w3c_caps = self._make_w3c_caps(caps)
        required_caps = {"capabilities": w3c_caps, "desiredCapabilities": caps}

        request_url = self._build_request_url('')
        response = self._post(request_url, required_caps)
        print(response)
        print(response.content)
        res = json.loads(response.text)
        self._session_id = res['sessionId']
    
    def _make_w3c_caps(self, caps: Dict) -> Dict[str, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        appium_prefix = 'appium:'

        caps = copy.deepcopy(caps)
        profile = caps.get('firefox_profile')
        always_match = {}
        if caps.get('proxy') and caps['proxy'].get('proxyType'):
            caps['proxy']['proxyType'] = caps['proxy']['proxyType'].lower()
        for k, v in caps.items():
            if v and k in _OSS_W3C_CONVERSION:
                always_match[_OSS_W3C_CONVERSION[k]] = v.lower() if k == 'platform' else v
            if k in _W3C_CAPABILITY_NAMES or _EXTENSION_CAPABILITY in k:
                always_match[k] = v
            else:
                if not k.startswith(appium_prefix):
                    always_match[appium_prefix + k] = v
        if profile:
            moz_opts = always_match.get('moz:firefoxOptions', {})
            # If it's already present, assume the caller did that intentionally.
            if 'profile' not in moz_opts:
                # Don't mutate the original capabilities.
                new_opts = copy.deepcopy(moz_opts)
                new_opts['profile'] = profile
                always_match['moz:firefoxOptions'] = new_opts
        return {'alwaysMatch': always_match, 'firstMatch': [{}]}

    def _set_hub_url(self, hub_url: str):
        self.hub_url = hub_url

    def _send_launch_channel(self, channel_code: str):
        data = {'channelId' : channel_code}
        request_url = self._build_request_url(f"/{self._session_id}/launch")
        return self._post(request_url, data)
    
    def _send_sequence(self, sequence):
        data = {'button_sequence' : sequence}
        request_url = self._build_request_url(f"/{self._session_id}/press")
        return self._post(request_url, data)

    def _get_ui_element(self, data: object):
        request_url = self._build_request_url(f"/{self._session_id}/element")
        return self._post(request_url, data)

    def _send_keypress(self, key_press: str):
        data = {'button' : key_press}
        request_url = self._build_request_url(f"/{self._session_id}/press")
        return self._post(request_url, data)

    def _build_request_url(self, endpoint: str):
        return self.hub_url + endpoint

    def quiet(self):
        request_url = self._build_request_url(f"/{self._session_id}")
        self._delete(request_url)

    def _post(self, request_url: str, data: object):
        return requests.post(url = request_url, data = json.dumps(data))

    def _get(self, request_url: str):
        return requests.get(request_url)
    
    def _delete(self, request_url: str):
        return requests.delete(request_url)


        #functionaliy
    def launch_the_channel(self, channel_code):
        launch_response = self._send_launch_channel(channel_code)
        if launch_response.status_code != 200:
            raise Exception("Wrong launch response code")

    def verify_is_screen_loaded(self, data: object, invoke_error = True, retries = 10):
        while retries > 0:
            ui_layout_response = self._get_ui_element(data)
            if ui_layout_response.status_code != 200:
                retries -= 1
                sleep(1)
            else:
                return True
        if invoke_error == True:
            raise Exception("Can't find element")
        else:       
            return False

    def press_btn(self, key_press: str):
        sleep(2)
        key_press_response = self._send_keypress(key_press)
        if key_press_response.status_code != 200:
            raise Exception("Wrong keypress response code")

    def send_word(self, word: str):
        sleep(2)
        for c in word:
            key_press_response = self._send_keypress(f"LIT_{c}")
            if key_press_response.status_code != 200:
                raise Exception("Wrong keypress response code")

    def send_button_sequence(self, sequence):
        key_press_response = self._send_sequence(sequence)
        if key_press_response.status_code != 200:
            raise Exception("Wrong keypress response code")

    def apps(self):
        request_url = self._build_request_url(f"/{self._session_id}/apps")
        print(request_url)
        response =  self._get(request_url)
        print(response.content)