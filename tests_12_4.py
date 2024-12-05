import logging
from rt_with_exceptions import Runner
import unittest

logging.basicConfig(level=logging.DEBUG, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_case = [("вася", 5),("петя", -5)]
        for name, speed in test_case:
            with self.subTest(name=name, speed=speed):
                try:
                    walker = Runner(name, speed)
                    logging.info(f'"test_walk" для {name} со скоростью {speed} выполнен успешно!')
                    for _ in range(10):
                        walker.walk()
                    self.assertEquals(walker.distance, 50)
                except ValueError:
                    logging.warning(f"Неверная скорость {speed} для Runner {name}", exc_info=True)


    def test_run(self):
        test_case = [("семен", 5), (123456, 5)]
        for name, speed in test_case:
            with self.subTest(name=name, speed=speed):
                try:
                    runner_ = Runner(name, speed)
                    logging.info(f'"test_run" для {name} выполнен успешно!')
                    for _ in range(10):
                        runner_.run()
                    self.assertEquals(runner_.distance,100)
                except TypeError:
                    logging.warning(f"Неверный тип данных для объекта Runner {name}", exc_info=True)


if __name__=='__main__':
    unittest.main()