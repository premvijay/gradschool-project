for i in 0 1 2 3
do
	echo "Run no. $i"
	./cic ../../snapshot_200.$i density_grid.$i
done
