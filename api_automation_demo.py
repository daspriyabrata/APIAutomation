import requests
import json
import unittest
import HtmlTestRunner
import os
import csv
from ddt import ddt, data, unpack
from csv_reader import get_csv_data
from api_call_manager import API_Call_Manager
csv_path = os.getcwd()+'/story_id.csv'

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
        field_1 = _response_body['by']
        field_2 = _response_body['descendants']
        field_3 = _response_body['id']
        field_4 =  _response_body['kids']
        field_5 = _response_body['score']
        field_6 = _response_body['time']
        field_7 = _response_body['title']
        field_8 = _response_body['type']
        field_9 = _response_body['url']
        if field_1 and field_2 and field_3 and field_4 and field_5 and field_6 and field_6 and field_7 and field_8 and field_9 :
            print(_response_body, _response_status, _response_time)
            assert 1==1
        else:
            raise Exception('Fields Not Present!!!')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.getcwd()))
