# Optional demonstration. Open this file and choose Run Cell above each cell marker.
# Use Python 3.12 (ECON 3030). Paths work from the root or a course subfolder.
# All observations are synthetic teaching data, not official statistics.

# %%
import polars as pl
import altair as alt
from pathlib import Path

alt.renderers.enable("mimetype")

# The Interactive Window may start in the project root or the script folder.
project = Path.cwd()
if not (project / "data/state_unemployment.csv").exists():
    project = project.parent
df = pl.read_csv(project / "data/state_unemployment.csv")
df.head()

# %%
california = df.filter(
    pl.col("state") == "California"
)
california

# %%
chart = (
    alt.Chart(california)
    .mark_line(point=True)
    .encode(
        x=alt.X("year:O", title="Year", sort="ascending"),
        y=alt.Y("unemployment_rate:Q", title="Unemployment rate (%)",
                scale=alt.Scale(zero=True),
                axis=alt.Axis(labelExpr="datum.value + '%'")),
        tooltip=[alt.Tooltip("year:O", title="Year"),
                 alt.Tooltip("unemployment_rate:Q", title="Unemployment rate (%)", format=".1f")]
    )
    .properties(title="California unemployment, 2014 to 2023 (synthetic)", width=520, height=280)
)

chart
