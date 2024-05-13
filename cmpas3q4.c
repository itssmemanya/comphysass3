#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#include <complex.h>

#define PI 3.14159265358979323846
#define N 1024 

double gaussian(double x)
{
    return exp(-x*x);
}

double analytical_ft(double k)
{
    return sqrt(0.5)* exp(-k*k/4.0);
}

int main() 
{
    int i;
    double x[N], k[N], f[N], delta_x, factor;
    fftw_complex *in, *out;
    fftw_plan p;

    double xmin = -10.0;
    double xmax = 10.0;
    delta_x = (xmax-xmin)/N;
    
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    
	printf(" Gaussian of x \n")
    for (i = 0; i < N; ++i) {
        x[i] = xmin + i * delta_x;
        printf("%f %f\n", x[i], gaussian(x[i]));
        in[i][0] = gaussian(x[i]); 
        in[i][1] = 0.0; // Imaginary part
    }
    
    p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE); 
    fftw_execute(p); 
    
    printf("\n  k values | FFTW | Analytical Result  \n")
    for (i = 0; i < N; ++i) 
	{
        if (i==0)
		{
           k[i] = 0;
        }
        else if (i<N/2)
		{
            k[i] = i / (N * delta_x);
        }
        else 
		{
            k[i] = -(N-i) / (N * delta_x);
        }
        factor = delta_x * sqrt(1.0/(2*PI)) * creal(cexp(I*k[i]*2*PI*xmin));
        printf("%f | %f | %f\n", 2*PI*k[i], fabs(factor * out[i][0]), analytical_ft(2*PI*k[i]));
    }

    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);
    return 0;
}
