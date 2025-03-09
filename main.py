
import datetime

# from methods.sort_the_algs import sort_the_algs


with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/generate-inverses/INPUT_file/alg_list_input_file.txt") as file_input:
    algs = file_input.read().splitlines() 


for alg in algs:

    alg = alg.strip()





print("\n\n\n")
inverse_algs = []
for alg in algs:
       inverse_algs.append(alg)

       


# WRITE TO FILE:  filtered algs
dt = datetime.datetime.now()
output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/generate-inverses/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_output")
with open(output_filename, "x") as output_file:
	for alg in inverse_algs:
		output_file.write(f"{alg}\n")

