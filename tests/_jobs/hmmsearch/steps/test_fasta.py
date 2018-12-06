from jobs.hmmsearch.steps.fasta import parse
from shared.s3 import stream as s3stream

def test_parse_fasta():
    stream = parse(s3stream("https://s3.amazonaws.com/tara-ocean/fasta/CERZ01.fasta.gz"))
    seqs = [seq for seq in stream]
    assert len(seqs) > 0
    assert seqs[0].description == 'ENA|CERZ01000001|CERZ01000001.1 Marine metagenome genome assembly, contig: TARA_082_DCM_<-0.22_scaffold2_1'
