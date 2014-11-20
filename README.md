atomChain
=========

Atomic chain supported by 2 electrodes

Download
========

$ git clone https://github.com/graguirre/atomChain.git


Examples
========

$ python2 chain.py -h
Options:
 -h Show help
 -e <element> Element (Supported: Pt, Au)
 -n <integer> chain length (default 0)
Syntax: python2 chain.py -e Pt -n 1


$ python2 chain.py
20

Pt	0.0	0.0	0.0
Pt	0.0	-1.962	-1.962
Pt	-1.962	0.0	-1.962
Pt	-1.962	-1.962	0.0
Pt	-1.962	-1.962	-3.924
Pt	-1.962	-3.924	-1.962
Pt	0.0	-3.924	-3.924
Pt	-3.924	-1.962	-1.962
Pt	-3.924	0.0	-3.924
Pt	-3.924	-3.924	0.0
Pt	1.405	1.405	1.405
Pt	1.405	3.367	3.367
Pt	3.367	1.405	3.367
Pt	3.367	3.367	1.405
Pt	3.367	3.367	5.329
Pt	3.367	5.329	3.367
Pt	1.405	5.329	5.329
Pt	5.329	3.367	3.367
Pt	5.329	1.405	5.329
Pt	5.329	5.329	1.405

