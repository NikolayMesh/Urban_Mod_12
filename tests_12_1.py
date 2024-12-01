import  runner
import unittest

is_frozen = False

class RunnerTest(unittest.TestCase):
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
         Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual
          сравните distance этого объекта со значением 50."""
        walker = runner.Runner("test walker")
        for _ in range(10):
            walker.walk()
        self.assertEquals(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
         Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual
         сравните distance этого объекта со значением 100."""
        runner_ = runner.Runner("test runner")
        for _ in range(10):
            runner_.run()
        self.assertEquals(runner_.distance,100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
         Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть
         разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов."""
        runner1 = runner.Runner("test runner1")
        walker2 = runner.Runner("test walker2")
        for _ in range(10):
            walker2.walk()
            runner1.run()
        self.assertNotEquals(runner1.distance, walker2.distance)


if __name__=='__main__':
    unittest.main()