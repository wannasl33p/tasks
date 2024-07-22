class LifeGame:
    """
    Class for Game life
    """

    def __init__(self, area: list[list[int]]) -> None:
        self.game_area = area

    def get_next_generation(self) -> list[list[int]]:
        new_game_area = self._create_new_game_area()
        for i in range(len(self.game_area)):
            for j in range(len(self.game_area[i])):
                self._update_cell(new_game_area, i, j)
        self.game_area = new_game_area
        return self.game_area

    def _create_new_game_area(self) -> list[list[int]]:
        return [[k for k in n] for n in self.game_area]

    def _update_cell(self, new_game_area: list[list[int]], i: int, j: int) -> None:
        fish, shrimp = self._get_neighbours(i, j)
        if self.game_area[i][j] == 0:
            if fish == 3:
                new_game_area[i][j] = 2
            elif shrimp == 3:
                new_game_area[i][j] = 3
        elif self.game_area[i][j] == 2:
            if fish > 3 or fish < 2:
                new_game_area[i][j] = 0
        elif self.game_area[i][j] == 3:
            if shrimp > 3 or shrimp < 2:
                new_game_area[i][j] = 0

    def _get_neighbours(self, i: int, j: int) -> tuple[int, int]:
        number_of_fish: int = 0
        number_of_shrimp: int = 0
        for n in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if n == 0 and k == 0:
                    continue
                if self._is_valid_position(i + n, j + k):
                    if self.game_area[i + n][j + k] == 2:
                        number_of_fish += 1
                    elif self.game_area[i + n][j + k] == 3:
                        number_of_shrimp += 1
        return number_of_fish, number_of_shrimp

    def _is_valid_position(self, i: int, j: int) -> bool:
        return -1 < i < len(self.game_area) and -1 < j < len(self.game_area[i])
