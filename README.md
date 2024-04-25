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
cd Dropbox/develop/pmprob/
python main.py  \
    -f /home/jorge/Documents/data/sgr/base_sample/lowbulge/proc/vvvx_x_gaia_lowbulge_proc.fits \
    -o /home/jorge/vvvx_x_gaia_lowbulge_proc_likelihood_pmonly.fits \
    -p gmm_params/pm_only_13comp \
    -ps pm_only
```
