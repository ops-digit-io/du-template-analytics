# UC-XXXX-XXXX · Analytics PoC (Cookiecutter Data Science)

PoC for UC-XXXX-XXXX · PLANT · process — proof-of-concept, not production data.

Structure from [cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science):
raw data in `data/raw/`, reusable code in the `analysis` package, exploratory work in
`notebooks/`, outputs in `reports/`.

```bash
cd poc
make requirements
pip install -e .            # make the analysis package importable in notebooks
jupyter lab notebooks/
```
