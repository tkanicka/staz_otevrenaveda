# znazorneni posunuteho odhadu variance
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

# smycka pro test odhadu pro ruzne delky nahodnych vzorku

sample_size = [] 		# osa x - velikost vzorku
biased_data = []		# hodnoty pro varN
unbiased_data = []		# hodnoty pro varNm1
true_variance = []		# hodnoty skutecne variance

for ns in range(10, 500, 10):
	k = 0
	varN = 0		# odhad variance s 1/N
	varNm1 = 0			# odhad variance s 1/(N-1)

	all_data = [] 		# data pro vvypocet zkutecneho rozptylu

	for j in range(1, 1000):			# smycka pro mnoho pokusu s odhady varinace ze vzorku delky ns

		data = uniform.rvs(size=ns)		#generovani nahodnych dat
		mu = np.mean(data)			#vypocet prumeru
		var = sum((data-mu)**2)		#soucet ctvercu odchylek od prumeru
		varN += var/ns
		varNm1 += var/(ns-1)
		k += 1

		for x in data:
			all_data.append(x)		# prevod na 1d list

	print(ns, varN/k, varNm1/k)   	# vypis velikosti vzorku, biased a unbiased variance

	biased_data.append(varN/k)
	unbiased_data.append(varNm1/k)		# přidávání hodnot pro graf
	sample_size.append(ns)

	mean = sum(all_data)/len(all_data)
	trueVar = sum((all_data - mean)**2)/len(all_data)		#vypocet skutecnych varianci smycky
	true_variance.append(trueVar)

true_variance = [sum(true_variance)/len(sample_size)]		# skutecna variance

plt.plot(sample_size, true_variance*len(sample_size), linestyle = '--', label = "true variance")
plt.plot(sample_size, biased_data, color = "red", label = "biased sample variance")
plt.plot(sample_size, unbiased_data, color = "blue", label = "unbiased sample variance")
plt.xlabel("sample size")
plt.ylabel(" sample variance value")
plt.title("comparison of biased/unbiased sample variance")
plt.legend(loc = "lower right")
plt.show()

print("\n true variance value: ", true_variance)
