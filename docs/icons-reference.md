# Icons reference

Math4AI includes built-in icon draw functions used by mindmaps.

Use icon key `"name"` in `mindmap.json` to resolve `draw_name_icon`.

## Linear algebra and matrix topics

- `norm_ball`, `ortho`, `proj`, `subspaces`
- `orthonormal_matrix`, `rotation_circle`, `qr`, `householder`
- `rank1`, `lu`, `ldu`, `det_area`, `shear`
- `eigenvector_scaling`, `eigendecomp`, `svd`, `svd_mapping`, `schur`
- `lora`, `kronecker`, `block_matrix`
- `ellipsoid`, `cholesky`
- matrix-shape icons: `row`, `col`, `square`, `diagonal`, `antidiagonal`, `lower`, `upper`, `tall`, `wide`

## Optimization and calculus topics

- `gradient`, `taylor`, `duality`, `newton`

## Probability and stochastic process topics

- `bayes`, `gaussian`, `kl`, `markov`
- `backup`, `contraction`, `em`, `reparam`
- `score_field`, `denoising`, `langevin_step`, `mala`
- `ito_vs_strat`, `ito_lemma`, `zoh`, `ssm`
- `density_evolution`, `current`

## Utility icon

- `placeholder`

## Notes

- Icon defaults (line width, shape proportions, default size) are defined in `icon_utils.py`.
- For one-off figures, define `draw_<name>_icon` in your script and set `"icon": "<name>"` in JSON.
