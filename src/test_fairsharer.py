from fairsharer import fair_sharer

def test_fair_sharer():
    """Test the fair_sharer function."""
    result = fair_sharer([1000], 1)
    assert result == [1000.0]
    result = fair_sharer([1000, 800], 1)
    assert result == [800.0, 1000.0]
    result = fair_sharer([1000, 800, 0], 1)
    assert result == [800.0, 900.0, 100.0]
    result = fair_sharer([0, 1000, 800, 0], 0)
    assert result == [0.0, 1000.0, 800.0, 0.0]
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert result == [100.0, 800.0, 900.0, 0.0]
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert result == [100.0, 890.0, 720.0, 90.0]
    result = fair_sharer([-100, 200, 300], 1)
    assert result == [-70.0, 230.0, 240.0]
    result = fair_sharer([-100, -200, -50], 1)
    assert result == [-105.0, -205.0, -40.0]
    result = fair_sharer([0, 200, 200, 0], 1)
    assert result == [20.0, 160.0, 220.0, 0]
