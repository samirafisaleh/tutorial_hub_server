''' Docfile '''

from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    ''' Class module '''

    @task
    def hello_world(self):
        ''' Function module '''

        self.client.get("/hello")
        self.client.get("/world")

    def dummy1(self):
        ''' Dummy 1 '''
        print("dummy1")

    def dummy2(self):
        ''' Dummy 2 '''
        print("dummy2")
