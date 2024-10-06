import unittest

def skip_if_frozen(test_method):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            print('Тесты в этом кейсе заморожены')
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self)
    return wrapper

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Tournament:
    def __init__(self, distance):
        self.distance = distance

    def start(self, runners):
        results = {}
        for runner in runners:
            time = self.distance / runner.speed
            results[time] = runner.name
        return results


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        runner = Runner("Usain Bolt", 9.58)
        self.assertEqual(runner.name, "Usain Bolt")
        self.assertEqual(runner.speed, 9.58)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Marathon Man", 12)
        self.assertEqual(runner.speed, 12)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Walker", 5)
        self.assertEqual(runner.speed, 5)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(100)
        self.assertEqual(tournament.distance, 100)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(200)
        self.assertEqual(tournament.distance, 200)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(300)
        self.assertEqual(tournament.distance, 300)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(RunnerTest))
    suite.addTests(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
