from normalization import normalize_marker


def test_glucose_fasting_normalizes_to_fasting_glucose():
    assert normalize_marker("glucose_fasting") == "fasting_glucose"


def test_fbs_normalizes_to_fasting_glucose():
    assert normalize_marker("FBS") == "fasting_glucose"


def test_a1c_normalizes_to_hba1c():
    assert normalize_marker("A1c") == "hba1c"


def test_hba1c_alias_normalizes_to_hba1c():
    assert normalize_marker("HbA1C") == "hba1c"


def test_trigs_normalizes_to_triglycerides():
    assert normalize_marker("trigs") == "triglycerides"


def test_unknown_marker_is_ignored():
    assert normalize_marker("some_unknown_marker") is None


