# Previosuly, I used variables to build a model that calculates my university grades,
# my aim is to now make this more efficient using functions
# Again, '__' is for currently unavailable values

def year1_sem1_grade(ibes_csc, ibes_pes, ita_exam, pmpd_essay, pmpd_pres):
    ibes_grade=(ibes_csc*0.8)+(ibes_pes*0.2)
    ita_grade=ita_exam
    pmpd_grade=(pmpd_essay*0.7)+(pmpd_pres*0.3)
    y1s1_grade=(ibes_grade+ita_grade+pmpd_grade)/3
    return y1s1_grade

get_y1s1_grade=year1_sem1_grade(45,58,64,45,78)
print(get_y1s1_grade)

def year1_sem2_grade(be_mse, be_mte, ff_exam, ff_gw, qaim_cw, qaim_exam):
    be_grade=(be_mse*0.5)+(be_mte*0.5)
    ff_grade=(ff_exam*0.7)+(ff_gw*0.3)
    qaim_grade=(qaim_cw*0.5)+(qaim_exam*0.5)
    y1s2_grade=(be_grade+ff_grade+qaim_grade)/3
    return y1s2_grade

get_y1s2_grade=year1_sem2_grade(80,40,45,66,73,56)
print(get_y1s2_grade)

def year2_sem1_grade(bpse_ref, bpse_gr, cf_exam, fr_exam):
    bpse_grade=(bpse_ref*0.6)+(bpse_gr*0.4)
    cf_grade=cf_exam
    fr_grade=fr_exam
    y2s1_grade=(bpse_grade+cf_grade+fr_grade)/3
    return y2s1_grade

get_y2s1_grade=year2_sem1_grade(75,65,66,__)
print(get_y2s1_grade)

def year2_sem2_grade(ima_exam, sts_exam, sts_gw, fww_essay):
    ima_grade=ima_exam
    sts_grade=(sts_exam*0.7)+(sts_gw*0.3)
    fww_grade=(fww_essay)
    y2s2_grade=(ima_grade+sts_grade+fww_grade)/3
    return y2s2_grade

get_y2s2_grade=year2_sem2_grade(__,__,65,__)
print(get_y2s2_grade)



year1_grade=(get_y1s1_grade+get_y1s2_grade)/2
print(year1_grade)

year2_grade=(get_y2s1_grade+get_y2s2_grade)/2
print(year2_grade)

