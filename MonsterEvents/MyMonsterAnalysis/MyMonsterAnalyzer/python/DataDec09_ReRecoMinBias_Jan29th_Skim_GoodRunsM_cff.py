import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_1.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_10.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_11.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_12.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_13.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_14.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_15.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_16.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_17.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_18.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_19.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_2.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_20.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_21.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_22.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_23.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_24.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_25.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_26.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_27.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_28.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_29.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_3.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_30.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_31.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_32.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_33.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_34.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_35.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_36.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_37.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_38.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_39.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_4.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_40.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_41.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_42.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_43.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_44.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_45.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_46.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_47.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_48.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_49.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_5.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_50.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_51.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_52.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_53.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_54.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_55.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_56.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_57.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_58.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_59.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_6.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_60.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_61.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_62.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_63.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_64.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_65.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_66.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_67.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_68.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_69.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_7.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_70.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_71.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_72.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_73.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_74.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_75.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_76.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_77.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_78.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_79.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_8.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_80.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_81.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_82.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_83.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_84.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_85.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_86.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_87.root",
"rfio:/castor/cern.ch/user/d/dinardo/MyMonsterAnalysisGoodRuns_Jan29th/MyMonsterAnalysisSkim_9.root" ] );

secFiles.extend( [
               ] )