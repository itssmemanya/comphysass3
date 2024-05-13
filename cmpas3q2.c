#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

#define PI 3.14159265358979323846

// Define sinc function
double sinc(double x) 
{
    if (x == 0) 
	{
       	return 1.0;
	} 
	else 
	{
        return sin(x) / x;
    }
}

// Fourier transform of sinc function
void fourier_transform_sinc(double *x_values, double *k_values, double *ans, int N) 
{
    int i, j;
    fftw_complex *in, *out;
    fftw_plan plan;
    in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    for (i = 0; i < N; i++) 
	{
        in[i][0] = sinc(x_values[i]);
        in[i][1] = 0.0; // Imaginary part
    }
    fftw_execute(plan);

    for (i = 0; i < N; i++) 
	{
        ans[i] = sqrt(out[i][0]*out[i][0] + out[i][1]*out[i][1]) / sqrt(2 * PI); 
    }
    fftw_destroy_plan(plan);
    fftw_free(in);
    fftw_free(out);
}

int main() 
{
    double f_min = -30;
    double f_max = 30;
    int num_points = 1000;
    double *f_values = (double*) malloc(num_points * sizeof(double));
    double *x_FT = (double*) malloc(num_points * sizeof(double));
    double *rearranged_FT = (double*) malloc(num_points * sizeof(double));
    for (int i = 0; i < num_points; i++) 
	{
        f_values[i] = f_min + i * (f_max - f_min) / (num_points - 1);
    }

    fourier_transform_sinc(f_values, f_values, x_FT, num_points);

    for (int i = 0; i < num_points / 2; i++) 
	{
        rearranged_FT[i] = x_FT[num_points / 2 + i];
        rearranged_FT[num_points / 2 + i] = x_FT[i];
    }

    printf(" Frequency (f) | Fourier Transform (FFT) \n");
    for (int i = 0; i < num_f_points; i++) 
	{
        printf("%f | %f\n", f_values[i], rearranged_FT[i]);
    }

    free(f_values);
    free(x_FT_numerical_values);
    free(rearranged_FT);
    return 0;
}

