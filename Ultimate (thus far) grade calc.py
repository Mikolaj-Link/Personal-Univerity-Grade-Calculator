# The ultimate grade calc (as of 12/06/26) (ts is acc beautiful considering its my day 3 of python)
# Would it be possible to have the 'print("year1, ...")' inside the function?
# I can't calculate 'y2s1_grade' (for example) without having all other values present, is there a way to avoid this?

def y1_grade(ibes_csc, ibes_es, ita_exam, pmpd_essay, pmpd_pres, be_mse, be_mte, ff_exam, ff_gw, qaim_cw, qaim_exam):
    y1s1_grade=round((((ibes_csc*0.8)+(ibes_es*0.2))+ita_exam+((pmpd_essay*0.7)+(pmpd_pres*0.3)))/3)
    y1s2_grade=round((((be_mse*0.5)+(be_mte*0.5))+((ff_exam*0.7)+(ff_gw*0.3))+((qaim_cw*0.5)+(qaim_exam*0.5)))/3)
    yr1_grade=round((y1s1_grade+y1s2_grade)/2)
    return y1s1_grade, y1s2_grade, yr1_grade

y1s1_grade, y1s2_grade, yr1_grade=y1_grade(45,58,64,45,78,80,40,45,66,73,56)

print("Year 1, semester 1 grade:",y1s1_grade)
print("Year 1, semester 2 grade:",y1s2_grade)
print("Overall year 1 grade:",yr1_grade)


def y2_grade(bpse_ref, bpse_gr, cf_exam, fr_exam, ima_exam, sts_exam, sts_gw, fww_essay):
    y2s1_grade=round((((bpse_ref*0.6)+(bpse_gr*0.4))+cf_exam+fr_exam)/3)
    y2s2_grade=round((ima_exam+((sts_exam*0.7)+(sts_gw*0.3))+fww_essay)/3)
    yr2_grade=round((y2s1_grade+y2s2_grade)/2)
    return y2s1_grade, y2s2_grade, yr2_grade

y2s1_grade, y2s2_grade, yr2_grade=y2_grade(75,65,66,_,_,_,65,_)

print("Year 2, semester 1 grade:",y2s1_grade)
print("Year 2, semester 2 grade:",y2s2_grade)
print("Overall year 2 grade:",yr2_grade)