# Import class to test
from __init__ import Analyser


# Test data
t1 = {'Adam': ['Bob'], 'Bob': ['Adam', 'Amir', 'Mia'], 'Amir': ['Bob', 'Mia'], 'Mia': ['Bob', 'Amir'], 'Chris': ['Zia'], 'Zia': ['Chris'], 'Liz': []}
t2 = {'Huntley': ['Clementina', 'Mirtha'], 'Clementina': ['Huntley', 'Contessa'], 'Leonarda': ['Mirtha'], 'Mirtha': ['Leonarda', 'Huntley', 'Marjorie'], 'Prudence': ['Shamika', 'Gidget'], 'Shamika': ['Prudence'], 'Marjorie': ['Mirtha'], 'Gidget': ['Prudence'], 'Contessa': ['Clementina'], 'Marylouise': []}
t3 = {'Mikey': ['Richardo'], 'Richardo': ['Mikey', 'Louie', 'Asia'], 'Margarete': ['Louie'], 'Louie': ['Margarete', 'Richardo'], 'Rozella': ['Carolann'], 'Carolann': ['Rozella', 'Kimberli', 'Kimberli'], 'Vanna': ['Asia', 'Theodor'], 'Asia': ['Vanna', 'Richardo', 'Elida'], 'Nisha': ['Adrianna'], 'Adrianna': ['Nisha'], 'Theodor': ['Vanna'], 'Kimberli': ['Carolann', 'Carolann'], 'Elida': ['Asia'], 'Dick': [], 'Rafaela': []}
t4 = {'Toshia': ['Elenor', 'Ian'], 'Elenor': ['Toshia', 'Kandace'], 'Merril': ['Laurinda'], 'Laurinda': ['Merril', 'Ian'], 'Ian': ['Laurinda', 'Toshia'], 'Rochester': ['Marven', 'Corinne'], 'Marven': ['Rochester', 'Shayne', 'Annice', 'Michael'], 'Shayne': ['Marven', 'Corinne'], 'Annice': ['Marven', 'Luvenia'], 'Kandace': ['Elenor'], 'Corinne': ['Rochester', 'Shayne'], 'Asuncion': ['Briggs'], 'Briggs': ['Asuncion', 'Lucretia'], 'Luvenia': ['Annice'], 'Michael': ['Marven'], 'Lucretia': ['Briggs'], 'Eboni': [], 'Reid': [], 'Isabelle': [], 'Maxim': []}
t5 = {'Xymenes': ['Mora'], 'Mora': ['Xymenes', 'Carroll'], 'Kindra': ['Delinda'], 'Delinda': ['Kindra', 'Raylene'], 'Sadie': ['Carroll'], 'Carroll': ['Sadie', 'Maxima', 'Marry', 'Godfrey', 'Mora'], 'Maxima': ['Carroll'], 'Barbra': ['Teodoor'], 'Teodoor': ['Barbra', 'Marget'], 'Shanti': ['Van'], 'Van': ['Shanti', 'Natacha'], 'Cori': ['Ikey', 'Patel'], 'Ikey': ['Cori', 'Wallace', 'Cesar'], 'Barnabas': ['Gidget'], 'Gidget': ['Barnabas', 'Tereasa', 'Latrina', 'Lorita'], 'Lauran': ['Upton', 'Elisa'], 'Upton': ['Lauran'], 'Marry': ['Carroll'], 'Elisa': ['Lauran', 'Magdalen'], 'Wallace': ['Ikey'], 'Tereasa': ['Gidget'], 'Jean-Christophe': ['Magdalen', 'Cathrine'], 'Magdalen': ['Jean-Christophe', 'Elisa'], 'Godfrey': ['Carroll'], 'Leigh': ['Ruben'], 'Ruben': ['Leigh', 'Broddy', 'Broddy', 'Johann'], 'Carina': ['Markus'], 'Markus': ['Carina'], 'Tamala': ['Natacha'], 'Natacha': ['Tamala', 'Van'], 'Cesar': ['Englebert', 'Ikey'], 'Englebert': ['Cesar'], 'Broddy': ['Ruben', 'Ruben'], 'Latrina': ['Gidget', 'Marget'], 'Patel': ['Cori'], 'Ruthanne': ['Breana'], 'Breana': ['Ruthanne'], 'Cathrine': ['Jean-Christophe'], 'Marget': ['Latrina', 'Teodoor'], 'Lorita': ['Gidget'], 'Johann': ['Ruben'], 'Raylene': ['Delinda'], 'Niall': [], 'Sherlene': [], 'Kenyetta': [], 'Luetta': [], 'Eulalia': [], 'Malorie': [], 'Allena': [], 'Gerome': []}
t6 = {'Theola': ['Penny'], 'Penny': ['Theola', 'Donnie'], 'Vernell': ['Janella', 'Kaylene', 'Linda'], 'Janella': ['Vernell', 'Anika', 'Ladawn', 'Winfield'], 'Saw': ['Arvy'], 'Arvy': ['Saw', 'Melba'], 'Karma': ['Seema', 'Sully'], 'Seema': ['Karma', 'Hubert', 'Jeri'], 'Fermina': ['Anika', 'Pascale'], 'Anika': ['Fermina', 'Janella'], 'Randall': ['Pascale', 'Alise'], 'Pascale': ['Randall', 'Ericka', 'Fermina'], 'Hubert': ['Marinda', 'Seema'], 'Marinda': ['Hubert', 'Waylen'], 'Barbera': ['Thad'], 'Thad': ['Barbera'], 'Kathrin': ['Alise'], 'Alise': ['Kathrin', 'Randall', 'Carlena'], 'Errol': ['Danny'], 'Danny': ['Errol'], 'Arline': ['Neoma'], 'Neoma': ['Arline', 'Kamilah'], 'Douglas': ['Dalia', 'Martainn'], 'Dalia': ['Douglas', 'Manie'], 'Ranee': ['Udell'], 'Udell': ['Ranee', 'Reynard'], 'Rochelle': ['Gaye', 'Angeline'], 'Gaye': ['Rochelle', 'Kalyn'], 'Manie': ['Dalia', 'Gilberte'], 'Derek': ['Felice'], 'Felice': ['Derek', 'Justis', 'Candi'], 'Byram': ['Shelton'], 'Shelton': ['Byram', 'Althea'], 'Kit': ['Beatris', 'Partha'], 'Beatris': ['Kit', 'Lonnie'], 'Kaylene': ['Vernell', 'Frazier'], 'Carlena': ['Alise', 'Moshe'], 'Althea': ['Lonnie', 'Shelton'], 'Lonnie': ['Althea', 'Sully', 'Shanika', 'Beatris'], 'Angeline': ['Rochelle', 'Leia'], 'Paul': ['Deeann', 'Bernie'], 'Deeann': ['Paul'], 'Partha': ['Kit'], 'Maurice': ['Moshe'], 'Moshe': ['Maurice', 'Carlena'], 'Justis': ['Felice'], 'Bernie': ['Paul', 'Stanford'], 'Sully': ['Lonnie', 'Karma'], 'Rhiannon': ['Chanel'], 'Chanel': ['Rhiannon', 'Marleen'], 'Kamilah': ['Neoma'], 'Kalyn': ['Gaye'], 'Linda': ['Vernell'], 'Gilles': ['Shani', 'Lavelle'], 'Shani': ['Gilles'], 'Elsa': ['Yolande', 'Bessie', 'George'], 'Yolande': ['Elsa', 'Eleanor'], 'Adele': ['Jeri'], 'Jeri': ['Adele', 'Seema'], 'Shanika': ['Lonnie'], 'Ericka': ['Pascale'], 'Stanford': ['Bernie'], 'Frazier': ['Kaylene'], 'Leia': ['Angeline', 'Eleanor'], 'Marleen': ['Chanel'], 'Waylen': ['Marinda'], 'Eleanor': ['Yolande', 'Leia'], 'Bessie': ['Elsa'], 'Melba': ['Arvy'], 'Lavelle': ['Gilles'], 'Martainn': ['Douglas'], 'Donnie': ['Penny'], 'Letha': ['Reynard'], 'Reynard': ['Letha', 'Udell'], 'George': ['Elsa'], 'Ladawn': ['Janella'], 'Winfield': ['Janella'], 'Gilberte': ['Manie'], 'Candi': ['Felice'], 'Husain': [], 'Karleen': [], 'Torrey': [], 'Oda': [], 'Dixie': [], 'Emogene': [], 'Rolph': [], 'Eliza': [], 'Garold': [], 'Burl': [], 'Floyd': [], 'Laurene': [], 'Latrina': [], 'Lewis': [], 'Lyn': [], 'Maryrose': [], 'Vertie': [], 'Tibold': [], 'Jaimie': [], 'Noriko': []}


# Create test data store
set_test_data = [t1, t2, t3, t4, t5, t6]

# iterate through and test data with an instance
for data in set_test_data:
    instance = Analyser(data)
    print(f'{str(instance)}\n')
    for user in data.keys():
        print(instance.calc_friend_total(user))

    print(instance.least_friends())

    for user1 in data.keys():
        print(instance.direct_relationships(user1))

    print(instance.indirect_relationships())

