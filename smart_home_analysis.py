import pandas as pd
import plotly.express as px

# Chargement du dataset
df = pd.read_csv(r"C:\Users\nadin_pbj\Downloads\casas_data\data",header=None)  # Mets le vrai nom ici


# Vérifier le contenu réel
print("Aperçu brut du fichier :")
print(df.head())

# Le fichier a tout mis dans une seule colonne => df[0] existe maintenant
# Découper chaque ligne en 4 parties : timestamp, code, event, value (value est parfois vide ou long texte)
df[['timestamp', 'code', 'event', 'value']] = df[0].str.extract(r'(\S+ \S+)\s+(\S+)\s+(\S+)\s*(.*)')

# Supprimer la colonne brute d’origine
df = df.drop(columns=0)

# Affichage final
print("\nDataFrame structuré :")
print(df.head())

# Compter les événements
event_counts = df['event'].value_counts()

# Tracer
fig = px.bar(event_counts, x=event_counts.index, y=event_counts.values,
             labels={'x': 'Événement', 'y': 'Fréquence'}, title='Distribution des événements')
fig.show()

# 2. Visualisation : événements ON/OFF dans le temps par capteur
df_filtered = df[df['event'].isin(['ON', 'OFF'])]
fig2 = px.scatter(df_filtered, x='timestamp', y='code', color='event',
                  title='État ON/OFF par capteur dans le temps')
fig2.show()

# 3. Visualisation : évolution des valeurs numériques (températures, etc.)
df_temp = df[df['event'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]
df_temp['value'] = df_temp['event'].astype(float)
fig3 = px.line(df_temp, x='timestamp', y='value', color='code',
               title='Évolution des valeurs numériques (ex: température)')
fig3.show()
