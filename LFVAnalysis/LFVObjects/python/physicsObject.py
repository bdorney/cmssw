import ROOT as r

class PhysObj:
    def __init__(self, px, py, pz, E, pdgId=-1):
        self.fourVector = r.TLorentzVector(px, py, pz, E)
        self.pdgId = pdgId
    
        return

    def px(self):
        return self.fourVector.px()
    
    def py(self):
        return self.fourVector.py()

    def pz(self):
        return self.fourVector.pz()

    def pt(self):
        return self.fourVector.pt()

    def M(self):
        return self.fourVector.M()
