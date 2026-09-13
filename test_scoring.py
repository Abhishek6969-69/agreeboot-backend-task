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