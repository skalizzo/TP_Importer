import unittest
from src.tpimporter.TP_Importer import TP_Importer
from src.tpimporter.adapters.Adapter_for_MAM import Adapter_For_MAM


class test_TPImporter(unittest.TestCase):
    def test_get_tp_data_from_file(self):
        importer = TP_Importer()
        tp_data = importer.get_tp_data_from_file(path='G:\Listen\TPDD aktuell absolutiert.xlsm')
        self.assertTrue(tp_data)
        self.assertEqual(type(tp_data), list)
        for title in tp_data:
            self.assertEqual(type(title), dict)
            self.assertTrue('vendor_id_amazon' in title.keys())
            self.assertTrue('vendor_id_alleskino' in title.keys())

    def test_get_transformed_data(self):
        importer = TP_Importer()
        tp_data = importer.get_tp_data_from_file(path='G:\Listen\TPDD aktuell absolutiert.xlsm')
        adapter = Adapter_For_MAM()
        transformed_data = adapter.transform(tp_data, None)
        for row in transformed_data:
            self.assertTrue('VendorIDAmazon' in row.keys())
        # transform metadata
        transformed_data = adapter.transform(tp_data, transformer_dict=adapter.metadata_dict)
        for row in transformed_data:
            self.assertTrue('IMDBlink' in row.keys())


if __name__ == '__main__':
    unittest.main()
