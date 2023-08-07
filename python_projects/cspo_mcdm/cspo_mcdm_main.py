# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:34:31 2023

@author: abhishek.jee
"""

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import minmax_scale
#from scikit-criteria import data, MIN, MAX
from skcriteria import DecisionMatrix
from skcriteria.preprocessing.scalers import MaxScaler, MinMaxScaler

# ---Assigning column names for all fields

colnames = [
    'id',
	'start_time',
	'end_time',
	'email',
	'name',
	'cst_number',
	'capx_opex_flg',
	'otl_cd',
	'vendor_name',
	'deliv_prtnr_name',
	'sol_name',
	'cust_code_req_flg',
	'hld_upld_doc',
	'poc_doc',
	'sow_doc',
	'use_case_doc',
	'escal_path_def_flg',
	'new_exist_pf_flg',
	'sol_phy_loc',
	'expec_txn_rt',
	'expec_user_cnt',
	'data_classif',
	'expec_crtclty',
	'expec_sla_hpi',
	'expec_sla_user_req',
	'maintt_wndw_intrsv_chg_curr',
	'non_intrsv_bus_hrs_flg',
	'expec_freq_sw_rel_sol',
	'sol_intrfc_data_acc_intrnt_flg',
	'npe_deplyd_cnt',
	'reqd_sol_mult_slct',
	'soln_audit_flg',
	'sol_user_admin_reqd_flg',
	'pii_flg',
	'spec_supp_consid_xtra',
	'app_name',
	'cmdb_app_id',
	'sol_chg_desc',
	'expec_crtclty_2',
	'expec_sla_hpi_2',
	'expec_sla_user_req_2',
	'maintt_wndw_intrsv_chg_fut',
	'non_intrsv_bus_hrs_flg_2',
	'expec_freq_sw_rel_sol_2',
	'expec_txn_vol',
	'expec_usr_node_nbr',
	'new_data_classif',
	'sol_pii_hosting_flg',
	'run_book_current_flg',
	'spec_supp_consid',
	'osi_doc_current_flg'
    ]
response_data = pd.read_excel("cspo_support_intake_form.xlsx",names=colnames)
print(response_data)

response_data = response_data.loc[:,[]].head(10)
print(response_data)