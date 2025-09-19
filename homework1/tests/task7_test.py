from task7 import summarize
import numpy as np
###################################TESTS###########

def test_summarize():
    stats = summarize([1,2,3,4,5])
    assert stats["mean"] == 3
    assert stats["median"] == 3
    assert np.isclose(stats["std"], np.std([1, 2, 3, 4, 5], ddof=0))