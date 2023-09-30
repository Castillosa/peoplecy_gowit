class NotRelatedAnswerException(Exception):
    def __init__(self, message="Not related answer"):
        super().__init__(message)


class WrongQuestionTypeException(Exception):
    def __init__(self, message="Wrong type"):
        super().__init__(message)


class WrongAnswerTypeException(Exception):
    def __init__(self, message="Wrong answer type"):
        super().__init__(message)


class NotRelatedQuestionException(Exception):
    def __init__(self, message="Not related question"):
        super().__init__(message)
