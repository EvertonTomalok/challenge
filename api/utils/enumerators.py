from enum import Enum


class Status(Enum):
    error = 0
    success = 1


class ProcessingStatus(Enum):
    processing = "processing"
    completed = "completed"


class ResultStatus(Enum):
    approved = "approved"
    refused = "refused"


class RefusePolicy(Enum):
    age = "age"
    score = "score"
    commitment = "commitment"
