class ScoreError(Exception):
    """The score informed isn't between the values."""

    def __init__(self, n1):

        # Call the base class constructor with the parameters it needs
        self.message = f"The score {n1} is not between 600-1000."
        super().__init__(self.message)


class TermError(Exception):
    """The term informed isn't between the values."""

    def __init__(self, n1):

        # Call the base class constructor with the parameters it needs
        self.message = f"The term {n1} is not between [6, 9, 12]."
        super().__init__(self.message)
