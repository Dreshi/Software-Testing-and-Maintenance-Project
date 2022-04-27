import unittest
from BowlingGameSet import BowlingGame


class TestBowlingGame(unittest.TestCase):

    """ Description	"""

    def setUp(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        self.game = BowlingGame()

    def testGutterGame(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        self.rollMany(0, 20)  # it was important to use the rollMany() here
        assert self.game.score() == 0

    def testAllOnes(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):  # method name was used twise
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """    # in order to not get the IndexError: list index out of range error, it was important to delete the s from rolls()
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """    # in order to not get the IndexError: list index out of range error, it was important to delete the s from rolls()

        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """

        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testAllSpare(self):  # naming had to be changed - the method name testOneSpare(self) was used 2x, plus this one was actually checking for all spares
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """

        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        """ Description
        :type self:
        :param self:

        :type pins:
        :param pins:

        :type rolls:
        :param rolls:

        :raises:

        :rtype:
        """
        for i in range(rolls):
            self.game.roll(pins)


if __name__ == '__main__':

    """ Description
    :raises:

    :rtype:
    """
    unittest.main()
