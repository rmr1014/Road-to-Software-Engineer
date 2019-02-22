import DaysOld

# yearHelper() Tests
def test_yearHelper():
    assert DaysOld.yearHelper(2020) == 366

# monthHelper() Tests
def test_monthHelper():
    assert DaysOld.monthHelper(7) == 31

# daysBetweenYears() Tests
def test_daysBetweenYears():
    assert DaysOld.daysBetweenYears(1987, 2019) == 12052
    assert DaysOld.daysBetweenYears(1887, 2019) == 48576

# daysBetweenDateAndNextYear() Tests
# def test_daysBetweenDateAndNextYear():
#     assert DaysOld.daysBetweenDateAndNextYear() == 