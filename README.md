# pmprob

Get the probabilities asociated with a GMM model

## Example usage

```bash
python main.py \
    -f /home/jorge/Documents/data/sgr/base_sample/lowbulge/30_proc/virac2_lowbulge_proc.fits \
    -o /home/jorge/Documents/data/sgr/base_sample/lowbulge/40_likelihood/virac2_lowbulge_like_pm+par.fits  \
    -p gmm_params/pm+par_7comp \
    -bs 400_000 \
    -ps pm+parallax 
```

```bash
python main.py  \
    -f /home/jorge/Documents/data/sgr/base_sample/lowbulge/30_proc/virac2_lowbulge_proc.fits  \
    -o /home/jorge/Documents/data/sgr/base_sample/lowbulge/40_likelihood/virac2_lowbulge_like_pm_only.fits \
    -p gmm_params/pm_only_13comp \
    -bs 400_000 \
    -ps pm_only
```

```bash
python main.py \
    -f /home/jorge/data/sgr/base_sample/lowbulge/30_proc/vvv_gaia_lowbulge_proc.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/40_likelihood/vvv_gaia_lowbulge_like_pm+parallax.fits \
    -p gmm_params/pm+par_7comp \
    -bs 400_000 \
    -ps pm+parallax
```

```bash
python main.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/30_proc/vvv_gaia_lowbulge_proc.fits  \
    -o /home/jorge/data/sgr/base_sample/lowbulge/40_likelihood/vvv_gaia_lowbulge_like_pm_only.fits \
    -p gmm_params/pm_only_13comp \
    -bs 400_000 \
    -ps pm_only
```

```bash
python main.py \
    -f /home/jorge/Documents/data/sgr/base_sample/lowbulge/30_proc/vvvx_x_gaia_lowbulge_proc.fits \
    -o /home/jorge/Documents/data/sgr/base_sample/lowbulge/40_likelihood/vvvx_x_gaia_lowbulge_like_pm+par.fits \
    -p gmm_params/pm+par_7comp \
    -bs 100_000 \
    -ps pm+parallax
```

```bash
python main.py  \
    -f /home/jorge/Documents/data/sgr/base_sample/lowbulge/30_proc/vvvx_x_gaia_lowbulge_proc.fits  \
    -o /home/jorge/Documents/data/sgr/base_sample/lowbulge/40_likelihood/vvvx_x_gaia_lowbulge_like_pm_only.fits \
    -p gmm_params/pm_only_13comp \
    -bs 100_000 \
    -ps pm_only
```

## Get Total probabilities

Testing

```bash
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/40_likelihood/vvvx_x_gaia_lowbulge_proc_likelihood_pm+parallax.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/70_totalprob/ESTE_vvvx_x_gaia_lowbulge_proc_likelihood_pm+parallax.fits \
    -eta 0.01 \
    -niter 1
```

```bash
python getprob.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/60_merged/virac2_x_vvvx_pmonly_merged.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/70_totalprob/virac2_x_vvvx_pmonly_merged_prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash
python getprob.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/60_merged/virac2_x_vvvx_pm+par_merged.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/70_totalprob/virac2_x_vvvx_pm+par_merged_prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash
python getprob.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/60_merged/vvv_x_vvvx_pmonly_merged.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/70_totalprob/vvv_x_vvvx_pmonly_merged_prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash
python getprob.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/60_merged/vvv_x_vvvx_pm+par_merged.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/70_totalprob/vvv_x_vvvx_pm+par_merged_prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash
python getprob.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/40_likelihood/vvvx_x_gaia_lowbulge_like_pm_only.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/70_totalprob/vvvx_x_gaia_pm_only_prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash
python getprob.py  \
    -f /home/jorge/data/sgr/base_sample/lowbulge/40_likelihood/vvvx_x_gaia_lowbulge_like_pm+par.fits \
    -o /home/jorge/data/sgr/base_sample/lowbulge/70_totalprob/vvvx_x_gaia_pm+par_prob.fits \
    -eta 0.01 \
    -niter 2
```

## Get likelihoods from pm+par_pmcorrtf3_11comp

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvv_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_withextinction_tf3corr_like.fits \
    -p gmm_params/pm+par_pmcorrtf3_11comp \
    -bs 100_000 \
    -ps pm+parallax
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/virac2_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_withextinction_tf3corr_like.fits \
    -p gmm_params/pm+par_pmcorrtf3_11comp \
    -bs 100_000 \
    -ps pm+parallax
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvvx_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like.fits \
    -p gmm_params/pm+par_pmcorrtf3_11comp \
    -bs 100_000 \
    -ps pm+parallax
```

## Get likelihoods from pm+par_tf3_9comp
```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvv_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9.fits \
    -p gmm_params/pm+par_tf3_9comp \
    -bs 100_000 \
    -ps pm+parallax_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/virac2_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9.fits \
    -p gmm_params/pm+par_tf3_9comp \
    -bs 100_000 \
    -ps pm+parallax_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvvx_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9.fits \
    -p gmm_params/pm+par_tf3_9comp \
    -bs 100_000 \
    -ps pm+parallax_tf3
```


### Get total probability

/home/jorge/Documents/data/sgr/base_sample/lowbulge/49_likelihood_tf3/


```bash  # ARCHIVO 1 MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_withextinction_tf3corr_like.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvv_ext_tf3corr_pm+parallax-prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash  # ARCHIVO 2  MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_withextinction_tf3corr_like.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/virac2_ext_tf3corr_pm+parallax-prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash  # ARCHIVO 3 MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_withSFDextinction_tf3corr_like.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvvx_ext_tf3corr_pm+parallax-prob.fits \
    -eta 0.01 \
    -niter 2
```

```bash  # ARCHIVO A_9 MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_withextinction_tf3corr_like9.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvv_ext_tf3corr_pm+parallax-prob9.fits \
    -eta 0.01 \
    -niter 1
```

```bash  # ARCHIVO B_9 MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_withextinction_tf3corr_like9.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/virac2_ext_tf3corr_pm+parallax-prob9.fits \
    -eta 0.01 \
    -niter 1
```

```bash  # ARCHIVO C_9 MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvvx_ext_tf3corr_pm+parallax-prob9.fits \
    -eta 0.01 \
    -niter 1
```


#### Para muestras cuts*

```bash MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par_cuts.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/virac2_ext_tf3corr_prob9_pm+par_cuts.fits \
    -eta 0.01 \
    -niter 1
```

```bash MALO-REHACER falto -ps pm+parallax_tf3
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par_cuts.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvv_ext_tf3corr_prob9_pm+par_cuts.fits \
    -eta 0.01 \
    -niter 1
```
