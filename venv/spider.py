import requests
import json

class GetAnswer:
    def __init__(self):
        self.offset = 0

    def get_answers_by_page(self, questions_id, offset):
        url = 'https://www.zhihu.com/api/v4/questions/' + str(questions_id) + '/answers?limit=20&offset=' + str(offset) + '&include=voteup_count,comment_count,content'
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'HOST': 'www.zhihu.com',
            'Authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'

        }
        r = requests.get(url, verify=False, headers=headers)
        content = r.content.decode('utf-8')
        print(content)
        data = json.loads(content)
        # is_end = data['paging']['is_end']

        self.offset = self.offset + 20

if __name__ == '__main__':
    getanswer = GetAnswer()
    for i in range(3):
        getanswer.get_answers_by_page(340858589, getanswer.offset)
        print(getanswer.offset)
