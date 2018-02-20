import os

from LVFAnalysis.python.utils.elHistos import ElHistos
from LVFAnalysis.python.utils.muonHistos import MuonHistos
from LVFAnalysis.python.utils.PhysObjHistos import PhysObjHistos
from LVFAnalysis.python.utils.tauHistos import TauHistos
from LVFAnalysis.python.utils.utilities import selLevels, mcLevels

from LVFAnalysis.python.utils.physicsObjects.physicsObject import *

import ROOT as r

class lvfAnalyzer:
    def __init__(self, inputFileName, inputTreeName="IIHEAnalysis", isData=False):
        """
        inputFileName - physical filename of input TFile to perform analysis on
        inputTreeName - name of TTree found in inputFileName
        isData - True (False) if running over data (MC)
        """

        # Get Input TTree
        self.inputFileName = inputFileName #store this for later
        try:
            self.dataFile = r.TFile(inputFileName, "READ", "", 1)
            self.dataTree = self.dataFile.Get(inputTreeName)
        except Exception as e:
            print "exception occured when trying to retrive TTree %s from TFile %s"%(inputTreeName,inputFileName)
            print "exception: ", e
            exit(os.EX_DATAERR)

        self.isData = isData

        # Make Histograms
        self.elHistos = {}
        self.muHistos = {}
        self.tauHistos = {}
        self.ZprimeHistos = {}
        if isData:
            # Placeholder
            self.elHistos["data"] = ElHistos()
            self.muHistos["data"] = MuonHistos()
            self.tauHistos["data"] = TauHistos()
            self.ZprimeHistos["data"] = PhysObjHistos(pdgId=32)
        else:
            for lvl in mcLevels:
                self.elHistos[lvl] = ElHistos(mcType=lvl)
                self.muHistos[lvl] = MuonHistos(mcType=lvl)
                self.tauHistos[lvl] = TauHistos(mcType=lvl)
                self.ZprimeHistos[lvl] = PhysObjHistos(pdgId=32, mcType=lvl)

        return

    def analyze(self, printLvl=1000):
        """
        Analyzes data stored in self.dataTree and prints the 
        number of processed events every printLvl number of events
        """

        print "analyzing input file: %s"%(self.inputFileName)

        #Loop over input TTree
        analyzedEvts = 0
        for event in self.dataTree:
            analyzedEvts += 1
            if analyzedEvts % printLvl:
                print "Processed %i number of events"%analyzedEvts 

            # Loop over generated particles
            if not isData:
                for idx in range(0,event.mc_px.size()):
                    

            # Loop over muons
            # Loop over electrons
            # Loop over taus


        return

    def write(self, outputFileName, debug=False):
        """
        Writes TObjects to outputFileName.
        The output TFile is deleted each time
        """
        
        option="RECREATE"

        if debug:
            print "saving electron histograms"
        for histos in self.elHistos:
            # write histos
            histos.write(outputFileName, option)
            
            # after first iteration change the option from recreate to update
            if option == "RECREATE":
                option = "UPDATE"

        if debug:
            print "saving muon histograms"
        for histos in self.muHistos:
            histos.write(outputFileName, option)

        if debug:
            print "saving tau histograms"
        for histos in self.tauHistos:
            histos.write(outputFileName, option)

        return
