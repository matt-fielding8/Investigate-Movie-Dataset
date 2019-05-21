# Investigate df_split

df_cgp = pd.read_csv('/home/ding/coding/DAND/investigate_\
            dataset_project/movies_dataset/df_split_cgp.csv')

df_actors = df_cgp.groupby('cast')
actor_means = df_actors.mean()
actor_counts = df_actors.count()
actor_profit = actor_means.profit
actor_profit_adj = actor_means.profit_adj

prod_comp_count = df_cgp.groupby('production_companies').count()
prod_comp_mean = df_cgp.groupby('production_companies').mean()
prod_comp_sum = df_cgp.groupby('production_companies').sum()
prod_comp_prof_av = prod_comp_mean.profit
prod_comp_prof_adj_av = prod_comp_mean.profit_adj
prod_comp_prof_tot = prod_comp_sum.profit
prod_comp_prof_adj_tot = prod_comp_sum.profit_adj

genres = df_cgp.groupby('genres')
genres_pop = genres.popularity.mean()
genres_count = genres.count()['id']
genres_prof = genres.profit.mean()
genres_prof_adj = genres.profit_adjt.mean()

# most successful actor director partnerships
pairs_da = df_cgp.groupby(['cast', 'director'])
pairs_ag = df_cgp.groupby(['cast', 'genres'])
pairs_dg = df_cgp.groupby(['director', 'genres'])
trips_adp = df_cgp.groupby(['cast', 'director', 'production_companies'])

pairs_da.count().sort_values(axis=1, ascending=False)['id']
pairs_dg.count().sort_values(axis=1, ascending=False)['id']
trips_adp.count().sort_values(axis=1, ascending=False)['id']

# Make date-time bins
labelsQ = ['Q1', 'Q2', 'Q3', 'Q4']
labelsM = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

df_clean_br.head()
df_clean_br['release_date'] = pd.to_datetime(df_clean_br['release_date'], dayfirst=True)

months = df_clean_br.groupby(df_clean_br.release_date.dt.month).mean()
quarters = df_clean_br.groupby(df_clean_br.release_date.dt.quarter).mean()
