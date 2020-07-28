for i in {0..8}
do
	echo "Run no. $i"
#	./cic ../../snapshot_200.$i density_grid.$i
	./cic /mnt/scratch/aseem/sims/scm1024/r1/snapshot_200.$i density_grid.$i &
done
