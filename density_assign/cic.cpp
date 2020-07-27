#include <stdio.h>
#include <iostream>
#include <cmath>
#include "assign_func.h"


int main(int argc, char** argv){

    FILE *fp;

    /* Open file as binary for reading */
    fp = fopen(argv[1], "rb");

    int num_prtcl_this_file;
    fseek(fp,8,SEEK_SET);
    fread(&num_prtcl_this_file, sizeof(int), 1, fp);
    printf("Number of particles in this file is %i \n",num_prtcl_this_file);

    /* Seek to a position in the file */
    fseek(fp, 260, SEEK_SET);
    int size_head;
    int size_posd;
    /* Read and display data */
    fread(&size_head, sizeof(int), 1, fp);
    fread(&size_posd, sizeof(int), 1, fp);

    printf("Header size is %i\n", size_head);
    printf("Position block size is %i\n", size_posd);

//    float posi[3];
    float xi,yi,zi;
    int xc,yc,zc;

    printf("xi is %f \n",xi);

    int grid_len = 128;
    float density_grid[grid_len][grid_len][grid_len];


//    float density_grid1[128][128][128];
    std::cout << "grid_size"<< sizeof(density_grid);

//    printf("%f \n",density_grid[1][1][1]);

    for (int i = 0; i < num_prtcl_this_file; i++) {
        if (i == 184393){
            std::cout << xi<<" "<<yi<<" "<<zi<<" \n";
            printf("Position of particle %i is %f,%f,%f \n", i,xi,yi,zi);
        };
        
        fread(&xi, sizeof(float), 1, fp);
        fread(&yi, sizeof(float), 1, fp);
        fread(&zi, sizeof(float), 1, fp);

        xc = (int)xi;
        yc = (int)yi;
        zc = (int)zi;

        density_grid[xc][yc][zc]       += W_cic(xc-xi)*   W_cic(yc-yi)*   W_cic(zc-zi);
        density_grid[xc][yc][zc+1]     += W_cic(xc-xi)*   W_cic(yc-yi)*   W_cic(zc+1-zi);
        density_grid[xc][yc+1][zc]     += W_cic(xc-xi)*   W_cic(yc+1-yi)* W_cic(zc-zi);
        density_grid[xc][yc+1][zc+1]   += W_cic(xc-xi)*   W_cic(yc+1-yi)* W_cic(zc+1-zi);
        density_grid[xc+1][yc][zc]     += W_cic(xc+1-xi)* W_cic(yc-yi)*   W_cic(zc-zi);
        density_grid[xc+1][yc][zc+1]   += W_cic(xc+1-xi)* W_cic(yc-yi)*   W_cic(zc+1-zi);
        density_grid[xc+1][yc+1][zc]   += W_cic(xc+1-xi)* W_cic(yc+1-yi)* W_cic(zc-zi);
        density_grid[xc+1][yc+1][zc+1] += W_cic(xc+1-xi)* W_cic(yc+1-yi)* W_cic(zc+1-zi);

    }

    printf("%f \n",density_grid[1][1][1]);

    FILE *fp_grid;
    fp_grid = fopen(argv[2],"wb");
    fwrite(density_grid, sizeof(float), sizeof(density_grid)/sizeof(float), fp_grid);


//    printf("%i \n", i);
//   printf("position is %f \n", pos[2145][1]);

    fclose(fp);
    fclose(fp_grid);
    return 0;
}
