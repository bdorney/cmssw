import ROOT as r
from LVFAnalysis.LVFHistograms.kinematicHistos import *
from LVFAnalysis.LVFHistograms.isolationHistos import *
from LVFAnalysis.LVFUtilities.utilities import selLevels

class PhysObjHistos:
    def __init__(self, pdgId, name=None, mcType=None):
        """
        pdgId - particle data group MC id for a particle (e.g. 13 for muon)
        name - Only used for complex objects (e.g. Jets) which don't have a pdgId
        mcType - string specifying Monte Carlo data tier, e.g. gen or reco
        """
        
        # Determine particle name
        dict_pdgId = {
            11:"el",
            13:"mu",
            15:"tau",
            32:"Zprime"
                }

        self.physObjType = ""
        if name is not None:
            self.physObjType = physObj
        else:
            self.physObjType = dict_pdgId[pdgId]
        
        # Setup histograms
        self.dict_histosKin = {}
        self.dict_histosIso = {}

        #prefix = "h_data"
        #if mcType not None:
        #    prefix = "h_%s"%mcType
        
        for lvl in selLevels:
            self.histosKin[lvl] = kinematicHistos(self.physObj, lvl, mcType)
            self.histosIso[lvl] = isolationHistos(self.physObj, lvl, mcType)

        return

    def write(self, filename, option="RECREATE"):
        """
        Creates a TFile using TOption option
        Writes all stored histograms to this TFile
        """
        
        outFile = r.TFile(filename, option, "", 1)
        outDirPhysObj = outFile.mkdir(self.physObjType)
        
        for lvl in selLevels:
            dirSelLevel = outDirPhysObj.mkdir(lvl)
            
            dirKin = dirSelLevel.mkdir("Kinematics")
            self.histosKin[lvl].write(dirKin)

            dirIso = dirSelLevel.mkdir("Isolation")
            self.histosIso[lvl].write(dirIso)

        return
