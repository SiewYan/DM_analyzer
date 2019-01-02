import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.option = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:ptllmin_100/Hadronized_roots/Hadronized_phim_500_mchi_1_ptllmin_100.root'
    )
)

process.demo = cms.EDAnalyzer('DM_Analyzer',
                              genParticleTag = cms.untracked.InputTag('genParticles')
)

process.TFileService = cms.Service("TFileService", fileName = cms.string('ptllmin_100/PY_roots/PY_mphim_500_mchi_1_ptllmin_100.root') )


process.p = cms.Path(process.demo)
