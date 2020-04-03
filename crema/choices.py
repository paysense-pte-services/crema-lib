from enum import Enum


class EventType(Enum):
    USER = "USER"
    LOAN_APPLICATION = "LOAN_APPLICATION"
    ENTITY = "ENTITY"
    DOCUMENT = "DOCUMENT"
    LOAN = "LOAN"
    ASSESSMENT = "ASSESSMENT"
    USER_INFO_REQUEST = "USER_INFO_REQUEST"
    DOCUMENT = "DOCUMENT"
    EMPLOYMENT = "EMPLOYMENT"
    DEBIT_INSTRUCTION = "DEBIT_INSTRUCTION"