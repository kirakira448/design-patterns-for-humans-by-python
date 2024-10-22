from abc import ABC, abstractmethod
import unittest


class JobPost:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title


class Observer(ABC):
    @abstractmethod
    def on_job_posted(self, job_post: JobPost):
        pass

class JobSeeker(Observer):
    def __init__(self, name):
        self._name = name

    def on_job_posted(self, job_post: JobPost):
        print(f"Hi {self._name}! New job posted: {job_post.get_title()}")


class Observable:
    def __init__(self):
        self._observers = []
    
    @abstractmethod 
    def attach(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self, job_post: JobPost):
        pass

    
class EmploymentAgency(Observable):
    def __init__(self):
        super().__init__()

    def notify(self, job_post: JobPost):
        for observer in self._observers:
            observer.on_job_posted(job_post)

    def attach(self, observer: Observer):
        self._observers.append(observer)    

    def add_job(self, job_post: JobPost):
        self.notify(job_post)


class TestObserver(unittest.TestCase):
    def test_observer(self):
        job_post = JobPost("Software Engineer")
        job_seeker1 = JobSeeker("John")
        job_seeker2 = JobSeeker("Jane")
        agency = EmploymentAgency()
        agency.attach(job_seeker1)
        agency.attach(job_seeker2)
        agency.add_job(job_post)


if __name__ == "__main__":
    unittest.main()


