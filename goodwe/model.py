from .inverter import Inverter

# Serial number tags to identify inverter type
ET_MODEL_TAGS = ["ETU", "ETL", "ETR", "ETC", "EHU", "EHR", "EHB", "BTU", "BTN", "BTC", "BHU", "AES", "ABP", "HHI",
                 "HSB", "HUA", "CUA",
                 "ESN", "EMN", "ERN", "EBN",  # ES Gen 2
                 "HLB", "HMB", "HBB", "SPN"]  # Gen 2
ES_MODEL_TAGS = ["ESU", "EMU", "ESA", "BPS", "BPU", "EMJ", "IJL"]
DT_MODEL_TAGS = ["DTU", "DTS", "MSU", "MST", "DSN", "DTN", "DST", "NSU", "SSN", "SST", "SSX", "SSY", "PSB", "PSC"]

SINGLE_PHASE_MODELS = ["DSN", "DST", "NSU", "SSN", "SST", "SSX", "SSY",  # DT
                       "MSU", "MST", "PSB", "PSC",
                       "MSC",  # Found on third gen MS
                       "EHU", "EHR", "HSB",  # ET
                       "ESN", "EMN", "ERN", "EBN", "HLB", "HMB", "HBB", "SPN"]  # ES Gen 2

MPPT3_MODELS = ["MSU", "MST", "PSC", "MSC",
                "25KET", "29KET", "29K9ET", "30KET"]

MPPT4_MODELS = ["HSB"]

# =============================================================================
# ADDED gowima: for inverters with 2 strings per mppt
# TODO: possibly incomplete list: GW15K-ET GW20K-ET GW25K-ET GW29.9K-ET
STRING_2_PER_MPPT_MODELS = ["15KET", "20K9ET", "25KET", "29K9ET"]
# =============================================================================

BAT_2_MODELS = ["25KET", "29KET", "29K9ET", "30KET"]


def is_single_phase(inverter: Inverter) -> bool:
    return any(model in inverter.serial_number for model in SINGLE_PHASE_MODELS)


def is_3_mptt(inverter: Inverter) -> bool:
    return any(model in inverter.serial_number for model in MPPT3_MODELS)


def is_4_mptt(inverter: Inverter) -> bool:
    return any(model in inverter.serial_number for model in MPPT4_MODELS)

# =============================================================================
# ADDED gowima: for inverters with 2 strings per mppt
def is_2_strings_per_mppt(inverter: Inverter) -> bool:
    return any(model in inverter.serial_number for model in STRING_2_PER_MPPT_MODELS)
# =============================================================================

def is_2_battery(inverter: Inverter) -> bool:
    return any(model in inverter.serial_number for model in BAT_2_MODELS)
