from app import app

from lib.summer import Summer


class summary():
    summer = Summer()
    @staticmethod
    def run(req, res):
        """"user login"""
        # get request data
        data = req.get_json()

        document = data['document']
        topk     = data['topk']

        # start summarize
        result = summary.summer.run(document, topk=topk)

        # make response
        res.message = 'Summarize successfully.'
        res.data    = {
            'summary' : result
        }
        return res