# PythonExam

JupyterLite for written exams in STA, ALI, and SMP at VIA University College.

The site is built with the Xeus Python browser kernel. Its Python runtime and selected packages are included in the GitHub Pages output, so normal calculations do not need a package CDN.

## Site

- JupyterLab: https://rbrooksdk.github.io/PythonExam/lab/index.html
- Notebook view: https://rbrooksdk.github.io/PythonExam/notebooks/
- Package check notebook: `exam-content/Start.ipynb`

## Included Python packages

- NumPy, SciPy, pandas, and Matplotlib
- SymPy
- statsmodels and scikit-learn
- openpyxl for Excel files
- Plotly

Python's standard library and dependencies of these packages are also included. The build environment is defined in `environment.yml`.

These choices follow the current [STA course](https://rbrooksdk.github.io/STA1_26/), [Danish STA course](https://rbrooksdk.github.io/STA_26/), [ALI course](https://rbrooksdk.github.io/ALI1_26/), and [SMP course](https://rbrooksdk.github.io/SMP1_26/). The courses use NumPy, pandas, SciPy, Matplotlib, SymPy, statsmodels, and some examples use scikit-learn, openpyxl, or Plotly.

## Build and checks

GitHub Actions builds and deploys the site from `.github/workflows/deploy.yml`. The workflow checks that the chosen packages and Xeus runtime are bundled and runs `scripts/smoke.py` in a browser Python environment with network access disabled. It also checks that the OpenAI Python package is not preinstalled.

Adding a package to `environment.yml` changes the next build. A package's presence in the build does not grant access to an external service.

## Exam access

WISEflow controls access to internet domains, not Python import statements. For an exam using this site, allow the `rbrooksdk.github.io` domain and remove the old `cdn.jsdelivr.net` resource after the new version has been tested inside the lockdown browser. The browser test should cover notebook startup, the package check notebook, any supplied data files, and submission of results.

This repository is public. Do not put exam questions, solutions, credentials, or API keys in it.
