# Making variables to calculate my grade percentages
# Anything with ___ hasn't been given yet
# Our grades are always rounded up, something which is not accounted for here (needs improvement)


ibes_case_study_critique=0.8*45
ibes_personal_ethics_statement=0.2*58
ibes_grade=ibes_case_study_critique+ibes_personal_ethics_statement

ita_exam=1*64
ita_grade=ita_exam

pmpd_individual_essay=0.7*45
pmpd_group_presentation=0.3*78
pmpd_grade=pmpd_individual_essay+pmpd_group_presentation

year1_sem1_grade=(ibes_grade+ita_grade+pmpd_grade)/3
# print(year1_sem1_grade)

be_midsem_exam=0.5*80
be_midterm_exam=0.5*40
be_grade=be_midsem_exam+be_midterm_exam

ff_exam=0.7*45
ff_group_work=0.3*66
ff_grade=ff_exam+ff_group_work

qaim_coursework=0.5*73
qaim_exam=0.5*56
qaim_grade=qaim_coursework+qaim_exam

year1_sem2_grade=(be_grade+ff_grade+qaim_grade)/3
# print(year1_sem2_grade)

first_year_grade=(year1_sem1_grade+year1_sem2_grade)/2
# print(first_year_grade)





bpse_reflection=0.6*75
bpse_group_report=0.4*65
bpse_grade=bpse_reflection+bpse_group_report

cf_exam=1*66
cf_grade=cf_exam

fr_exam=1*___
fr_grade=fr_exam

year2_sem1_grade=(bpse_grade+cf_grade+fr_grade)/3
# print(year2_sem1_grade)

ima_exam=1*___
ima_grade=ima_exam

sts_exam=0.7*___
sts_group_work=0.3*65
sts_grade=sts_exam+sts_group_work

fww_essay=1*___
fww_grade=fww_essay

year2_sem2_grade=(ima_grade+sts_grade+fww_grade)/3
# print(year2_sem2_grade)

second_year_grade=(year2_sem2_grade+year2_sem2_grade)/2
# print(second_year_grade)