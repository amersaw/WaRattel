class QuranPageProvider(object):
    def __init__(self):
        pass
    def get_quran_page(self, page):
        return f"https://ia800400.us.archive.org/21/items/Quran4u_Quran_Brown/{str(page).zfill(4)}.jpg"