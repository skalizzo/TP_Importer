import unittest
from src.tpimporter.TVTP_Importer import TVTP_Importer


class test_TPImporter(unittest.TestCase):
    def test_get_tp_data_from_file(self):
        importer = TVTP_Importer()
        series_data, season_data, episode_data = importer.get_tp_data_from_file(path='G:\Listen\TV Titelplanung DD_absolutiert_v2.xlsm')
        print(len(series_data), len(season_data), len(episode_data))
        self.assertTrue(season_data)
        self.assertEqual(type(season_data), list)
        self.assertEqual(type(episode_data), list)
        self.assertEqual(type(series_data), list)
        for title in season_data:
            #print(title)
            self.assertEqual(type(title), dict)
            self.assertTrue('vendor_id_amazon' in title.keys())
            self.assertTrue('licensor' in title.keys())
        for title in series_data:
            #print(title)
            self.assertEqual(type(title), dict)
            self.assertTrue('titel_local' in title.keys())
            self.assertTrue('vendor_id' in title.keys())
        for title in episode_data:
            #print(title)
            self.assertEqual(type(title), dict)
            self.assertTrue('titel_local' in title.keys())
            self.assertTrue('tv_air_date' in title.keys())



if __name__ == '__main__':
    unittest.main()
