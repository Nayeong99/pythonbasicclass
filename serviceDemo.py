class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __init__(self):
        print('{} Service가 종료되었습니다.'.format(self.service))

s = Service('길안내')
del s