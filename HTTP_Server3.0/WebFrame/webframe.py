"""
webframe

"""

from socket import *
import json
from settings import *
from select import select
from urls import *


#应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []

        self.sockfd = socket()
        self.sockfd.bind(ADDR)
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, Debug)
        self.sockfd.listen(5)
        self.rlist.append(self.sockfd)
    def start(self):
        print('Start app listen',ADDR)
        while True:
            rs,ws,xs= select(self.rlist,
                             self.wlist,
                             self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    def get_html(self,info):
        if info == '/':
            filename = INDEX_DIR + "/index.html"
        else:
            filename = INDEX_DIR + info
        try:
            fd = open(filename)
        except Exception as e:
            return {'status': '404', 'data': '没有找到'}
        else:
            return {'status': '200', 'data': fd.read()}

    # 处理数据
    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': 'Sorry..'}
    #处理具体的httpserver请求
    def handle(self,c):
        request = c.recv(1024).decode()
        request = json.loads(request)
        print(request)
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        c.send(json.dumps(response).encode())
        c.close()


if __name__ == '__main__':
    app = Application()
    app.start()
