import unittest
import tests_12_1
import tests_12_2

check = unittest.TestSuite()
check.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
check.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(check)