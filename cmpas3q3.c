#include <stdio.h>
#include <stdlib.h>
#include <gsl/gsl_fft_complex.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_math.h>

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

void gsl_fourier_transform_sinc(double *x_values, double *k_values, double *ans, int N) 
{
    int i;
    double *in;
    gsl_fft_complex_wavetable *wavetable;
    gsl_fft_complex_workspace *workspace;
    data = (double *)malloc(2 * N * sizeof(double));

    for (i = 0; i < N; i++) 
	{
        in[2*i] = sinc(x_values[i]);
        in[2*i+1] = 0.0; // Imaginary part
    }

    wavetable = gsl_fft_complex_wavetable_alloc(N);
    workspace = gsl_fft_complex_workspace_alloc(N);
    gsl_fft_complex_forward(in, 1, N, wavetable, workspace);

    for (i = 0; i < N; i++) 
	{
        ans[i] = sqrt(in[2*i]*in[2*i] + in[2*i+1]*in[2*i+1]) / sqrt(2 * PI);
    }

    gsl_fft_complex_wavetable_free(wavetable);
    gsl_fft_complex_workspace_free(workspace);
    free(data);
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

    gsl_fourier_transform_sinc(f_values, f_values, x_FT, num_points);

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
    free(x_FT);
    free(rearranged_FT);
    return 0;
}
