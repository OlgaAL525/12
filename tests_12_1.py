import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runner.Runner('Олень')
        i = 1
        while i <= 10:
            runner_1.walk()
            i += 1
        self.assertEqual(runner_1.distance, 50)
    def test_run(self):
        runner_2 = runner.Runner('Волк')
        i = 1
        while i <= 10:
            runner_2.run()
            i += 1
        self.assertEqual(runner_2.distance, 100)
    def test_challenge(self):
        runner_3 = runner.Runner('Волк1')
        runner_4 = runner.Runner('Олень1')
        i = 1
        while i <= 10:
            runner_3.run()
            runner_4.walk()
            i += 1
        self.assertNotEqual(runner_3.distance, runner_4.distance, 'Волк1 не догонит Оленя1' )
