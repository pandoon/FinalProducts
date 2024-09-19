#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


# In[29]:


Test = ['AAPL', 'MSFT', 'NVDA', 'AVGO', 'ORCL', 'ASML', 'ADBE', 'CRM', 'AMD', 'ACN', 'CSCO', 'TXN', 'TSM']
Industrials = ['GE', 'CAT', 'RTX', 'UNP', 'LMT', 'HON', 'ETN', 'UPS', 'BA', 'DE', 'WM', 'GD', 'TT', 'CTAS', 'CP', 'PH', 'TDG', 'NOC', 'ITW', 'CNI', 'MMM', 'FDX', 'CSX', 'CARR', 'RSG', 'EMR', 'NSC', 'CPRT', 'PCAR', 'URI', 'JCI', 'WCN', 'GWW', 'LHX', 'CMI', 'ODFL', 'PWR', 'AME', 'HWM', 'FAST', 'VRSK', 'EFX', 'OTIS', 'IR', 'HEI', 'XYL', 'VRT', 'ROK', 'HEI.A', 'WAB', 'GPN', 'VLTO', 'AXON', 'DAL', 'DOV', 'HUBB', 'LII', 'BAH', 'BLDR', 'CSL', 'J', 'AER', 'EME', 'WSO.B', 'WSO', 'JBHT', 'EXPD', 'MAS', 'LUV', 'ZTO', 'TXT', 'RBA', 'SWK', 'IEX', 'SNA', 'PNR', 'OC', 'NDSN', 'UAL', 'GGG', 'UHAL', 'UHAL.B', 'POOL', 'ACM', 'XPO', 'CLH', 'FTAI', 'CNH', 'TTEK', 'FIX', 'AOS', 'WMS', 'CHRW', 'CW', 'ALLE', 'BLD', 'ITT', 'NVT', 'RRX', 'HII', 'LECO', 'ULS', 'SAIA', 'WWD', 'FBIN', 'APG', 'ARMK', 'TTC', 'BWXT', 'GNRC', 'CNM', 'KBR', 'ESLT', 'CR', 'MTZ', 'DCI', 'RBC', 'FLR', 'KNX', 'MLI', 'WCC', 'ASR','FCN', 'ATI', 'AIT', 'LTM', 'AYI', 'AAON', 'MIDD', 'SPXC', 'DRS', 'WSC', 'CRS', 'MSA', 'OSK', 'AAL', 'KEX', 'TREX', 'LPX', 'DLB', 'AGCO', 'LOAR', 'ADT', 'WTS', 'FLS', 'LSTR', 'RHI', 'SITE', 'ESAB', 'MOG.A', 'MOG.B', 'R', 'CWST', 'AZEK', 'GXO', 'TKR', 'FSS', 'VMI', 'AVAV', 'BECN', 'MMS', 'ZWS', 'AWI', 'SRCL', 'EXPO', 'CSWI', 'MDU', 'HXL', 'AL', 'GTLS', 'DY', 'TNET', 'GATX', 'BCO', 'SNDR', 'FELE', 'MATX', 'MSM', 'GTES', 'ALK', 'VRRM', 'ACA', 'HRI', 'HAFN', 'SPR', 'ENS', 'AEIS', 'RXO', 'KFY', 'TEX', 'KAI', 'IESC', 'CBZ', 'STRL', 'ABM', 'JOBY', 'UNF', 'NSP', 'BRC', 'MAN', 'ROAD', 'KTOS', 'GMS', 'NPO', 'CXT', 'ATKR', 'MWA', 'GVA', 'GFF', 'HAYW', 'RKLB', 'SKYW', 'ICFI', 'PRIM', 'SEB', 'ATMU', 'REZI', 'HUBG', 'CAR', 'JBT', 'FA', 'TRN', 'BE', 'MGRC', 'ENOV', 'SBLK', 'HNI', 'ARCB', 'AZZ', 'CMPR', 'GOGL', 'CAAP', 'ENR', 'AIR', 'HI', 'WOR', 'WERN', 'MRCY', 'MIR', 'EPAC', 'ALG', 'ASPN', 'ROCK', 'SXI','BWLP', 'B', 'KMT', 'POWL', 'SYM', 'PRG', 'HLMN', 'GEO', 'VSTS', 'TNC', 'HURN', 'VVX', 'JBLU', 'DSGR', 'HEES', 'VSEC', 'NSSC', 'CMRE', 'ENVX', 'CODI', 'MYRG', 'PLUG', 'REVG', 'NMM', 'SCS', 'JBI', 'AMRC', 'SFL', 'DAC', 'NVEE', 'CXW', 'BV', 'GBX', 'CDRE', 'HLIO', 'APOG', 'MRTN', 'DNOW', 'LNN', 'GIC', 'PBI', 'TPC', 'UP', 'KFRC', 'ACHR', 'JELD', 'LZ', 'ARLO', 'CRAI', 'TRNS', 'MEG', 'ULH', 'ATSG', 'HY', 'TILE', 'TGI', 'THR', 'AGX', 'FIP', 'CCEC', 'GRC', 'CECO', 'PCT']
Tech = ['AAPL', 'MSFT', 'NVDA', 'AVGO', 'ORCL', 'ASML', 'ADBE', 'CRM', 'AMD', 'ACN', 'CSCO', 'TXN', 'QCOM', 'IBM', 'INTU', 'NOW', 'AMAT', 'UBER', 'ARM', 'SONY', 'PANW', 'ADI', 'ADP', 'ANET', 'KLAC', 'MU', 'LRCX', 'FI', 'SHOP', 'INTC', 'DELL', 'APH', 'SNPS', 'MSI', 'CDNS', 'PLTR', 'WDAY', 'CRWD', 'MRVL', 'NXPI', 'ROP', 'FTNT', 'ADSK', 'TTD', 'PAYX', 'TEL', 'MPWR', 'FIS', 'MCHP', 'TEAM', 'FICO', 'SQ', 'DDOG', 'CTSH', 'SNOW', 'IT', 'GLW', 'GRMN', 'HPQ', 'ON', 'APP', 'ZS', 'CDW', 'STM', 'ANSS', 'NET', 'KEYS', 'FTV', 'MSTR', 'SMCI', 'HUBS', 'HPE', 'TYL', 'BR', 'NTAP', 'FSLR', 'GDDY', 'IOT', 'WDC', 'TER', 'CPAY', 'CHKP', 'PTC', 'MDB', 'LDOS', 'ZM', 'STX', 'TDY', 'SSNC', 'VRSN', 'ZBRA', 'SWKS', 'ENTG', 'PSTG', 'ENPH', 'BSY', 'GEN', 'MANH', 'NTNX', 'AKAM', 'DT', 'AZPN', 'TOST', 'TRMB', 'LOGI', 'AFRM', 'OKTA', 'MNDY', 'FLEX', 'JNPR', 'GRAB', 'JKHY', 'JBL', 'CYBR', 'GWRE', 'DOCU', 'COHR','FFIV', 'UI', 'EPAM', 'QRVO', 'CACI', 'NICE', 'ONTO', 'SNX', 'PSN', 'TWLO', 'FFIV', 'UI', 'EPAM', 'QRVO', 'CACI', 'NICE', 'ONTO', 'SNX', 'PSN', 'TWLO', 'DOX', 'WIX', 'DUOL', 'OLED', 'PAYC', 'DAY', 'PCTY', 'FN', 'PCOR', 'DSGX', 'OTEX', 'APPF', 'KVYO', 'CIEN', 'DBX', 'AMKR', 'AUR', 'MKSI', 'MTSI', 'WEX', 'ESTC', 'CRUS', 'ALTR', 'YMM', 'INFA', 'GTLB', 'SPSC', 'S', 'PATH', 'ARW', 'NSIT', 'G', 'CGNX', 'HCP', 'CFLT', 'CVLT', 'SMAR', 'LFUS', 'ALAB', 'CCCS', 'SAIC', 'NOVT', 'LSCC', 'U', 'NVMI', 'VRNS', 'SQSP', 'RBRK', 'BMI', 'PEGA', 'VERX', 'EXLS', 'NXT', 'BILL', 'ST', 'ZETA', 'CRDO', 'QXO', 'FOUR', 'KD', 'CWAN', 'VNT', 'ALGM', 'ACIW', 'SATS', 'CLVT', 'TENB', 'CNXC', 'TSEM', 'AVT', 'OS', 'EEFT', 'RMBS', 'LYFT', 'PI', 'BOX', 'QLYS', 'ITRI', 'RUN', 'ASTS', 'BRZE', 'QTWO', 'BDC', 'WK', 'ASGN', 'BLKB', 'LPL', 'CAMT', 'ALIT', 'LITE', 'SLAB', 'POWI', 'SANM', 'PWSC', 'FORM', 'DXC', 'ZI', 'ACLS', 'CLBT', 'FRSH', 'PLXS', 'IDCC', 'ENV', 'NCNO', 'INTA', 'DOCN','INST', 'DV', 'SITM', 'GDS', 'GBTG', 'ALKT', 'SMTC', 'DIOD', 'SYNA', 'ASAN', 'AGYS', 'ESE', 'BL', 'FROG', 'RNG', 'IPGP', 'AI', 'ALRM', 'LIF', 'PAYO', 'YOU', 'PAY', 'VSH', 'TDC', 'MQ', 'CORZ', 'RELY', 'PRFT', 'WNS', 'PLUS', 'PYCR', 'PRGS', 'OSIS', 'CALX', 'AMBA', 'FIVN', 'KLIC', 'NABL', 'CXM', 'RPD', 'JAMF', 'APPN', 'FLYW', 'VZIO', 'EVTC', 'SWI', 'AVPT', 'SIMO', 'GRND', 'ODD', 'NATL', 'EXTR', 'SPNS', 'VECO', 'SEMR', 'VSAT', 'ROG', 'TTMI', 'EVCM', 'VYX', 'PAR', 'VRNT', 'DFIN', 'CNXN', 'VIAV', 'PD', 'UPBD', 'SPT', 'SOUN', 'IBTA', 'VICR', 'MLNK', 'RAMP', 'UCTT', 'DBD', 'HLIT', 'AVDX', 'PLAB', 'KN', 'RUM', 'IONQ', 'STER', 'BHE', 'NTCT', 'CTS', 'INFN', 'SONO', 'MTTR', 'XRX', 'TWKS', 'BB', 'NOVA', 'SEDG', 'ETWO', 'ADEA', 'CSGS', 'PSFE', 'ZUO', 'WKME', 'MXL', 'COHU', 'CRCT', 'WOLF', 'SCSC', 'PDFS', 'AOSL', 'FORTY', 'TASK', 'SABR', 'ACMR', 'SGH', 'AMPL', 'PGY', 'BELFA', 'DGII', 'GDYN', 'ICHR', 'HIMX', 'ARRY', 'JKS', 'ATEN','GPK', 'HRB', 'CROX', 'WYNN', 'VFS', 'GAP', 'NIO', 'ALV', 'BFAM', 'CZR', 'ALSN', 'LAD', 'BERY', 'NCLH', 'BWA', 'LEVI', 'XPEV', 'ANF', 'GNTX', 'MTH', 'VFC', 'AN', 'TMHC', 'PLNT', 'MTN', 'BBWI', 'VIPS', 'REYN', 'LEA', 'MAT', 'MOD', 'ETSY', 'KBH', 'IBP', 'WH', 'CHH', 'GLBE', 'THO', 'SLGN', 'SON', 'PVH', 'BYD', 'WHR', 'DDS', 'VVV', 'SKY', 'W', 'BC', 'SEE', 'MNSO', 'GPI', 'HOG', 'ABG', 'LTH', 'COLM', 'PII', 'RH', 'IGT', 'FUN', 'MHO', 'M', 'CPRI', 'KTB', 'TPH', 'RUSHA', 'FIVE', 'GOLF', 'BOOT', 'RUSHB', 'ASO', 'SHAK', 'AEO', 'HGV', 'SIG', 'LOT', 'FTDR', 'JWN', 'SG', 'BROS', 'GRBK', 'DORM', 'RRR', 'WEN', 'YETI', 'CVCO', 'URBN', 'UAA', 'UA', 'SHOO', 'EAT', 'CCS', 'DFH', 'ACVA', 'TNL', 'GEF.B', 'LCII','CARG', 'GEF', 'FL', 'AIN', 'QS', 'PATK', 'PRKS', 'VC', 'PENN', 'AAP', 'ATAT', 'VAC', 'LGIH', 'GT', 'CRI', 'DRVN', 'VSTO', 'HBI', 'MLCO', 'KSS', 'SAH', 'PTVE', 'MCW', 'PHIN', 'BKE', 'MLKN', 'MBC', 'MSGE', 'TRIP', 'CAKE', 'ADNT', 'OI', 'KAR', 'ARCO', 'MODG', 'VSCO', 'GTX', 'PTON', 'ARHS', 'WGO', 'LZB', 'LEG', 'FOXF', 'OSW', 'BLBD', 'BOWL', 'DAN', 'RVLV', 'THRM', 'PZZA', 'BLMN', 'CAL', 'SVV', 'MCRI', 'AMWD', 'OLPX', 'OXM', 'SBH', 'LVWR', 'HOV', 'WINA', 'CNNE', 'SHCO', 'XPEL', 'GIII', 'CARS', 'EVRI', 'GES', 'MSC', 'SCVL', 'WWW', 'FIGS', 'TRS', 'ODP', 'PLYA']
Consumer_Discretionary =['AMZN', 'TSLA', 'HD', 'TM', 'MCD', 'BABA', 'LOW', 'PDD', 'TJX', 'BKNG', 'NKE', 'SBUX', 'MELI', 'CMG', 'ABNB', 'MAR', 'ORLY', 'DHI', 'GM', 'AZO', 'HLT', 'HMC', 'ROST', 'LEN', 'SE', 'F', 'RCL', 'CPNG', 'JD', 'YUM', 'FLUT', 'LULU', 'TCOM', 'EBAY', 'TSCO', 'LVS', 'NVR', 'PHM', 'SW', 'DECK', 'ROL', 'QSR', 'BBY', 'CCL', 'LI', 'GPC', 'BALL', 'DKS', 'APTV', 'DRI', 'PKG', 'CVNA', 'EXPE', 'AVY', 'WSM', 'BURL', 'IP', 'DKNG', 'ULTA', 'AMCR', 'H', 'TOL', 'DPZ', 'VIK', 'RIVN', 'CASY', 'SN', 'KMX', 'CAVA', 'YUMC', 'MGA', 'FND', 'CHWY', 'MBLY', 'MGM', 'PAG', 'WING', 'SCI', 'TXRH', 'LKQ', 'CCK', 'MUSA', 'RL', 'SKX', 'CHDN', 'GME', 'MHK', 'LNW', 'HTHT', 'HAS', 'TPR', 'LCID', 'CART', 'TPX']
Communication_Services = ['GOOGL', 'META', 'NFLX', 'TMUS', 'VZ', 'DIS', 'CMCSA', 'T', 'DASH', 'NTES', 'CHTR', 'EA', 'BIDU', 'RBLX', 'TTWO', 'LYV', 'PINS', 'OMC', 'WBD', 'FOXA', 'FWONK', 'FWONA', 'NWSA', 'SNAP', 'WMG', 'Z', 'SIRI', 'IPG', 'RDDT', 'ROKU', 'MTCH', 'TKO', 'NYT', 'LBRDK', 'EDR', 'LSXMK', 'LSXMB', 'LSXMA', 'FYBR', 'LBTYK', 'PARA', 'BILI', 'NXST', 'BZ', 'LUMN', 'MSGS', 'USM', 'IAC', 'TEO', 'DJT', 'LLYVK', 'LLYVA', 'CCOI', 'CNK', 'IRDM', 'ATHM', 'PLTK', 'BATRA', 'TDS', 'BATRK', 'CRTO', 'WLY', 'GSAT', 'YELP', 'TGNA', 'ZD', 'IQ', 'CABO', 'YY', 'MGNI', 'IAS', 'LGF.A', 'LILAK', 'WB', 'AMC', 'WBTN', 'SPHR', 'GENI','GETY', 'ANGI', 'UPWK', 'SSTK', 'ADV', 'PLAY', 'MOMO', 'ATUS', 'TBLA', 'EEX', 'IMAX', 'QNST', 'NRDS', 'GOGO']
Financials = ['BRK.B', 'JRYPM', 'V', 'MA', 'BAC', 'WFC', 'AXP', 'GS', 'MS', 'SPGI', 'HDB', 'PGR', 'BLK', 'MUFG', 'C', 'SCHW', 'CB', 'MMC', 'KKR', 'BX', 'IBN', 'ICE', 'MCO', 'CME', 'AON', 'PYPL', 'USB', 'PNC', 'APO', 'AJG', 'AFL', 'TFC', 'ITUB', 'ING', 'COF', 'MET', 'MFG', 'TRV', 'BK', 'ALL', 'AIG', 'MSCI', 'COIN', 'AMP', 'PRU', 'ACGL', 'NDAQ', 'DFS', 'HIG', 'BRO', 'WTW', 'FCNCA', 'ARES', 'FCNCO', 'IX', 'FITB', 'MTB', 'BBD', 'ERIE', 'STT', 'TW', 'KB', 'RJF', 'TROW', 'WRB', 'HBAN', 'CBOE', 'RF', 'CINF', 'SHG', 'MKL', 'SYF', 'CFG', 'PFG', 'TRU', 'NTRS', 'L', 'HOOD', 'CRBG', 'NMR', 'BAM', 'EG', 'LPLA', 'FNF', 'FDS', 'KEY', 'RGA', 'CG', 'CNA', 'IBKR', 'EQH', 'MORN', 'RNR', 'ARCC', 'ALLY', 'BCH', 'JEF', 'EWBC', 'KNSL', 'AFG', 'HLI', 'BEN', 'UNM', 'AIZ', 'OWL', 'BSAC', 'GL', 'EVR', 'MKTX', 'ORI', 'WF', 'SF', 'WAL', 'PRI', 'FHN', 'SEIC', 'FUTU', 'BNRE', 'BNRE.A', 'SOFI', 'CBSH', 'WBS', 'RYAN', 'IVZ', 'PNFP', 'CMA', 'BPOP', 'SSB', 'ZION', 'WTFC', 'CFR', 'RLI', 'PB', 'VOYA', 'ESNT', 'JXN', 'BOKF', 'AXS', 'SNV', 'MTG', 'FAF', 'ONB', 'HLNE', 'COOP', 'JHG', 'OMF', 'OBDC', 'CADE', 'FG', 'FSK', 'CACC', 'HOMB', 'ACT', 'SIGI', 'PFSI', 'CRVL', 'FRHC', 'LNC', 'RDN', 'FNB', 'FCFS', 'GBCI', 'DNB', 'THG', 'COLB', 'UBSI', 'FFIN', 'TPG', 'AMG', 'UMBF', 'OZK', 'MARA', 'BGC', 'SLM', 'ESGR', 'MC', 'WTM', 'HWC', 'LAZ', 'CNS', 'SFBS', 'VLY', 'PIPR', 'MAIN', 'ABCB', 'AGO', 'NNI', 'WU', 'QFIN', 'NYCB', 'KMPR', 'AX', 'AB', 'GBDC', 'IBOC', 'UPST', 'TFSL', 'STEP', 'CNO', 'MCY', 'UCB', 'WD', 'AUB', 'VCTR', 'FULT', 'BANF', 'FBP', 'EBC', 'ASB', 'NMIH', 'FIBK', 'WSFS', 'CBU', 'CATY', 'BWIN', 'FHB', 'TCBI', 'HTGC', 'GNW', 'WAFD', 'PJT', 'APAM', 'BFH', 'BKU', 'BUR', 'PRK', 'BHF', 'RKT', 'FHI', 'INDB', 'SFNC', 'VIRT', 'CLSK', 'BOH', 'SNEX', 'AMK', 'PLMR', 'CVBF', 'TBBK', 'TOWN', 'SPNT', 'FFBC', 'PFS', 'PPBI', 'IBTX', 'BANC', 'HTLF', 'SBCF', 'NBTB', 'RIOT', 'FRME', 'ENVA', 'FBK', 'PSEC', 'RNST', 'AGM', 'FIHL', 'OFG', 'HTH', 'AGM.A', 'MBIN', 'BANR', 'STC', 'GSHD', 'TRMK', 'HG', 'LION', 'EFSC', 'TSLX', 'TFIN', 'LOB', 'TRUP', 'WSBC', 'RZLV', 'CLBK', 'NAVI', 'MRX', 'SYBT', 'OBDE', 'NWBI', 'FCF', 'FBNC', 'CHCO', 'LKFN', 'NTB', 'CASH', 'WULF', 'NBHC', 'GSBD', 'STBA', 'CUBI', 'SKWD', 'HOPE', 'BUSE', 'SRCE', 'TCBK', 'VRTS', 'WT', 'NIC', 'STEL', 'HMN', 'SASR', 'OCSL', 'WABC', 'FINV', 'VBTX', 'LC', 'NMFC', 'LMND', 'SAFT', 'MFIC', 'QCRH', 'CET', 'RBCAA', 'BY', 'EIG', 'GABC', 'CSWC', 'ECPG', 'FSUN', 'BHLB', 'CIFR', 'BLX', 'PX', 'PEBO', 'PFBC', 'BCSF', 'HGTY', 'FBMS', 'BBDC', 'OBK', 'OCFC', 'SBSI', 'PWP', 'DCOM', 'BOW', 'AMAL', 'HCI']


# In[36]:


def save_financial_statements_to_excel(tickers, filename='financial_data_with_statements.xlsx'):
    """
    This function retrieves the income statement, cash flow statement, and balance sheet for each
    ticker in the provided list, and saves them in a single Excel file with multiple sheets.
    
    Parameters:
    tickers (list): A list of stock ticker symbols.
    filename (str): The name of the Excel file to save the data to (default: 'financial_data_with_statements.xlsx').
    """
    
    # API setup
    base_url = 'https://financialmodelingprep.com/api/v3/'
    api_key = 'ksnxCfuMd8YcYtNVDrqZKBY0aZeDMLX8'
    
    # Statement types to fetch
    statements = ['income-statement', 'cash-flow-statement', 'balance-sheet-statement']
    
    # Create an Excel writer object to save multiple sheets
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        # Loop through each ticker in the provided list
        for ticker in tickers:
            # Initialize an empty DataFrame to store all statements
            all_statements = pd.DataFrame()

            for statement in statements:
                # Construct the API URL for the current statement and ticker
                url = f'{base_url}{statement}/{ticker}?period=quarter&apikey={api_key}'
                
                # Send a GET request to the API
                response = requests.get(url)
                
                # Convert the response to JSON
                data = response.json()
                
                # Convert the JSON data to a pandas DataFrame and transpose it
                df = pd.DataFrame(data).T
                
                # Add a title row to distinguish each financial statement
                title_row = pd.DataFrame([[statement.upper()]], columns=[ticker])
                all_statements = pd.concat([all_statements, title_row])  # Add the title row
                
                # Append the statement data to the combined DataFrame
                all_statements = pd.concat([all_statements, df])
                
                # Add an empty row after each statement for separation
                empty_row = pd.DataFrame([[''] * len(df.columns)], columns=df.columns)
                all_statements = pd.concat([all_statements, empty_row])

            # Write the combined DataFrame (income, cash flow, balance sheet) to a sheet named after the ticker
            # Set index=True to ensure that index labels (such as dates) are written in Column A
            all_statements.to_excel(writer, sheet_name=ticker, index=True)
    
    print(f"Financial data saved to {filename}")


# In[ ]:


tickers_list = Test
save_financial_statements_to_excel(tickers_list)

