import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.option = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use, run_01
    fileNames = cms.untracked.vstring(
        'file:samples/hadronized_files/run_02/run_02_had_mphi_10_mchi_1.root'
    )
)

process.demo = cms.EDAnalyzer('DM_Analyzer',
                              genParticleTag = cms.untracked.InputTag('genParticles')
)

process.TFileService = cms.Service("TFileService", fileName = cms.string('samples/analyzed/run_02/SAVE_had_mphi_10_mchi_1.root') )


process.p = cms.Path(process.demo)
