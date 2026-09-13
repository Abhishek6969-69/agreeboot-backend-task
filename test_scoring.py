from scoring import compute_score


def test_missing_marker_does_not_reduce_pillar_score():
    readings = {
        "resting_heart_rate": 60,
    }

    result = compute_score(readings)

    assert result["pillars"]["fitness"] == 250.0


def test_missing_pillar_does_not_crash():
    readings = {
        "resting_heart_rate": 60,
    }

    result = compute_score(readings)

    assert result["pillars"]["metabolic"] == 0.0



def test_known_report_score():
    readings = {
        "fasting_glucose": 92,
        "hba1c": 5.3,
        "triglycerides": 168,
        "resting_heart_rate": 64,
        "vo2_max": 41,
        "reaction_time_ms": 392,
        "sleep_hours": 6.4,
        "sleep_efficiency": 0.9,
        "steps_per_day": 6100,
    }

    result = compute_score(readings)

    assert result["total"] == 946