class QuranPageProvider(object):
    def __init__(self):
        pass

    def get_quran_page(self, page):
        # https://www.quranflash.com/books/Medina2/data/L/0154.png
        # https://www.quranflash.com/books/MedinaOld/data/L/0154.png
        # https://www.quranflash.com/books/Tajweed/data/L/105.png
        return f"https://ia800400.us.archive.org/21/items/Quran4u_Quran_Brown/{str(page).zfill(4)}.jpg"
