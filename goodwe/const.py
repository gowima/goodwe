"""Constants."""
GOODWE_TCP_PORT = 502
GOODWE_UDP_PORT = 8899

BATTERY_MODES: dict[int, str] = {
    0: "No battery",
    1: "Standby",
    2: "Discharge",
    3: "Charge",
    4: "To be charged",
    5: "To be discharged",
}

ENERGY_MODES: dict[int, str] = {
    0: "Check Mode",
    1: "Wait Mode",
    2: "Normal (On-Grid)",
    4: "Normal (Off-Grid)",
    8: "Flash Mode",
    16: "Fault Mode",
    32: "Battery Standby",
    64: "Battery Charging",
    128: "Battery Discharging",
}

GRID_MODES: dict[int, str] = {
    0: "Not connected to grid",
    1: "Connected to grid",
    2: "Fault",
}

GRID_IN_OUT_MODES: dict[int, str] = {
    0: "Idle",
    1: "Exporting",
    2: "Importing",
}

LOAD_MODES: dict[int, str] = {
    0: "Inverter and the load is disconnected",
    1: "The inverter is connected to a load",
}

PV_MODES: dict[int, str] = {
    0: "PV panels not connected",
    1: "PV panels connected, no power",
    2: "PV panels connected, producing power",
}

WORK_MODES: dict[int, str] = {
    0: "Wait Mode",
    1: "Normal",
    2: "Error",
    4: "Check Mode",
}

WORK_MODES_ET: dict[int, str] = {
    0: "Wait Mode",
    1: "Normal (On-Grid)",
    2: "Normal (Off-Grid)",
    3: "Fault Mode",
    4: "Flash Mode",
    5: "Check Mode",
}

WORK_MODES_ES: dict[int, str] = {
    0: "Inverter Off - Standby",
    1: "Inverter On",
    2: "Inverter Abnormal, stopping power",
    3: "Inverter Severly Abnormal, 20 seconds to restart",
}

SAFETY_COUNTRIES: dict[int, str] = {
    0: "IT CEI 0-21",
    1: "CZ-A1",
    2: "DE LV with PV",
    3: "ES-A",
    4: "GR",
    5: "DK2",
    6: "BE",
    7: "RO-A",
    8: "GB G98",
    9: "Australia A",
    10: "FR mainland",
    11: "China",
    12: "60Hz 230Vac Default",
    13: "PL LV",
    14: "South Africa",
    16: "Brazil 220Vac",
    17: "Thailand MEA",
    18: "Thailand PEA",
    19: "Mauritius",
    20: "NL-A",
    21: "G98/NI",
    22: "China Higher",
    23: "FR island 50Hz",
    24: "FR island 60Hz",
    25: "Australia Ergon",
    26: "Australia Energex",
    27: "NL 16/20A",
    28: "Korea",
    29: "China Utility",
    30: "AT-A",
    31: "India",
    32: "50Hz 230Vac Default",
    33: "Warehouse",
    34: "Philippines",
    35: "IE-16/25A",
    36: "Taiwan",
    37: "BG",
    38: "Barbados",
    39: "China Highest",
    40: "GB G99-A",
    41: "SE LV",
    42: "Chile BT",
    43: "Brazil 127Vac",
    44: "Newzealand",
    45: "IEEE1547 208Vac",
    46: "IEEE1547 220Vac",
    47: "IEEE1547 240Vac",
    48: "60Hz 127Vac Default",
    49: "50Hz 127Vac Default",
    50: "Australia WAPN",
    51: "Australia MicroGrid",
    52: "JP 50Hz",
    53: "JP 60Hz",
    54: "India Higher",
    55: "DEWA LV",
    56: "DEWA MV",
    57: "SK",
    58: "NZ GreenGrid",
    59: "HU",
    60: "Sri Lanka",
    61: "ES island",
    62: "Ergon30K",
    63: "Energex30K",
    64: "IEEE1547 230/400Vac",
    65: "IEC61727 60Hz",
    66: "CH",
    67: "IT CEI 0-16",
    68: "Australia Horizon",
    69: "CY",
    70: "Australia SAPN",
    71: "Australia Ausgrid",
    72: "Australia Essential",
    73: "Australia Victoria",
    74: "Hong Kong",
    75: "PL MV",
    76: "NL-B",
    77: "SE MV",
    78: "DE MV",
    79: "DE LV without PV",
    80: "ES-D",
    81: "Australia Endeavour",
    82: "Argentina",
    83: "Israel LV",
    84: "IEC61727 50Hz",
    85: "Australia B",
    86: "Australia C",
    87: "Chile MT-A",
    88: "Chile MT-B",
    89: "Vietnam",
    90: "reserve14",
    91: "Israel-HV",
    93: "NewZealand:2015",
    94: "RO-D",
    96: "US 208Vac Default",
    97: "US 240Vac Default",
    98: "US CA 208Vac",
    99: "US CA 240Vac",
    100: "cUSA_208VacCA_SDGE",
    101: "cUSA_240VacCA_SDGE",
    102: "cUSA_208VacCA_PGE",
    103: "cUSA_240VacCA_PGE",
    104: "US HI 208Vac",
    105: "US HI 240Vac",
    106: "USA_208VacHECO_14HM",
    107: "USA_240VacHECO_14HM",
    108: "US 480Vac",
    109: "US CA 480Vac",
    110: "US HI 480Vac",
    111: "US Kauai 208Vac",
    112: "US Kauai 240Vac",
    113: "US Kauai 480Vac",
    114: "US ISO-NE 208Vac",
    115: "US ISO-NE 240Vac",
    116: "US ISO-NE 480Vac",
    118: "PR 208Vac",
    119: "PR 240Vac",
    120: "PR 480Vac",
    128: "Poland_B",
    129: "EE",
    135: "CZ-A2",
    136: "CZ-B1",
    146: "Brazil 208Vac",
    147: "Brazil 230Vac",
    148: "Brazil 240Vac",
    149: "Brazil 254Vac",
}

ERROR_CODES: dict[int, str] = {
    31: 'Internal Communication Failure',
    30: 'EEPROM R/W Failure',
    29: 'Fac Failure',
    28: 'DSP communication failure',
    27: 'PhaseAngleFailure',
    26: '',
    25: 'Relay Check Failure',
    24: '',
    23: 'Vac Consistency Failure',
    22: 'Fac Consistency Failure',
    21: '',
    20: 'Back-Up Over Load',
    19: 'DC Injection High',
    18: 'Isolation Failure',
    17: 'Vac Failure',
    16: 'External Fan Failure',
    15: 'PV Over Voltage',
    14: 'Utility Phase Failure',
    13: 'Over Temperature',
    12: 'InternalFan Failure',
    11: 'DC Bus High',
    10: 'Ground I Failure',
    9: 'Utility Loss',
    8: 'AC HCT Failure',
    7: 'Relay Device Failure',
    6: 'GFCI Device Failure',
    5: '',
    4: 'GFCI Consistency Failure',
    3: 'DCI Consistency Failure',
    2: '',
    1: 'AC HCT Check Failure',
    0: 'GFCI Device Check Failure',
}

DIAG_STATUS_CODES: dict[int, str] = {
    0: "Battery voltage low",
    1: "Battery SOC low",
    2: "Battery SOC in back",
    3: "BMS: Discharge disabled",
    4: "Discharge time on",
    5: "Charge time on",
    6: "Discharge Driver On",
    7: "BMS: Discharge current low",
    8: "APP: Discharge current too low",
    9: "Meter communication failure",
    10: "Meter connection reversed",
    11: "Self-use load light",
    12: "EMS: discharge current is zero",
    13: "Discharge BUS high PV voltage",
    14: "Battery Disconnected",
    15: "Battery Overcharged",
    16: "BMS: Temperature too high",
    17: "BMS: Charge too high",
    18: "BMS: Charge disabled",
    19: "Self-use off",
    20: "SOC delta too volatile",
    21: "Battery self discharge too high",
    22: "Battery SOC low (off-grid)",
    23: "Grid wave unstable",
    24: "Export power limit set",
    25: "PF value set",
    26: "Real power limit set",
    27: "DC output on",
    28: "SOC protect off",
    30: "BMS: Emergency charging",
}

BMS_ALARM_CODES: dict[int, str] = {
    15: 'Charging over-voltage 3',
    14: 'Discharging under-voltage 3',
    13: 'Cell temperature high 3',
    12: 'Communication failure 2',
    11: 'Charging circuit failure',
    10: 'Discharging circuit failure',
    9: 'Battery lock',
    8: 'Battery break',
    7: 'DC bus fault',
    6: 'Precharge fault',
    5: 'Discharging over-current 2',
    4: 'Charging over-current 2',
    3: 'Cell temperature low 2',
    2: 'Cell temperature high 2',
    1: 'Discharging under-voltage 2',
    0: 'Charging over-voltage 2',
}

BMS_WARNING_CODES: dict[int, str] = {
    11: 'System temperature high',
    10: 'System temperature low 2',
    9: 'System temperature low 1',
    8: 'Cell imbalance',
    7: 'System reboot',
    6: 'Communication failure 1',
    5: 'Discharging over-current 1',
    4: 'Charging over-current 1',
    3: 'Cell temperature low 1',
    2: 'Cell temperature high 1',
    1: 'Discharging under-voltage 1',
    0: 'Charging over-voltage 1',
}

DERATING_MODE_CODES: dict[int, str] = {
    31: '',
    30: '',
    29: '',
    28: '',
    27: '',
    26: '',
    25: '',
    24: '',
    23: '',
    22: '',
    21: '',
    20: '',
    19: '',
    18: '',
    17: '',
    16: '',
    15: '',
    14: '',
    13: '',
    12: '',
    11: '',
    10: 'Power calibration limit power (For ATS)',
    9: 'Overvoltage derating (For GW)',
    8: 'Maximum current derating',
    7: 'Limited power start derating',
    6: 'DRED derating',
    5: 'Export power derating',
    4: 'PU Curve',
    3: 'Power VS Frequency',
    2: 'Reactive power derating(PF/QU/FixQ)',
    1: 'Active power derating',
    0: 'Overtemperature derating',
}
