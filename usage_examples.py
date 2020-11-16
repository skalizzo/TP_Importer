from src import TP_Importer
from src import Adapter_For_MAM

def import_tp_data_for_mam():
    tp_path = "G:\Listen\TPDD aktuell absolutiert.xlsm"
    tp_data = TP_Importer().get_tp_data_from_file(tp_path)
    tp_data_mam = Adapter_For_MAM().transform(tp_data)
    for title in tp_data_mam:
        print(title)


if __name__ == '__main__':
    import_tp_data_for_mam()