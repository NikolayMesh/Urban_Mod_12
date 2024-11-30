import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):
    all_results ={}

    @classmethod
    def setUpClass(cls):
        """setUpClass - метод, где создаётся атрибут класса all_results.
        Это словарь в который будут сохраняться результаты всех тестов."""
        cls.all_results = {}


    def setUp(self):

        """Создание бегунов с указанными именами и скоростями
            Бегун по имени Усэйн, со скоростью 10.
            Бегун по имени Андрей, со скоростью 9.
            Бегун по имени Ник, со скоростью 3."""

        self.usain = runner_and_tournament.Runner("Усэйн", speed=10)
        self.andrey = runner_and_tournament.Runner("Андрей", speed=9)
        self.nik = runner_and_tournament.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):

        """tearDownClass - метод, где выводятся all_results по очереди в столбец."""

        print("\nРезультаты всех тестов:")
        for key in sorted(cls.all_results.keys()):
            finishers = cls.all_results[key]
            result_str = {place: str(runner) for place, runner in finishers.items()}
            print(result_str)


    def test_tournament_usain_nik(self):

        tournament = runner_and_tournament.Tournament(90,  *[self.usain, self.nik])
        results = tournament.start()
        TournamentTest.all_results[1] = results

        """Проверяем, что Ник финишировал последним"""
        last_runner_name = results[max(results.keys())].name
        self.assertTrue(last_runner_name == "Ник")

    def test_tournament_andrey_nik(self):

        tournament = runner_and_tournament.Tournament(90,  *[self.andrey, self.nik])
        results = tournament.start()
        TournamentTest.all_results[2] = results

        """Проверяем, что Ник финишировал последним"""
        last_runner_name = results[max(results.keys())].name
        self.assertTrue(last_runner_name == "Ник")

    def test_tournament_usain_andrey_nik(self):

        tournament = runner_and_tournament.Tournament(90,  *[self.usain,self.andrey, self.nik])
        results = tournament.start()
        TournamentTest.all_results[3] = results

        """Проверяем, что Ник финишировал последним assertEqual"""
        last_runner_name = results[max(results.keys())].name
        self.assertEqual(last_runner_name, "Ник")


if __name__ == '__main__':
    unittest.main()