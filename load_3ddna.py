import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors.kde import KernelDensity
from tqdm import tqdm as tqdm
import pysam
import argparse

def parse_3ddna(assembly_filename, sam_filename):
    sam = pysam.AlignmentFile(sam_filename, 'r')
    name_map = {}
    order = []
    orientation = []
    with open(assembly_filename) as f:
        for l in f:
            if l[0] == '>':
                record = l[1:].rstrip('\n').split(' ')
                name_map[record[1]] = sam.get_tid(record[0])
            else:
                ls = l.rstrip('\n').split(' ')
                for contig in ls:
                    if contig[0] == '-':
                        order.append(name_map[contig[1:]])
                        orientation.append(1)
                    else:
                        order.append(name_map[contig])
                        orientation.append(0)
    
    print('finish', len(order), len(orientation))
    return order, orientation

if __name__ == '__main__':
    print('hoge')
    parse_3ddna('../analysis/3D_DNA/mock_chrI/mock_chrI.0.assembly', '../analysis/mock/r1_70x_mock_chrI.sam')