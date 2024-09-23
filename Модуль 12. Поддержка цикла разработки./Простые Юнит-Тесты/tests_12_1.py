import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = runner.Runner("random_name")
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn1 = runner.Runner("random_name1")
        for i in range(10):
            rn1.run()
        self.assertEqual(rn1.distance, 100)

    def test_challenge(self):
        rn2 = runner.Runner("random_name2")
        rn3 = runner.Runner("random_name3")
        for i in range(11):
            rn2.run()
            rn3.walk()
        self.assertNotEqual(rn2.distance, rn3.distance)


if __name__ == "__main__":
    unittest.main()
