import unittest
from src.tpimporter.TVTP_Importer import TVTP_Importer


class test_TPImporter(unittest.TestCase):
    def test_get_tp_data_from_file(self):
        importer = TVTP_Importer()
        series_data = importer.get_tp_data_from_file(path='G:\Listen\TV Titelplanung DD_absolutiert_v2.xlsm')
        print(len(series_data))
        self.assertTrue(series_data)
        self.assertEqual(type(series_data), dict)
        num_series, num_seasons, num_episodes = 0, 0, 0
        for vendor_id, series in series_data.items():
            num_series += 1
            #print(series)
            self.assertEqual(type(series), dict)
            self.assertTrue('vendor_id' in series.keys())
            self.assertTrue('seasons' in series.keys())
            for vendor_id_season, season in series.get('seasons').items():
                num_seasons += 1
                #print(season)
                self.assertEqual(type(season), dict)
                self.assertTrue('vendor_id' in season.keys())
                self.assertTrue('episodes' in season.keys())
                self.assertTrue('est_end' in season.keys())
                for vendor_id_episode, episode in season.get('episodes').items():
                    num_episodes += 1
                    #print(episode)
                    self.assertEqual(type(episode), dict)
                    self.assertTrue('vendor_id' in episode.keys())
                    self.assertTrue('titel_local' in episode.keys())
                    self.assertTrue('tvod_start' in episode.keys())
        print(num_series, num_seasons, num_episodes)




if __name__ == '__main__':
    unittest.main()
