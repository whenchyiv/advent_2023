from input import puzzle_input
from loguru import logger
from day02 import Game, GameProcessor


class PowerGame(Game):
    @property
    def red_max(self):
        return max(self.red)

    @property
    def green_max(self):
        return max(self.green)

    @property
    def blue_max(self):
        return max(self.blue)


class PowerGameProcessor(GameProcessor):
    def __init__(self, input: str):
        super().__init__(input=puzzle_input)
        self.games: list[PowerGame] = [
            PowerGame(game_data=i) for i in self.inputs
        ]

    @property
    def total_power(self):
        return sum([
            (g.red_max*g.blue_max*g.green_max) for g in self.games
        ])


if __name__ == '__main__':
    game = PowerGameProcessor(input=puzzle_input)
    logger.info(f'\n💪 Total power: {game.total_power}')
