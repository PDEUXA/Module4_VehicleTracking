"""
Module for testing flask api with unittest
"""
import json
import unittest
import urllib
from urllib import request


class TestGet(unittest.TestCase):
    data = {'list_frame_contour': 'data/bounding_box.json', "frame_path": 'data/image/'}

    def test_json_output(self):
        """
        test types of output request
        test values and length of output request
        :return:
        """
        url_values = urllib.parse.urlencode(self.data)
        url = "http://0.0.0.0:5000/Track/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')

        result = request.urlopen(full_url).read()
        output = json.loads(result.decode("utf8"))

        self.assertEqual(type(output), dict)
        for k in output.keys():
            self.assertEqual(type(output[k]), list)
            for item in output[k]:
                self.assertEqual(type(item), int)

        self.assertEqual(output["frame 11"], [0])
        self.assertEqual(output["frame 18"], [0, 1])
        self.assertEqual(output["frame 518"], [62])

        self.assertNotIn("frame 519", output.keys())
        self.assertEqual(len(output), 519)

    def test_json_output_with_dict_input(self):
        """
        test types of output request
        test values and length of output request
        :return:
        """
        data_file = json.load(open('data/bounding_box.json', 'r'))
        data = {'list_frame_contour': json.dumps(data_file), "frame_path": 'data/image/'}

        url_values = urllib.parse.urlencode(data, quote_via=urllib.parse.quote)
        url = "http://0.0.0.0:5000/Track/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')

        result = request.urlopen(full_url).read()
        output = json.loads(result.decode("utf8"))

        self.assertEqual(type(output), dict)
        for k in output.keys():
            self.assertEqual(type(output[k]), list)
            for item in output[k]:
                self.assertEqual(type(item), int)

        self.assertEqual(output["frame 11"], [0])
        self.assertEqual(output["frame 18"], [0, 1])
        self.assertEqual(output["frame 518"], [62])

        self.assertNotIn("frame 519", output.keys())
        self.assertEqual(len(output), 519)
