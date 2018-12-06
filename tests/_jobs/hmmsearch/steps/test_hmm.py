from jobs.hmmsearch.steps.hmm import parse


def test_parse_hmm():
    stream = parse(open("/data/src/tara-ocean-analysis/data/Pfam-A.hmm"))
    hmms = [hmm for hmm in stream]
    assert len(hmms) > 0
    assert hmms[0]['EFFN'] == '19.774048'
