# pmprob
Get the probabilities asociated with a GMM model

# Example usage
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


## Pendientes

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

