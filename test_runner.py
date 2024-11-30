import  runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner("test walker")
        for _ in range(10):
            walker.walk()
        self.assertEquals(walker.distance, 50)

    def test_run(self):
        runner_ = runner.Runner("test runner")
        for _ in range(10):
            runner_.run()
        self.assertEquals(runner_.distance,100)

    def test_challenge(self):
        runner1 = runner.Runner("test runner1")
        walker2 = runner.Runner("test walker2")
        for _ in range(10):
            walker2.walk()
            runner1.run()
        self.assertNotEquals(runner1.distance, walker2.distance)


