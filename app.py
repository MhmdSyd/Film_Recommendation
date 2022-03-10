# =================================Import Liberaries=================================== #
import pandas as pd
import numpy as np
import random
import os
import warnings

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# ========================================================================================#
warnings.filterwarnings('ignore')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# ===================================read-data============================================ #
df_movies = pd.read_csv('data/movies_Clean.csv')
df_movies['movie_id'] = df_movies['movie_id'].astype('string')
df_recommend = pd.read_csv('data/Movies_Recommendation.csv', index_col=["user_id"])
options_list = [{'label': str(x), 'value': str(x)} for x in [*df_recommend.index]]
random_value = str(random.sample([*df_recommend.index], 1)[0])

# =================================Methods============================================= #
def recommend_movies(user_id):
    df_only_user = df_recommend.loc[user_id, ['user_filters', 'recommend_movies']]
    movies = df_only_user['recommend_movies'].split()
    similar_users = df_only_user['user_filters'].split()
    if len(similar_users)>5:
        random_users = " and some of similar users are: "+", ".join(random.sample(similar_users, 5))
    else:
        random_users = " and This is a new user so there isn't similar user yet."
    return random.sample(movies, 10), random_users

# ==================================Text field========================================== #
def drawText():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Movies Recommendation System"),
                ], className="navbar navbar-expand-lg navbar-dark bg-dark", style={'textAlign': 'center', 'color':'#fff'}) 
            ]), color = 'dark'
        ),
    ])

# ===================================Bootstrap Sheet===================================== #
external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash(__name__, 
                external_stylesheets=external_stylesheets,
                update_title='Loading...',
                title='Movies'
)

server = app.server


app.layout = html.Div([
    dbc.Card(
        dbc.CardBody([
#===================================Dashboard Title================================#
            dbc.Row([
                
                    html.H2("Movies Recommendation System",  style={'textAlign': 'center', 'color':'#fff'}),
                    
            ], className="navbar navbar-expand-lg navbar-dark bg-dark"),
            
            dbc.Row([
                dbc.Col([
                    
                    dcc.Dropdown(
                        options=options_list,
                        value=random_value,
                        clearable=False,
                        id='demo-dropdown', style={"margin-bottom": "1rem!important"}),
                ], width=2, style={"margin-bottom": "1rem!important"}),
                
                dbc.Col([
                    html.H5(id="comment", className="card-text")
                ], width=10, className="card", style={'margin-bottom':'0px', 'padding':'5px'})
                
            ], className="navbar navbar-expand-lg navbar-light bg-light"),
            
            html.Br(),
# ============================Row of Movies One=================================== #
            dbc.Row([
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster1',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title1", 
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
            
                ], width=3),
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster2',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title2",
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
                    
                ], width=3),
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster3',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title3",
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
                    
                ], width=3),
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster4',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title4", 
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
                    
                ], width=3)
            ], justify="center", align='center', style={"border-bottom": "2px solid #000"}),
            
            dbc.Row([
                html.Br()
            ]),
# ========================================Row Two============================================== #
            dbc.Row([
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster5',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title5", 
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
            
                ], width=3),
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster6',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title6",
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
                    
                ], width=3),
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster7',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title7", 
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
                    
                ], width=3),
                dbc.Col([
                    html.Div(
                        children=[
                            html.Img(id='poster8',
                                     src={}, 
                                     className="rounded mx-auto d-block", 
                                     style={"width":"90%", "border": "2px solid #000"}
                                    )
                        ]
                    ),
                    html.Br(),
                    html.H5(id="Title8", 
                            className="text-center", 
                            style={"color":"#279fcd", "font-size":"medium", "width":"100%"}
                           )
                    
                ], width=3)
            ], justify="center", align='center') 
          
            

        ], style={"padding":"0rem 0.8rem"})
    )
])

@app.callback(
    Output('poster1', 'src'),
    Output('poster2', 'src'),
    Output('poster3', 'src'),
    Output('poster4', 'src'),
    Output('poster5', 'src'),
    Output('poster6', 'src'),
    Output('poster7', 'src'),
    Output('poster8', 'src'),
    Output('Title1', 'children'),
    Output('Title2', 'children'),
    Output('Title3', 'children'),
    Output('Title4', 'children'),
    Output('Title5', 'children'),
    Output('Title6', 'children'),
    Output('Title7', 'children'),
    Output('Title8', 'children'),
    Output('comment', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(user):
    movies_ids, similar_users = recommend_movies(int(user))
    comment = "You select user no. "+user+ similar_users
    df_slice = df_movies[df_movies['movie_id'].isin(movies_ids)]
    posters = [*df_slice['Poster'].values]
    titles = [*df_slice['Title'].values]
    return posters[0], posters[1], posters[2], posters[3], posters[4], posters[5], posters[6], posters[7], titles[0], titles[1], titles[2], titles[3], titles[4], titles[5], titles[6], titles[7], comment


#===================================run server====================================#
if __name__ == '__main__':
    app.run_server(debug=True)