#
# V: 11-2017
# See documetation at https://docs.python.org/3/library/argparse.html
import argparse as ap
import logging
from makeDigikeyBOM import makeDigikeyBOM
NUM_PROCESSES = 30  # Maximum number of parallel web-scraping processes.

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
##################################################################
def openInputFile(inputFilename):
    # The logging article: http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python gave good advice on doing a traceback.
    try:
        return open(inputFilename)
    except (SystemExit,KeyboardInterrupt):
        raise
    except Exception:
        logging.error('failed to open file named %s',inputFilename,exc_info=True)
        exit
##################################################################
def getUserInput():
    parser = ap.ArgumentParser(
        description='Build BoM csv file for a KiCAD project.')
    # See https://docs.python.org/3/library/argparse.html#name-or-flags why -i or --input
    #
    # The full path and name to the bom2csv file must be given.
    #
    parser.add_argument('-xml', '--bom2csv',
                        # See https://docs.python.org/3/library/argparse.html#nargs
                        nargs='?',
                        type=str,
                        default=None,
                        # See https://docs.python.org/3/library/argparse.html#metavar
                        metavar='file.xml',
                        help='BOM XML file created from csv2bom Kicad plug-in.')
    parser.add_argument('-j','--jellybean',
                        nargs='?',
                        type=str,
                        default=None,
                        metavar='file.csv',
                        help='csv file containing the jellybean parts.')
    parser.add_argument('-d','--outdir',
                        nargs='?',
                        type=str,
                        default=None,
                        metavar='/<dir path>/...',
                        help='Directory path where the MadeDigikeyBOM.csv will be written.')
    parser.add_argument('-np', '--num_processes',
                        nargs='?',
                        type=int,
                        default=NUM_PROCESSES,
                        const=NUM_PROCESSES,
                        metavar='NUM_PROCESSES',
                        help='Set the number of parallel processes used for web scraping part data.')
    return parser.parse_args()
###############################################################################
# Main entrypoint.
###############################################################################
def main():
    #args = getUserInput()
    # Hard coding for now....
    #outputFrom_bom2csv = openInputFile(args.bom2csv)
    outputFrom_bom2csv = openInputFile('/Users/margaret/Documents/EnergyMonitoring/HappyDayNeighbors/HappyDay_Energy_PCB/HappyDay_Energy_PCB.xml')
    #jellyBeanFile = openInputFile(args.jellybean)
    jellyBeanFile = openInputFile('/Users/margaret/Documents/EnergyMonitoring/HappyDayNeighbors/HappyDay_Energy_PCB/BoM/JBParts.csv')
    #if args.outdir != None and os.path.exists(args.outdir):
    outdir = '/Users/margaret/Documents/EnergyMonitoring/HappyDayNeighbors/HappyDay_Energy_PCB/BoM'
    # if args.outdir != None and os.path.exists(args.outdir):
    #     makeDigikeyBOM(outputFrom_bom2csv,jellyBeanFile,args.outdir,args.num_processes)
    # else:
    #     logstr = 'The output directory path does not exist'
    #     logging.error(logstr,exc_info=True)
    #     exit
    makeDigikeyBOM(outputFrom_bom2csv,jellyBeanFile,outdir,NUM_PROCESSES)
if __name__ == '__main__':
    main()
