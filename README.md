# pmprob

Get the probabilities asociated with a GMM model.

## Get likelihoods from pm+par_tf3_9comp

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvv_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par.fits \
    -p gmm_params/pm+par_tf3_9comp \
    -bs 100_000 \
    -ps pm+parallax_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/virac2_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par.fits \
    -p gmm_params/pm+par_tf3_9comp \
    -bs 100_000 \
    -ps pm+parallax_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvvx_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9_pm+par.fits \
    -p gmm_params/pm+par_tf3_9comp \
    -bs 100_000 \
    -ps pm+parallax_tf3
```

## Get likelihoods from pm_only_tf3_15comp

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvv_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like15_pmonly.fits \
    -p gmm_params/pm_only_tf3_15comp \
    -bs 100_000 \
    -ps pm_only_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/virac2_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like15_pmonly.fits \
    -p gmm_params/pm_only_tf3_15comp \
    -bs 100_000 \
    -ps pm_only_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvvx_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like15_pmonly.fits \
    -p gmm_params/pm_only_tf3_15comp \
    -bs 100_000 \
    -ps pm_only_tf3
```


## Apply cuts to the data

```bash  OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par_cuts.fits \
    -ks 16.0\
    -p 0.1
```

```bash  OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par_cuts.fits \
    -ks 16.0\
    -p 0.1
```

```bash  OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9_pm+par_cuts.fits \
    -ks 16.0\
    -p 0.1
```

```bash  OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like15_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like15_pmonly_cuts.fits \
    -ks 16.0\
    -p 0.1
```

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like15_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like15_pmonly_cuts.fits \
    -ks 16.0\
    -p 0.1
```

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like15_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like15_pmonly_cuts.fits \
    -ks 16.0 \
    -p 0.1
```

### Apply cuts to the data (deeper fotometry v2)

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par_cuts2.fits \
    -ks 16.5\
    -p 0.1
```

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par_cuts2.fits \
    -ks 16.5\
    -p 0.1
```

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9_pm+par_cuts2.fits \
    -ks 16.5\
    -p 0.1
```

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like15_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like15_pmonly_cuts2.fits \
    -ks 16.5\
    -p 0.1
```

```bash OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like15_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like15_pmonly_cuts2.fits \
    -ks 16.5\
    -p 0.1
```

```bash  OK
python cut_tool.py \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like15_pmonly.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like15_pmonly_cuts2.fits \
    -ks 16.5 \
    -p 0.1
```

## Get total probability (deprecated)

```bash  # ARCHIVO 1
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvv_ext_tf3corr_pm+par-prob9.fits \
    -eta 0.01 \
    -niter 1
```

```bash  # ARCHIVO 2 
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9_pm+par.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/virac2_ext_tf3corr_pm+par_prob9.fits \
    -eta 0.01 \
    -niter 1
```

```bash  # ARCHIVO 3 
python getprob.py  \
    -f /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_withSFDextinction_tf3corr_like.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/73_totalprob_tf3/vvvx_ext_tf3corr_pm+parallax-prob.fits \
    -eta 0.01 \
    -niter 1
```
