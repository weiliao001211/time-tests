# @Author : Wei Liao
# @Time : 2024/10/28 09:40
from times import compute_overlap_time, time_range
import pytest

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected


def test_non_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:00:00", "2010-01-12 13:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected


def test_both_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:00:00", "2010-01-12 10:45:00", 2, 60)
    expected = [('2010-01-12 10:00:00', '2010-01-12 10:22:00'), ('2010-01-12 10:23:00', '2010-01-12 10:45:00')]
    assert compute_overlap_time(large, short) == expected


def test_endstart_same():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected


def test_time_range_backwards_error():
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2024-10-10 12:00:00", "2024-10-09 12:00:00")