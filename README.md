# pmprob

Get the probabilities asociated with a GMM model

## Example usage

```bash
python main.py \
    -f input.fits \
    -o output.fits \
    -p gmm_params/pm+par_7comp \
    -ps pm+parallax
```

```bash
python main.py  \
    -f /home/jorge/Documents/data/sgr/base_sample/lowbulge/proc/vvvx_x_gaia_lowbulge_proc.fits \
    -o /home/jorge/vvvx_x_gaia_lowbulge_proc_likelihood_pmonly.fits \
    -p gmm_params/pm_only_13comp \
    -ps pm_only
```

```bash
python main.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/proc/vvv_gaia_lowbulge_proc.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/likelihood/vvv_gaia_lowbulge_likelihood_pmonly.fits \
    -p gmm_params/pm_only_13comp \
    -ps pm_only
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/proc/virac2_lowbulge_proc.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/likelihood/virac2_lowbulge_proc_likelihood_pm+parallax.fits \
    -p gmm_params/pm+par_7comp \
    -ps pm+parallax
```

```bash
python main.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/proc/virac2_lowbulge_proc.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/likelihood/virac2_lowbulge_proc_likelihood_pmonly.fits \
    -p gmm_params/pm_only_13comp \
    -ps pm_only
```

## Get Total probabilities

Testing

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/likelihood/vvvx_x_gaia_lowbulge_proc_likelihood_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/likelihood/vvvx_x_gaia_lowbulge_proc_likelihood_pmonly_totalprob.fits \
    -eta 0.01 \
    -niter 10 
```

### Case VVVX +  VIRAC2 PM+PARALLAX

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/likelihood/virac2_x_vvvx_pm+parallax_merged.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/totalprob/virac2_x_vvvx_pm+parallax_merged_totalprob.fits \
    -eta 0.01 \
    -niter 10
```

### Case VVVX +  VIRAC2 (ONLYPM)

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/likelihood/virac2_x_vvvx_pmonly_merged.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/totalprob/virac2_x_vvvx_pmonly_merged_totalprob.fits \
    -eta 0.01 \
    -niter 10
```

### Case VVV + VVVX (PM+PARALLAX)

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/60_merged/virac2_x_vvvx_pmonly_merged.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/totalprob/virac2_x_vvvx_pm+parallax_merged_totalprob.fits \
    -eta 0.01 \
    -niter 10
```

### Case VVVX +  VIRAC2 (ONLY PM)

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/60_merged/virac2_x_vvvx_pmonly_merged_fixed.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/70_totalprob/virac2_x_vvvx_pmonly_totalprob.fits \
    -eta 0.01 \
    -niter 10
```

### Case VVVX +  VIRAC2 (PM+PARALLAX)

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/60_merged/virac2_x_vvvx_pm+parallax_merged_fixed.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/70_totalprob/virac2_x_vvvx_pm+parallax_totalprob.fits \
    -eta 0.01 \
    -niter 10
```


### Case VVVX +  VVV (ONLY PM)

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/60_merged/vvv_x_vvvx_pmonly_merged.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/70_totalprob/vvv_x_vvvx_pmonly_totalprob.fits \
    -eta 0.01 \
    -niter 10
```

### Case VVVX +  VVV (PM+PARALLAX)

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/60_merged/vvv_x_vvvx_pm+parallax_merged.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/70_totalprob/vvv_x_vvvx_pm+parallax_totalprob.fits \
    -eta 0.01 \
    -niter 10
```
