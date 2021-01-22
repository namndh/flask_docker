import pytest
from typing import List, Dict, Any
from app.utils import compute_quantile


def test_quantile():
    test_cases: List[Dict[str, Any]] = [
        {
            "name": "happy case",
            "pool": [1, 2, 5, 4, 3],
            "percentile": 50,
            "result": float(3),
        },
        {
            "name": "wrong_percentile",
            "pool": [1, 2, 3, 4, 5],
            "percentile": 120,
            "result": ValueError
        },
        {
            "name": "list_with_length_1",
            "pool": [1],
            "percentile": 60,
            "result": float(1)
        },
        {
            "name": "pos_less_than_1",
            "pool": [1, 2 ,4 ,5 ,3],
            "percentile": 2,
            "result": float(1)
        }
    ]
    for test_case in test_cases:
        if not isinstance(test_case["result"], float):
            with pytest.raises(test_case["result"]):
                compute_quantile(pool=test_case["pool"], percentile=test_case["percentile"])
        else:
            quantile_value = compute_quantile(pool=test_case["pool"], percentile=test_case["percentile"])
            assert quantile_value == test_case["result"], test_case["name"]
