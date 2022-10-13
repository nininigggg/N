import requests
import hamcrest


class TestAPI:
    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        # assert_that

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'