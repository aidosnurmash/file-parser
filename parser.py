import csv
import logging

SKIP_LINE = 42
COL_NAMES = ('DEPT', 'ROP', 'WOB', 'RPM', 'GAM')

logger = logging.getLogger("info_logger")
logging.basicConfig(filename='logs/info.log', filemode='a+',
                    format='[%(asctime)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s')


"""
:param filename: file with data (.las)
:param separator: symbol which data are separated in file
:returns: dictionary where keys are COL_NAMES, values are data in this column 
"""


def import_text(filename, separator):

    cols = {}
    data = {}

    with open(filename) as file:

        for i in range(SKIP_LINE):
            next(file)

        first_line = True
        line_cnt = 0

        for line in csv.reader(file, delimiter=separator,
                               skipinitialspace=True):

            line_cnt += 1

            if line:
                if first_line:
                    first_line = False

                    del line[0]

                    # get column number
                    for idx, col in enumerate(line):
                        if col in COL_NAMES:
                            cols[col] = idx

                    # check all columns are exist
                    for col in COL_NAMES:
                        data[col] = []
                        if not (col in cols):
                            logger.error('check input, not all columns exist(' + col + ')')
                            return

                else:
                    for col in COL_NAMES:
                        pos = cols[col]

                        if pos >= len(line):
                            logger.error('in line ' + str(line_cnt) + ' not exist data for column ' + col)

                        data[col].append(float(line[pos]))

    return data


data = import_text('data.las', ' ')
print(data)
