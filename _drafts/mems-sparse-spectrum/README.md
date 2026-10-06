# MEMS sparse-spectrum blog draft

Status: editorial draft; not linked from the live website.

- `article.md`: editable Chinese article source.
- `index.html`: self-contained static page using `article.css` and local image assets.
- `assets/fig05-architecture.png`: complete graphical area of paper Fig. 5.
- `assets/fig15-reconstruction.png`: complete graphical area of paper Fig. 15.

The article uses a teaching register with explicitly labelled constructed examples. It distinguishes uniform sparse sampling from feature-aware reference-spectrum resampling, and observed data from learned priors. It describes the interpolation baseline, learned residual, observation-value restoration and three consistency losses using Algorithm 1.

## Source and attribution

X. Liu et al., “Toward Intelligent Design and Measurement of MEMS Acoustic Wave Resonators,” IEEE TMTT, 74(4), 3478–3490, 2026. DOI: https://doi.org/10.1109/TMTT.2025.3649908.

Images were extracted from the IEEE published PDF, accessed at https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11333585. The published article explicitly states © 2026 The Authors, CC BY 4.0. The extraction removes surrounding paper text and replaces captions with Chinese descriptions; the figure content is unchanged.

## Editorial checks before release

The draft intentionally avoids specifying how resonance anchors were generated for the 16-point experiment: Algorithm 1 lists anchors, whereas Section III-C specifies a uniform mask without fully documenting anchor provenance. Confirm against the corresponding published-version implementation before adding reproduction instructions or claims of inference without resonance priors.

The reported R² > 0.98 is attributed to the paper's 25% held-out cohort. Do not reinterpret it as a guarantee for every device or channel. A 98% decrease in sample count is not a measured 98% decrease in total test time.

All reported research results and figures come from the published article. Constructed teaching examples are explicitly labelled.

Version 2 (2026-10-06) introduces the article through VNA testing and adds concrete examples of scan spacing, missed narrow peaks, residual correction, equal-magnitude/different-phase responses, local peak-position errors, batch timing and unfamiliar device responses. The model's demonstrated scope remains complex admittance reconstruction for the paper's SAW devices. S11/S21 applications are introductory context and possible adaptation targets, not additional validated results.

## Publication

This directory is stored on the draft branch. The production navigation has not been changed. Before publication, finish editorial review and move the article to the site's chosen blog path, then add a link to the site. A draft branch in a public repository is publicly readable; draft status does not provide access control.
