from enum import Enum

class DocumentStatus(Enum):
    NEGATIVE = "negative"
    POSITIVE = "positive"
    INVALID = "invalid"
    PENDING = "pending"

class DataOrigin(Enum):
    MANUAL = "manual"
    API = "api"

class EntityType(Enum):
    FEDERAL = "federal"
    STATE = "state"
    MUNICIPAL = "municipal"
    LABOR = "labor"
