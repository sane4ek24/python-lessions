import runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(levelname)s, %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            rn = runner.Runner("random_name")
            for i in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            rn1 = runner.Runner("random_name1")
            for i in range(10):
                rn1.run()
            self.assertEqual(rn1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        rn2 = runner.Runner("random_name2")
        rn3 = runner.Runner("random_name3")
        for i in range(11):
            rn2.run()
            rn3.walk()
        self.assertNotEqual(rn2.distance, rn3.distance)


if __name__ == "__main__":
    test = RunnerTest()
    test.test_walk()
    test.test_run()
