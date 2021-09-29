from Array import Array
import openpyxl

class ExcelMaker:
    def __init__(self, filename) -> None:
        self.__filename = filename
        self.book = openpyxl.Workbook()
    
    def load_work_book(self, filename_to_load, read_only=False, keep_vba=False, data_only=False, keep_links=True) -> None:
        self.book = openpyxl.load_workbook(
            filename=filename_to_load,
            read_only=read_only,
            keep_vba=keep_vba,
            keep_links=keep_links,
            data_only=data_only
        )

    def save(self, filename="", path="") -> None:
        if filename:
            self.book.save(f"{path}{filename}")
        else:
            self.book.save(f"{path}{self.__filename}")

    def write_in_work_sheet(self, work_sheet="Sheet", data=[]):
        _data = Array(data)

        sheet = self.book[work_sheet] 

        if _data.length:
            pass
