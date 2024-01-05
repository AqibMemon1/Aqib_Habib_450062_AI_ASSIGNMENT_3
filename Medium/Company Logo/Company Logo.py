#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

s = input()
s = sorted(s)

Occurence= Counter(list(s))
for k, v in Occurence.most_common(3):
    print(k, v)