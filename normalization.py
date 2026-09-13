MARKER_ALIASES = {
    "glucose_fasting": "fasting_glucose",
    "FBS": "fasting_glucose",
    "A1c": "hba1c",
    "HbA1C": "hba1c",
    "trigs": "triglycerides",
}

CANONICAL_MARKERS = {
    "fasting_glucose",
    "hba1c",
    "triglycerides",
    "resting_heart_rate",
    "vo2_max",
    "reaction_time_ms",
    "sleep_hours",
    "sleep_efficiency",
    "steps_per_day",
}


def normalize_marker(marker_name):
    if marker_name in CANONICAL_MARKERS:
        return marker_name

    return MARKER_ALIASES.get(marker_name)


def normalize_readings(readings):
    normalized = {}

    for marker, value in readings.items():
        canonical = normalize_marker(marker)

        if canonical is not None:
            normalized[canonical] = value

    return normalized