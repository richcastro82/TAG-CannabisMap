import pandas as pd
import dash
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, dash_table
import dash_html_components as html
# import dash_bootstrap_components as dbc
from dash.dependencies import State, Input, Output

app = Dash(__name__,)
server=app.server

df = pd.read_csv("table.csv", dtype={"code": str})
df2=pd.read_csv("table.csv")
map_data = df.copy()
#State_List=['Floida', 'Alabama']


def FullMap():
        figure = px.choropleth(
        map_data,
        locations='id',
        #labels={'State':'Medicinal'},
        locationmode='USA-states',
        color='Legal Status',
        hover_name="State",

        hover_data=["Medicinal", "Decriminalized"],
        color_discrete_sequence=["#97C072", "#34B924", "#C47D3B"],
        scope="usa"
        )

        figure.update_layout(
         autosize=False,
        margin = dict(
                l=20,
                r=20,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            width=900,
            height=600,

            legend_title_text="",
            legend=dict(
                # x=0,
                # y=1,

                orientation="h",
                yanchor="bottom",
                y=-.2,
                xanchor="center",
                x=.5,
                traceorder="reversed",
                title_font_family="Times New Roman",
                font=dict(
                    family="Courier",
                    size=12,
                    color="black"
                ),
                bgcolor="LightSteelBlue",
                bordercolor="Black",
                borderwidth=2
            )
        )


        return figure
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(style={'width':'100%'},children=[
    # html.H1("HashTAG State Level THC Map", style={'text-align': 'center'}),





    html.Div(style={'width':'100%','margin':'auto'}, children=[
        html.Div(id='output_container', children=[
            dcc.Graph(id='hash_map', config= {'displaylogo': False}, figure=FullMap()),
            html.P(className="source", children=["Source: Marijuana Policy Project"]),
            html.P(className="sourceDate", children=["Report Date: 12/15/2022"]),


            #     fig.update_layout(legend=dict(
            #     orientation="h",
            #     yanchor="bottom",
            #     y=1.02,
            #     xanchor="right",
            #     x=1
            # ))


            # fig.update_layout(
            #     legend=dict(
            #         x=0,
            #         y=1,
            #         traceorder="reversed",
            #         title_font_family="Times New Roman",
            #         font=dict(
            #             family="Courier",
            #             size=12,
            #             color="black"
            #         ),
            #         bgcolor="LightSteelBlue",
            #         bordercolor="Black",
            #         borderwidth=2
            #     )
            # )





            ]),
            html.Br(),]),




#
#     html.Div(style={'width':'800px', 'margin':'auto'},children=[
#             dash_table.DataTable(
#                 id='table',
#                 style_as_list_view=True,
#                 style_cell={'padding': '5px','backgroundColor': '#f5f5f5'},
#                 style_header={
#                     'backgroundColor': '#bafc03',
#                     'fontWeight': 'bold'
#                     },
#                 columns=[{"name": i, "id": i} for i in df2.columns],
#                 data=(df2.to_dict('records')),
#                 )
#     ]),
#
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
# @app.callback(
#     Output(component_id='hash_map', component_property='figure'),
#     Input(component_id='select_state', component_property='value')
# )
# def update_graph(option_slctd):
#     # container = "State selected: {}".format(option_slctd)
#     map_data = df.copy()
#     fig = px.choropleth(
#         map_data,
#         locations='state',
#         locationmode='USA-states',
#         color='legality',
#         scope="usa"
#     )
#
#     return fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
