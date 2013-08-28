################
# Instructions #
################

# 1. Copy PYTHIA6_B0dToKstMuMuKPi_7TeV_cff.py in Configuration/Generator/python/
# 2. If not in repository copy Bd_MuMuKstar_mumuKpi.dec in GeneratorInterface/ExternalDecays/data/
# 3. scram b
# 4. source GenMyMC.sh


### Create just GEN-MC ###
# Remove only the mumugenfilter from PYTHIA6_B0dToKstMuMuKPi_7TeV_cff.py
#cmsDriver.py Configuration/Generator/python/PYTHIA6_B0dToKstMuMuKPi_7TeV_cff.py -s GEN --conditions START53_V19F::All --datatier GEN-SIM --eventcontent RAWSIM -n 10000000000 --no_exec


### Create just GEN-SIM-MC for official production tests ###
cmsDriver.py Configuration/Generator/python/PYTHIA6_B0dToPsi2SKstMuMuKPi_7TeV_cff.py -s GEN,SIM --conditions START53_V19F::All --datatier GEN-SIM --eventcontent RAWSIM -n 100000 --no_exec


### Create MC up to HLT ###
#cmsDriver.py Configuration/Generator/python/PYTHIA6_B0dToKstMuMuKPi_7TeV_cff.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT --conditions START53_V19F::All --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 10000000000 --no_exec


### Create RECO-MC from MC up to HLT (output RECO + SIM) ###
#cmsDriver.py Configuration/Generator/python/PYTHIA6_B0dToKstMuMuKPi_7TeV_cff.py -s RAW2DIGI,RECO --conditions START53_V19F::All --datatier GEN-SIM-RECO --eventcontent RECOSIM --filein file:PYTHIA6_B0dToKstMuMuKPi_7TeV_cff_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root -n -1 --no_exec


### Create RECO-MC from MC up to HLT (output AOD + SIM) ###
#cmsDriver.py Configuration/Generator/python/PYTHIA6_B0dToKstMuMuKPi_7TeV_cff.py -s RAW2DIGI,RECO --conditions START53_V19F::All --datatier GEN-SIM-RECO --eventcontent AODSIM --filein file:PYTHIA6_B0dToKstMuMuKPi_7TeV_cff_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root -n -1 --no_exec
