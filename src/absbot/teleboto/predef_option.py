from typing import List


class PredefOption:
    def __init__(self, title: str, command: str, pos_row: int, pos_column: int):
        self.title = title
        self.command = command
        self.pos_row = pos_row
        self.pos_column = pos_column
        pass

    @staticmethod
    def KB_PrevNext() -> List["PredefOption"]:
        res: List[PredefOption] = []
        res.append(PredefOption("Next", "next", 0, 0))
        res.append(PredefOption("Previous", "prev", 0, 1))
        return res
