import json
import os
import unittest

import HtmlTestRunner
from ddt import ddt, data, unpack

from api_call_manager import API_Call_Manager
from csv_reader import get_csv_data

csv_path = os.getcwd() + '/story_id.csv'


@ddt
class HackerNewsAPIAutomation(unittest.TestCase):

    def setUp(self):
        self._host_name = "https://hacker-news.firebaseio.com/v0/"

    def test_1_top_stories(self):
        _response = API_Call_Manager.top_stories_api(self._host_name)
        if _response.status_code == 200 and _response.json():
            assert 1 == 1
            print(_response.json(), _response.elapsed.total_seconds())
        else:
            print(_response.json(), _response.status_code)
            assert 1 == 2

    @data(*get_csv_data(csv_path))
    @unpack
    def test_2_story_wise_data(self, story_id):
        _response = API_Call_Manager.story_wise_details(self._host_name, story_id)
        _response_body = _response.json()
        _response_status = _response.status_code
        _response_time = _response.elapsed.total_seconds()

        with open('sampleresponse.json', 'rt') as f:
            sj = json.load(f)
            keys = list(sj.keys())
        for key in keys:
            if key in list(_response_body.keys()):
                pass
            else:
                raise Exception(key + " key is not present.")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.getcwd()))
