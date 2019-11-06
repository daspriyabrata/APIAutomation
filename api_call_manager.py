import requests
import csv
import os


class API_Call_Manager:

    @staticmethod
    def top_stories_api(_host):
        try:
            _response = requests.get(_host+ "topstories.json?print=pretty")
        except requests.ConnectTimeout:
            raise Exception('Connection TimedOut!!!')
        except requests.ConnectionError:
            raise Exception('Connection Error Occured!!!!')
        except requests.ReadTimeout:
            raise Exception('Read Timeout')
        _response_json = _response.json()
        _top_ten_stories = []
        for i in range(12):
            # print(_response_json[i])
            _top_ten_stories.append(str(_response_json[i]))

        variable_file = open(str(os.getcwd()) + '/story_id.csv', "wt")
        writer = csv.writer(variable_file)
        writer.writerow(_top_ten_stories)
        return _response

    @staticmethod
    def story_wise_details(_host, _story_id):
        try:
            _response = requests.get(_host+"item/"+_story_id+".json?print=pretty")
        except requests.ConnectTimeout:
            raise Exception('Connection TimedOut!!!')
        except requests.ConnectionError:
            raise Exception('Connection Error Occured!!!!')
        except requests.ReadTimeout:
            raise Exception('Read Timeout')
        return _response