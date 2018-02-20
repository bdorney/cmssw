import ROOT as r

class kinematicHistos:
    def __init__(self, physObj="mu", selLevel="all", mcType=None):
        """
        physObj - string specifying physics object type
        selLevel - string specifying the selection type
        mcType - string specifying Monte Carlo data tier, e.g. gen or reco
        """
        
        prefix = "h_data"
        if mcType not None:
            prefix = "h_%s"%mcType

        self.eta = r.TH1F("%s_%s_eta_%s"%(prefix,physObj,selLevel),"%s eta - %s"%(physObj, selLevel), 50,-2.45,2.45)
        self.mass = r.TH1F("%s_%s_mass_%s"%(prefix,physObj,selLevel),"%s mass - %s"%(physObj, selLevel), 200,-0.5,2000.5)
        self.multi = r.TH1F("%s_%s_multi_%s"%(prefix,physObj,selLevel),"%s multiplicity - %s"%(physObj, selLevel), 30,-0.5,30.5)
        self.pt = r.TH1F("%s_%s_pt_%s"%(prefix,physObj,selLevel),"%s pt - %s"%(physObj, selLevel), 200,-0.5,2000.5)

        return

    def write(self, directory):
        """
        directory - TDirectory histograms should be written too
        """

        directory.cd()

        self.eta.Write()
        self.mass.Write()
        self.multi.Write()
        self.pt.Write()

        return
