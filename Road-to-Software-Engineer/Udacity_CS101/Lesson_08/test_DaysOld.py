import DaysOld

# yearHelper() Tests
def test_yearHelper_InputYear_2020_ReturnsDays_366():
    assert DaysOld.yearHelper(2020) == 366

# monthHelper() Tests
def test_monthHelper_InputMonth_7_ReturnsDaysInMonth_31():
    assert DaysOld.monthHelper(7) == 31

# daysBetweenYears() Tests
def test_daysBetweenYears_InputYear1_1987_Year2_2019_ReturnsDays_12052():
    assert DaysOld.daysBetweenYears(1987, 2019) == 12052