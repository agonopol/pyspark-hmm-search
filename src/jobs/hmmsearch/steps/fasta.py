from Bio import SeqIO
from Bio.Seq import Seq


def parse(stream):
    seqs = SeqIO.parse(stream, 'fasta')
    for seq in seqs:
        yield seq


def transform(sequence):
    description, seq = sequence.description, Seq(str(sequence.seq).upper().replace('X', 'N'))
    f = (-3, -2, -1, 1, 2, 3)
    for i in f:
        if i < 0:
            yield ('%s_%d' % (description, i), seq.reverse_complement()[-(i + 1):].translate(stop_symbol='X'))
        elif i > 0:
            yield ('%s_+%d' % (description, i), seq[i - 1:].translate(stop_symbol='X'))
