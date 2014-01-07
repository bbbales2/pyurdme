""" ADFSP solver. """
#import pyurdme
from pyurdme import pyurdme

class ADFSPSolver(pyurdme.URDMESolver):
    """ ADFSP solver class. """
    NAME = 'adaptive_dfsp'

    def __init__(self, model, solver_path=None, report_level=0):
        if solver_path is None or solver_path == "":
            solver_path = '/Users/brian/Desktop/research/operator_splitting/urdme_solvers'
        print "constructor for the ADFSPSolver, solver_path={0}".format(solver_path)
        pyurdme.URDMESolver.__init__(self, model, solver_path=solver_path, report_level=report_level)
