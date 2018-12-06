from mock import patch
from pysparkling import Context
from jobs.hmmsearch import analyze

@patch('jobs.hmmsearch.HmmSearchContext.initalize_counter')
@patch('jobs.hmmsearch.HmmSearchContext.inc_counter')
def test_hmmsearch_analyze(_, __):
    result = analyze(Context())
    assert len(result) == 327
