# IDT mmWave self-resonance teaching draft

Status: editorial draft on a separate branch; not linked from the live website.

- `article.md`: editable Chinese article.
- `index.html` and `article.css`: static reading preview.
- `assets/`: complete graphical regions of published Figs. 9, 16 and 19.

## Source

X. Liu, J. Zheng, and Y. Yang, “Scale Interdigital Transducer-Based Microacoustic Resonators Into mmWave Applications,” IEEE TUFFC 72(5), 674–685, May 2025. DOI: https://doi.org/10.1109/TUFFC.2025.3554004.

Original figures © 2025 IEEE. This is an author's research commentary. The figures retain their scientific content, labels, curves and legends; surrounding article text was cropped away, and Chinese captions were written separately. No new open license is granted to these figures.

## Editorial verification

The central teaching point is reducing self-inductance while retaining the required static capacitance. Three constructed examples explain the LC scaling law, capacitive reactance and finger-length/count tradeoff. Reported research results are drawn only from the published paper.

The 300 fF comparison uses measured SRF values 7.874 and 23.4 GHz, and reported A1 quality factors 9.794 and 35.76. The 130 fF comparison distinguishes the approximate 50 GHz summary from Fig. 18(g)'s measured >50 GHz bound and simulated 51.1477 GHz value. EM SRF is not the acoustic operating frequency, and an improvement in observed Q is not a direct measurement of intrinsic material loss.

Fig. 16 is discussed by its actual axes: panel (a) plots static capacitance, panel (b) current-loop count. The article does not reproduce the apparently exchanged panel references in the accompanying source prose. The source's qualitative inductance geometry relations are not presented as exact quantitative formulas.

## Publication

Keep this PR in Draft until editorial review is finished. Publication requires moving the article to the chosen blog path and adding site navigation in a later change. A draft branch in a public repository is publicly readable.
