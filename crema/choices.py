from enum import Enum


class EventType(Enum):
    # PSCORE
    USER = "USER"
    LOAN_APPLICATION = "LOAN_APPLICATION"
    DOCUMENT = "DOCUMENT"
    LOAN = "LOAN"
    USER_INFO_REQUEST = "USER_INFO_REQUEST"
    EMPLOYMENT = "EMPLOYMENT"
    DEBIT_INSTRUCTION = "DEBIT_INSTRUCTION"
    ADDRESS = "ADDRESS"
    BANK_ACCOUNT = "BANK_ACCOUNT"
    INCOME_VERIFICATION = "INCOME_VERIFICATION"
    USER_REFERENCES = "USER_REFERENCES"
    ASSISTANCE_REMINDER = "ASSISTANCE_REMINDER"
    ASSISTANCE_ACTIVITY = "ASSISTANCE_ACTIVITY"
    WHATSAPP_COMM = "WHATSAPP_COMM"
    OPS_COMMENT = "OPS_COMMENT"
    ASSISTANCE_AGENT_CALL = "ASSISTANCE_AGENT_CALL"
    DEVICE_INSTALLATION = "DEVICE_INSTALLATION"
    USER_AGENT_ASSIGNMENT = "USER_AGENT_ASSIGNMENT"
    ASSISTANCE_USER_TAG = "ASSISTANCE_USER_TAG"
    LOAN_RESTRUCTURE = "LOAN_RESTRUCTURE"
    MORATORIUM = "MORATORIUM"
    KYC_VERIFICATION = "KYC_VERIFICATION"
    COMMUNICATION = "COMMUNICATION"
    PSCORE_PRODUCT_ELIGIBILITY = "PSCORE_PRODUCT_ELIGIBILITY"
    REFERENCE_META = "REFERENCE_META"
    USER_REGISTRATION = "USER_REGISTRATION"
    USER_UPDATION = "USER_UPDATION"

    # Assessment Engine
    AE_ASSESSMENT = "AE_ASSESSMENT"

    # AMS
    ASSESSMENT = "ASSESSMENT"
    PRODUCT_ELIGIBILITY = "PRODUCT_ELIGIBILITY"
    BUREAU_ADDRESS = "BUREAU_ADDRESS"
    SMS = "SMS"
    PERFIOS_FEATURES = "PERFIOS_FEATURES"

    # NBFC AMS
    NBFC_ASSESSMENT = "NBFC_ASSESSMENT"
    USER_OBLIGATION = "USER_OBLIGATION"
    AML = "AML"
    CIBIL_PORTFOLIO_SCRUB_CIR_INSERTIONS = "CIBIL_PORTFOLIO_SCRUB_CIR_INSERTIONS"
    CIBIL_PORTFOLIO_SCRUB_CIR_WITH_ALGOS_INSERTIONS = "CIBIL_PORTFOLIO_SCRUB_CIR_WITH_ALGOS_INSERTIONS"
    EXTERNAL_BUREAU_REPORT = "EXTERNAL_BUREAU_REPORT"
    XPRESS_REASSESSMENT = "XPRESS_REASSESSMENT"
    USER_UNDERWRITING_DATA = "USER_UNDERWRITING_DATA"

    # USER_ACTIVITY
    USER_ACTIVITY = "USER_ACTIVITY"

    # PAYMENTS
    LOAN_INFO_STATIC = "LOAN_INFO_STATIC"
    LOAN_INFO_DYNAMIC = "LOAN_INFO_DYNAMIC"
    VIRTUAL_ACCOUNT = "VIRTUAL_ACCOUNT"
    LOAN_REPAYMENT = "LOAN_REPAYMENT"
    CUSTOMER_REASSESSMENT = "CUSTOMER_REASSESSMENT"
    LOAN_ALLOCATION_REQUEST = "LOAN_ALLOCATION_REQUEST"
    BT_CANCELLATION = "BT_CANCELLATION"
    NACH_REJECTION = "NACH_REJECTION"

    # Hades
    LOAN_ALLOCATION = "LOAN_ALLOCATION"
    PL_COMMUNICATION = "PL_COMMUNICATION"
    SEND_COLLECTION_MESSAGES = "SEND_COLLECTION_MESSAGES"

    # Bureau
    BUREAU_DATA = "BUREAU_DATA"

    # INTERNAL TOPICS
    # All internal topics start with prefix I_
    I_LOAN_APPLICATION_INDEX = "I_LOAN_APPLICATION_INDEX"
    I_LEAD_INDEX = "I_LEAD_INDEX"
    I_SALES_FORCE = "I_SALES_FORCE"
    I_CLEVER_TAP = "I_CLEVER_TAP"
    I_HADES = "I_HADES"
    I_LEAD_SQUARED = "I_LEAD_SQUARED"
    I_TRACKWIZZ = "I_TRACKWIZZ"
    I_BUREAU_DATA = "I_BUREAU_DATA"

    # TELEMETRY
    RAW_SMS = "RAW_SMS"

    # PROMPT TOPICS
    # All topics where a prompt/trigger needs to be sent to a service to take some action will start with P_
    P_ACTION = "P_ACTION"


class EventPartition(Enum):
    # PSCORE
    USER = 16
    LOAN_APPLICATION = 16
    DOCUMENT = 8
    LOAN = 8
    USER_INFO_REQUEST = 8
    EMPLOYMENT = 8
    DEBIT_INSTRUCTION = 8
    ADDRESS = 8
    BANK_ACCOUNT = 8
    INCOME_VERIFICATION = 8
    USER_REFERENCES = 8
    ASSISTANCE_REMINDER = 8
    ASSISTANCE_ACTIVITY = 16
    WHATSAPP_COMM = 8
    OPS_COMMENT = 8
    ASSISTANCE_AGENT_CALL = 8
    DEVICE_INSTALLATION = 8
    USER_AGENT_ASSIGNMENT = 8
    ASSISTANCE_USER_TAG = 8
    LOAN_RESTRUCTURE = 8
    MORATORIUM = 8
    KYC_VERIFICATION = 8
    COMMUNICATION = 8
    PSCORE_PRODUCT_ELIGIBILITY = 4
    REFERENCE_META = 4
    USER_REGISTRATION = 4
    USER_UPDATION = 4

    # Assessment Engine
    AE_ASSESSMENT = 8

    # AMS
    ASSESSMENT = 16
    PRODUCT_ELIGIBILITY = 8
    BUREAU_ADDRESS = 8
    SMS = 8
    PERFIOS_FEATURES = 2

    # NBFC AMS
    NBFC_ASSESSMENT = 16
    USER_OBLIGATION = 8
    AML = 8
    CIBIL_PORTFOLIO_SCRUB_CIR_INSERTIONS = 4
    CIBIL_PORTFOLIO_SCRUB_CIR_WITH_ALGOS_INSERTIONS = 4
    EXTERNAL_BUREAU_REPORT = 4
    XPRESS_REASSESSMENT = 8
    USER_UNDERWRITING_DATA = 4

    # USER_ACTIVITY
    USER_ACTIVITY = 128

    # PAYMENTS
    LOAN_INFO_STATIC = 8
    LOAN_INFO_DYNAMIC = 32
    VIRTUAL_ACCOUNT = 8
    LOAN_REPAYMENT = 8
    LOAN_ALLOCATION_REQUEST = 4
    CUSTOMER_REASSESSMENT = 4
    BT_CANCELLATION = 4
    NACH_REJECTION = 4

    # Hades
    LOAN_ALLOCATION = 8
    PL_COMMUNICATION = 16
    SEND_COLLECTION_MESSAGES = 8

    # Bureau
    BUREAU_DATA = 8

    # INTERNAL TOPICS
    I_LOAN_APPLICATION_INDEX = 64
    I_LEAD_INDEX = 64
    I_SALES_FORCE = 64
    I_CLEVER_TAP = 64
    I_HADES = 8
    I_LEAD_SQUARED = 32
    I_TRACKWIZZ = 8
    I_BUREAU_DATA = 8

    # TELEMETRY
    RAW_SMS = 8

    # PROMPT TOPICS
    P_ACTION = 8
