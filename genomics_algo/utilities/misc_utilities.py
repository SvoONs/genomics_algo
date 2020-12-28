import random

from typing import Dict, List


class Bases:
    A = "A"
    C = "C"
    G = "G"
    T = "T"


COMPLEMENTARY_BASE = {
    Bases.A: Bases.T,
    Bases.C: Bases.G,
    Bases.G: Bases.C,
    Bases.T: Bases.A,
    "N": "N",
}


def reverse_complement(s: str) -> str:
    """
    Find the reverse complement of a DNA strand
    s: A DNA sequence of a strand - the string must have the characters A, C, G and T

    Returns:
        DNA sequence of the opposite strand in the reverse order

    >>> reverse_complement("ATGC")
    'GCAT'
    >>> reverse_complement("")
    ''
    """
    # TODO: make robust against garbage values
    return "".join([COMPLEMENTARY_BASE[base] for base in s[::-1]])


def generate_artificial_reads(
    genome: str, number_of_reads: int, read_length: int
) -> List[str]:
    """Generate a set of reads randomly from a genome"""
    reads = []
    for _ in range(number_of_reads):
        start_position = random.randint(0, len(genome) - read_length + 1)
        reads.append(genome[start_position : start_position + read_length + 1])
    return reads


def get_frequency_map(text: str, substring_length: int) -> Dict[str, int]:
    """
    Find the frequency of all substring of length in a given text
    >>> get_frequency_map("GTACGTACC", 1)
    {'G': 2, 'T': 2, 'A': 2, 'C': 3}
    >>> get_frequency_map("GTACGTACC", 2)
    {'GT': 2, 'TA': 2, 'AC': 2, 'CG': 1, 'CC': 1}
    >>> get_frequency_map("GTACGTACC", 4)
    {'GTAC': 2, 'TACG': 1, 'ACGT': 1, 'CGTA': 1, 'TACC': 1}
    >>> get_frequency_map("GTACGTACC", 6)
    {'GTACGT': 1, 'TACGTA': 1, 'ACGTAC': 1, 'CGTACC': 1}
    """
    assert substring_length > 0
    assert len(text) > 0

    freq_map = {}
    for index in range(len(text) - substring_length + 1):
        substr = text[index : index + substring_length]
        if substr in freq_map:
            freq_map[substr] += 1
        else:
            freq_map[substr] = 1
    return freq_map
