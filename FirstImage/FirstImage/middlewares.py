from fake_useragent import UserAgent


class UserAgentDownloadMiddleware(object):
    def process_request(self, request, spider):
        # if self.user_agent:
        # request.headers.setdefault(b'User-Agent', 'abc')
        request.headers.setdefault(b'User-Agent', UserAgent().random)
