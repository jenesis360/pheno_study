'''

Welcome to variables.py

Here we configure how the variables are 
binned and labelled in the ROOT plots
using a dictionary d_vars = {}

'''

#____________________________________________________________________________
def configure_vars():
  
   
  # ---------------------------------------------
  #
  # Format for each variable entry
  #
  # 'variable name as in TTree ntuple of SusySkimHiggsino' 
  #    : {
  #       'tlatex'  : ROOT TLaTeX axis entry to display in plot
  #       'units'   : Units of variable to print on plot
  #       'hXNbins' : Number of bins
  #       'hXmin',  : Lower x axis edge
  #       'hXmax'   : Upper x axis edge 
  #      }
  #
  # To do variable bin widths, place 'var' as value of 'hXNbins' 
  # and specify lower bin edges as 'binsLowE':[0,4,5,11,15,20,40,60]
  # e.g. 
  # 'lep2Pt':{'tlatex':'p_{T}(#font[12]{l}_{2})','units':'GeV','hXNbins':'var','hXmin':0,'hXmax':60,'binsLowE':[0,4,5,11,15,20,40,60]}
  #
  # ---------------------------------------------
  
  # ---------------------------------------------
  #
  # Contents
  # TODO Fill in as add variables
  # ---------------------------------------------

  d_vars = {
   
    # -------------------//------------------------
   
    # ---------------------------------------------
    # Higgs variables
    # ---------------------------------------------
    'm_hh' :{'tlatex':'m_hh','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':800},

    'm_h1' :{'tlatex':'m_h1','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':300},
    'm_h2' :{'tlatex':'m_h2','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':300},
    
    'pT_h1' :{'tlatex':'pT_h1','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},
    'pT_h2' :{'tlatex':'pT_h2','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},

    'eta_h1' :{'tlatex':'#eta_h1','units':'GeV','hXNbins':100,'hXmin':-5, 'hXmax':5},
    'eta_h2' :{'tlatex':'#eta_h2','units':'GeV','hXNbins':100,'hXmin':-5,  'hXmax':5},

    'phi_h1' :{'tlatex':'#phi_h1','units':'GeV','hXNbins':100,'hXmin':-5, 'hXmax':5},
    'phi_h2' :{'tlatex':'#phi_h2','units':'GeV','hXNbins':100,'hXmin':-5,  'hXmax':5},
  
    'pT_hh' :{'tlatex':'pT_hh','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},
    'dR_hh' :{'tlatex':'dR_hh','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':5},
    'deta_hh' :{'tlatex':'d#eta_hh','units':'GeV','hXNbins':100,'hXmin':-5, 'hXmax':5},
    'dphi_hh' :{'tlatex':'d#phi_hh','units':'GeV','hXNbins':100,'hXmin':-5, 'hXmax':5},

    'pT_h1_j1' :{'tlatex':'pT_h1_j1','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},
    'pT_h1_j2' :{'tlatex':'pT_h1_j2','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},
    'pT_h2_j1' :{'tlatex':'pT_h2_j1','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},
    'pT_h2_j2' :{'tlatex':'pT_h2_j2','units':'GeV','hXNbins':100,'hXmin':0, 'hXmax':2000},

    # -------------------//------------------------

  } # end of d_vars = {} dictionary

  return d_vars

