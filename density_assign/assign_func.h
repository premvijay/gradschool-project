#include <cmath>
#ifndef ASSIGN_FUNC_H_INCLUDED
#define ASSIGN_FUNC_H_INCLUDED

float W_cic(float diff){
return std::abs(1.0 - diff);
};

float W_ngp(float diff){
return 1;
};

#endif // ASSIGN_FUNC_H_INCLUDED
