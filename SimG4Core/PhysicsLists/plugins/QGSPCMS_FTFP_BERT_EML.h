#ifndef SimG4Core_PhysicsLists_QGSPCMS_FTFP_BERT_EML_H
#define SimG4Core_PhysicsLists_QGSPCMS_FTFP_BERT_EML_H
 
#include "SimG4Core/Physics/interface/PhysicsList.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
 
class QGSPCMS_FTFP_BERT_EML: public PhysicsList {

public:
  QGSPCMS_FTFP_BERT_EML(G4LogicalVolumeToDDLogicalPartMap& map, const HepPDT::ParticleDataTable * table_, sim::ChordFinderSetter *chordFinderSetter_, const edm::ParameterSet & p);
};

#endif


