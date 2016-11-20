maxAlma=0
counta=0
for i in range(1,5):
	prospatheia=1
	bestEpidosh=0
	while (prospatheia<=3) and (bestEpidosh<=4.5):
		print 'Prospatheia ', prospatheia
		epidosh=input('Dwse alma:')
		if epidosh>bestEpidosh:
			bestEpidosh=epidosh
			if epidosh>4.5:
				print 'Prokrithike'
				counta=counta+1
		prospatheia=prospatheia+1
		
	if bestEpidosh < 4.5:
		print 'Den prokrithike! To kalytero toy alma htan:',bestEpidosh
		
	if maxAlma<bestEpidosh:
		maxAlma=bestEpidosh

print 'Prokrithikan ', counta, 'athlites'
print 'Kalyterh epidosh pou shmeiwthike htan:', maxAlma