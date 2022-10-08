import sys
file_path = sys.argv[1]
name = sys.argv[2]
sample_coeff = sys.argv[3]

outd2freq = {}
ind2freq = {}
fr = open(file_path,'r')
for line in fr:
    arr = line.strip().split(',')
    ind = int(arr[-2])
    outd = int(arr[-1])
    if not outd in outd2freq:
        outd2freq[outd] = 0
    outd2freq[outd] += 1
    if not ind in ind2freq:
        ind2freq[ind] = 0
    ind2freq[ind] += 1
fr.close()
fw = open(f'{name}_{sample_coeff}_outd-distr.csv','w')
for outd, freq in sorted(outd2freq.items(),key=lambda x:x[0]):
    fw.write(str(outd)+','+str(freq)+'\n')
fw.close()
fw = open(f'{name}_{sample_coeff}_ind-distr.csv','w')
for ind, freq in sorted(ind2freq.items(),key=lambda x:x[0]):
    fw.write(str(ind)+','+str(freq)+'\n')
fw.close()


# ind2freq = {}
# fr = open(file_path,'r')
# for line in fr:
#     arr = line.strip().split(',')
#     ind = int(arr[-2])
#     if not ind in ind2freq:
#         ind2freq[ind] = 0
#     ind2freq[ind] += 1
# fr.close()
# fw = open(f'{kind}_{sample_coeff}_ind-distr.csv','w')
# for ind, freq in sorted(ind2freq.items(),key=lambda x:x[0]):
#     fw.write(str(ind)+','+str(freq)+'\n')
# fw.close()
