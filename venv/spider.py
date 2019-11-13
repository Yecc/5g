import requests
import json
import re

class GetAnswer:
    def __init__(self):
        self.offset = 0
        self.dic = {}

    def get_answers_by_page(self, questions_id, offset):
        url = 'https://www.zhihu.com/api/v4/questions/' + str(questions_id) + '/answers?limit=20&offset=' + str(offset) + '&include=voteup_count,comment_count,content'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'HOST': 'www.zhihu.com',
            'Authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'

        }
        r = requests.get(url, verify=False, headers=headers)
        content = r.content.decode('utf-8')

        data = json.loads(content)
        is_end = data['paging']['is_end']

        for i in data['data']:
            author = i['author']['name']
            # answers = i['content'].replace('<p>', '').replace('</p>', '').replace('<b>', '').replace('</b>', '')
            answers = re.sub('<.*?>','',i['content'])
            self.dic[author] = [answers]


        self.offset = self.offset + 20
        return is_end

    def get_answers(self,questions_id):
        while True:
            is_end = self.get_answers_by_page(questions_id, self.offset)
            if is_end:
                break



if __name__ == '__main__':
    getanswer = GetAnswer()

    getanswer.get_answers(340858589)
    print(getanswer.dic)
