import re
from input import puzzle_input
from loguru import logger

class Game(object):
    _RED_MAX = 12
    _GREEN_MAX = 13
    _BLUE_MAX = 14

    def __init__(self, game_data: str = None):
        self.game_id = int(re.search(r'Game (\d+)', game_data).group(1))
        self.red = [int(i) for i in re.findall(r'(\d+) red', game_data)]
        self.green = [int(i) for i in re.findall(r'(\d+) green', game_data)]
        self.blue = [int(i) for i in re.findall(r'(\d+) blue', game_data)]
        logger.debug(f'Game {self.game_id} has red: {self.red}, green: {self.green}, blue: {self.blue}')

    @property
    def possible(self) -> bool:
        impossible = False
        for r in self.red:
            if r > self._RED_MAX:
                impossible = True
                break
        if not impossible:
            for g in self.green:
                if g > self._GREEN_MAX:
                    impossible = True
                    break
        if not impossible:
            for b in self.blue:
                if b > self._BLUE_MAX:
                    impossible = True
                    break
        return (not impossible)


class GameProcessor(object):
    def __init__(self, input: str):
        self.inputs: list[str] = puzzle_input.split('\n')
        self.games: list[Game] = [
            Game(game_data=i) for i in self.inputs
        ]
    
    @property
    def sum(self):
        return sum([
            g.game_id for g in self.games if g.possible
        ])


if __name__ == '__main__':
    game = GameProcessor(input=puzzle_input)
    logger.info(f'\n🎲 Game ID sum: {game.sum}')
