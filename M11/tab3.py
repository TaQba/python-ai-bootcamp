import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

def render_tab(df):
    df['weekday'] = df['tran_date'].dt.day_name()
    df = df.drop('tran_date', axis=1)
    all = df.groupby(['weekday']).sum().sort_values(by='total_amt', ascending=False).reset_index()
    fig = go.Figure(data=[go.Bar(x=all['weekday'], y=all['total_amt'])],layout=go.Layout(title='Wszystkie kanały na dzień tygodnia'))

    ind = df.groupby(['Store_type', 'weekday']).sum().reset_index()

    df2 = pd.DataFrame({
        "Day": [day for day in ind['weekday']],
        "Amount": [amount for amount in ind['total_amt']],
        "Store Type": [types for types in ind['Store_type']],
    })

    fig2 = px.bar(df2, x="Day", y="Amount", color="Store Type", barmode="group")

    layout = html.Div(
        [
            html.H1('Kanał sprzedaży',style={'text-align':'center'}),
            html.Div(
            [
                        html.Div(
                            [dcc.Graph(id='bar-weekdays-all',figure=fig)],style={'width':'50%'}
                        ),
                        html.Div(
                            [dcc.Graph(id='bar-weekdays-ind', figure=fig2)], style={'width': '50%'}
                        ),
                    ],
                style={'display':'flex'}
            ),
            html.Div(id='temp-out')
        ]
    )

    return layout
