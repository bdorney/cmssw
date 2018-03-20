import ROOT as r
from LVFAnalysis.LVFHistograms.PhysObjHistos import *
from LVFAnalysis.LVFUtilities.utilities import selLevels

class MuonHistos(PhysObjHistos):
    def __init__(self, pdgId=13, name=None, mcType=None):
        """
        pdgId - particle data group MC id for a particle (e.g. 13 for muon)
        name - Only used for complex objects (e.g. Jets) which don't have a pdgId
        mcType - string specifying Monte Carlo data tier, e.g. gen or reco
        """

        return
