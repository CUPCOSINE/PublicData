# Six Years Annual Modulation Signal Search

![GitHub last commit](https://img.shields.io/github/last-commit/CUPCOSINE/PublicData?path=COSINE100-6YearsModulation%2FREADME.md)
[![arXiv](https://img.shields.io/badge/arXiv-2409.13226-CC1400.svg)](https://arxiv.org/abs/2409.13226)

- The data used in the ["COSINE-100 Full Dataset Challenges the Annual Modulation Signal of DAMA/LIBRA"](https://arxiv.org/abs/2409.13226) paper are available in this folder.
- If you use data in this folder, please cite [arXiv:2409.13226](https://arxiv.org/abs/2409.13226).

## Notation

- `erc`, `nrc`, and `irc` in the file names indicate the calibration policy adopted.
  - `erc` stands for `electron-recoil-compatible` with the DAMA experiment. It adopted the linear calibration pivoted at 60 keV gamma-ray. It is identical to $\mathrm{keV_{ee}}$ in the paper.
  - `nrc` stands for `(sodium)-nuclear-recoil-compatible` with the DAMA experiment. It calibrates considering the different quenching factors (for Na-recoil) of two experiments, DAMA and COSINE-100. Dividing them by 0.3 gives the energy in $\mathrm{keV_{nr}}$ in the paper.
  - `irc` stands for `iodine-(nuclear)-recoil-compatible` with the DAMA experiment. It calibrates considering the different quenching factors (for I-recoil) of two experiments, DAMA and COSINE-100. Dividing them by 0.09 gives the energy in $\mathrm{keV_{nr,~I}}$ in the paper.
  - Examples
    - `erc1-3` indicates 1-3 $\mathrm{keV_{ee}}$ (linearly-calibrated energy unit).
    - `erc2-6` indicates 2-6 $\mathrm{keV_{ee}}$ (linearly-calibrated energy unit).
    - `nrc2-6` indicates 6.7-20 $\mathrm{keV_{nr}}$ ($2 \div 0.3$ gives 6.7, $6 \div 0.3$ gives 20). It corresponds to 2-6 keV in the DAMA detectors.
    - `irc2-6` indicates 22.2-66.7 $\mathrm{keV_{nr,~I}}$ ($2 \div 0.09$ gives 22.2). It corresponds to 2-6 keV in the DAMA detectors.
- Event rate unit
  - For `erc` calibration, the event rates and modulation amplitudes are represented in the unit of "counts/day/kg/$\mathrm{keV_{ee}}$". It corresponds to so-called DRU, daily-rate-unit.
  - For `nrc` calibration, the event rates and modulation amplitudes are represented in the unit of "counts/day/kg/units of (3.3 $\mathrm{keV_{nr}}$)". The weird constant 3.3 makes the resulting numbers to be identical to the numbers in DRU.
  - For `irc` calibration, the event rates and modulation amplitudes are represented in the unit of "counts/day/kg/units of (11 $\mathrm{keV_{nr,~I}}$)". The weird constant 11 makes the resulting numbers to be identical to the numbers in DRU.

## Visualizers

- The Python notebooks in the `visualizers` folder help you to draw the plots in the paper. They were tested under the environment as following.
  - `Python==3.10.8`, `numpy==1.25.2`, `matplotlib==3.8.3`, `cmasher==1.8.0`, `scipy==1.12.0`, `pandas==2.1.4`, `iminuit==2.24.0`

## Data Description

- `BackgroundRate_<roi>.csv`: best-fit total background event rates in the `<roi>`. See [Notation](#notation) for more information on `<roi>`.
  - `day_centers`: days after 2016.01.01-00:00.
  - `background_crystal#`: the background event rate for the crystal in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration) or "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration) unit.
- `EventRate_<roi>.csv`: 15-day-bin event rates of the COSINE-100 full dataset in the `<roi>`. See [Notation](#notation) for more information on `<roi>`.
  - `day_centers`: days after 2016.01.01-00:00.
  - `event_rate_crystal#`: the event rate for the crystal in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration) or "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration) unit.
    - `event_rate_error_crystal#`: the 1$\sigma$ error for `event_rate_crystal#`.
  - `residual_crystal#`: `event_rate_crystal#` - `background_crystal#` from `BackgroundRate_<roi>.csv`.
    - `residual_error_crystal#`: the 1$\sigma$ error for `residual_crystal#`.
  - `mean_residual`: the average residual event rate. Averaged over `residual_crystal#` for all crystals considering `residual_error_crystal#`.
    - `mean_residual_error`: the 1$\sigma$ error for `mean_residual`.
  - `livetime_efficiency_crystal#`: the time-efficiency of the crystal collecting the good-quality data during the time bin.
  - `counts_crystal#`: the number of events collected in the time bin.
    - Note that not only the `livetime_efficiency` but also the event selection efficiency must be considered to convert `counts` into `event_rate`.
- `AmplitudePosterior_<roi>.csv`: the phase-fixed annual modulation amplitude posterior distribution obtained through the MCMC technique.
  - `amplitude`: the modulation amplitude in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration), "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration), or "counts/day/kg/11 $\mathrm{keV_{nr,~I}}$" (for `irc` calibration) unit.
  - `mcmc_samples`: the number of MCMC samples sampled from the COSINE-100 full dataset.
- `PseudoUnderDama_<roi>.csv`: the expected distribution of the best-fits under the assumption of the DAMA's claim to be true.
  - `amplitude_median`: the best-fit obtained from the pseudo-experiments in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration), "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration), or "counts/day/kg/11 $\mathrm{keV_{nr,~I}}$" (for `irc` calibration) unit.
  - `pseudo_experiments`: the number of pseudo-experiments yielded the `amplitude_median`.
- `TwoDimensionalPosterior_<roi>_histogram.csv`: the phase-floated annual modulation amplitude and phase posterior distribution obtained through the MCMC technique.
  - `amplitude`: the modulation amplitude in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration) or "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration) unit.
  - `phase`: the modulation phase in day unit.
  - `mcmc_samples`: the number of MCMC samples sampled from the COSINE-100 full dataset.
- `TwoDimensionalPosterior_<roi>_pdf.csv`: probability density function of `TwoDimensionalPosterior_<roi>_histogram.csv`, smoothed using Gaussian kernel density estimation.
  - `amplitude`: the modulation amplitude in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration) or "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration) unit.
  - `phase`: the modulation phase in day unit.
  - `pdf`: the probability density.
- `AmplitudeSpectrum.csv`: the spectrum of the phase-fixed annual modulation amplitude obtained from the COSINE-100 full dataset.
  - `energy_min`, `energy_max`: minimum/maximum energy for the bin in "counts/day/kg/$\mathrm{keV_{ee}}$" (for `erc` calibration) or "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" (for `nrc` calibration) unit.
  - `dama_amplitude`: the modulation amplitudes reported by DAMA/LIBRA.
    - `dama_amplitude_error`: corresponding 1$\sigma$ error.
  - `cosine_<calibration>_<coincidence>_amplitude`: the modulation amplitude obtained from the COSINE-100 full dataset `<coincidence>` data, with `<calibration>` calibration policy.
    - Example: `cosine_nrc_single_amplitude`: the modulation amplitude obtained from the COSINE-100 full dataset single-hit data, with `nrc` calibration policy, in "counts/day/kg/3.3 $\mathrm{keV_{nr}}$" unit.
    - `cosine_<calibration>_<coincidence>_amplitude_upper/lower_error`: corresponding 1$\sigma$ errors.
- `SelectionEfficiency.csv`: event selection efficiency as a function of energy.
  - `energy_kevee_#`: the energy for crystal`#` in $\mathrm{keV_{ee}}$ unit.
  - `efficiency_#`: the event selection efficiency for crystal`#`.
    - `efficiency_upper/lower_bound_#`: corresponding 1$\sigma$ credible interval.
- `CosineNaQF.csv`: the quenching factor for the Na-quenching, measured by the COSINE collaboration.
  - `nuclear_recoil_energy`: the original nuclear recoil energy in $\mathrm{keV_{nr}}$ unit.
  - `qf`: the quenching factor in %.
    - `qf_err`: corresponding 1$\sigma$ error in %.
- `CosineIQF.csv`: the quenching factor for the I-quenching, measured by the COSINE collaboration.
  - `nuclear_recoil_energy`: the original nuclear recoil energy in $\mathrm{keV_{nr,~I}}$ unit.
  - `qf`: the quenching factor in %.
    - `qf_err`: corresponding 1$\sigma$ error in %.
