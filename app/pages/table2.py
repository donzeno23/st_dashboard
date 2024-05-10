#app.py
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder  #add import for GridOptionsBuilder

@st.cache_data()
def load_data():
    data = pd.read_csv("./data/data.csv", parse_dates=["referenceDate"])
    return data

data = load_data()

gb = GridOptionsBuilder()

# makes columns resizable, sortable and filterable by default
gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=False,
)

#configures state column to have a 80px initial width
gb.configure_column(field="state", header_name="State", width=80)

#configures Power Plant column to have a tooltip and adjust to fill the grid container
gb.configure_column(
    field="powerPlant",
    header_name="Power Plant",
    flex=1,
    tooltipField="powerPlant",
)

gb.configure_column(field="recordType", header_name="Record Type", width=110)

gb.configure_column(
    field="buyer", header_name="Buyer", width=150, tooltipField="buyer"
)

#applies a value formatter to Reference Date Column to display as a short date format.
gb.configure_column(
    field="referenceDate",
    header_name="Reference Date",
    width=100,
    valueFormatter="value != undefined ? new Date(value).toLocaleString('en-US', {dateStyle:'medium'}): ''",
)

#Numeric Columns are right aligned
gb.configure_column(
    field="hoursInMonth",
    header_name="Hours in Month",
    width=50,
    type=["numericColumn"],
)
#The last column is the value column and will be formatted using javascript number.toLocaleString()
gb.configure_column(
    field="volumeMWh",
    header_name="Volume [MWh]",
    width=100,
    type=["numericColumn"],
    valueFormatter="value.toLocaleString()",
)

#makes tooltip appear instantly
gb.configure_grid_options(tooltipShowDelay=0)
go = gb.build()

AgGrid(data, gridOptions=go, height=400)