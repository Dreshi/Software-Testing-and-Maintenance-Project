class BowlingGame:

    """ Description	"""

    def __init__(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        self.rolls = []

    def roll(self, pins):
        """ Description
        :type self:
        :param self:

        :type pins:
        :param pins:

        :raises:

        :rtype:
        """
        self.rolls.append(pins)

    def score(self):
        """ Description
        :type self:
        :param self:

        :raises:

        :rtype:
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):  # checking the possibility of 10 turns
            if frameIndex in range(10):  # checking if the first throw was a strike
                # indentation was wrong and if statement was necessary to check for a strike
                if self.isStrike(rollIndex):
                    result += self.strikeScore(rollIndex)
                    rollIndex += 1
                elif self.isSpare(rollIndex):
                    result += self.spareScore(rollIndex)
                    rollIndex += 2
                else:
                    result += self.frameScore(rollIndex)
                    rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """ Description
        :type self:
        :param self:

        :type rollIndex:
        :param rollIndex:

        :raises:

        :rtype:
        """

        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """ Description
        :type self:
        :param self:

        :type rollIndex:
        :param rollIndex:

        :raises:

        :rtype:
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10

    def strikeScore(self, rollIndex):  # method was misspelled
        """ Description
        :type self:
        :param self:

        :type rollIndex:
        :param rollIndex:

        :raises:

        :rtype:
        """
        return 10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]

    def spareScore(self, rollIndex):
        """ Description
        :type self:
        :param self:

        :type rollIndex:
        :param rollIndex:

        :raises:

        :rtype:
        """
        return 10 + self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """ Description
        :type self:
        :param self:

        :type rollIndex:
        :param rollIndex:

        :raises:

        :rtype:
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
