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

## Get likelihoods from pm_only_tf3_9comp

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvv_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvv_ext_tf3corr_like9.fits \
    -p gmm_params/pm_only_tf3_9comp \
    -bs 100_000 \
    -ps pm_only_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/virac2_withextinction_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/virac2_ext_tf3corr_like9.fits \
    -p gmm_params/pm_only_tf3_9comp \
    -bs 100_000 \
    -ps pm_only_tf3
```

```bash
python main.py \
    -f /home/jorge/zorro/base_sample/lowbulge/46_tf3corr_nolikelihood/vvvx_tf3corr.fits \
    -o /home/jorge/zorro/base_sample/lowbulge/49_likelihood_tf3/vvvx_tf3corr_like9.fits \
    -p gmm_params/pm_only_tf3_9comp \
    -bs 100_000 \
    -ps pm_only_tf3
```

## Get total probability

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

## Para muestras cuts*

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
