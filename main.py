from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__, template_folder='templates')

server = 'DESKTOP-UO3DV01\SQLEXPRESS01'
database = 'PrzychodniaMedyczna'
connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wizyty', methods=['GET', 'POST'])
def wizyty():
    if request.method == 'POST':
        ID_wizyty = request.form['ID_wizyty']
        ID_pacjenta = request.form['ID_pacjenta']
        ID_lekarza = request.form['ID_lekarza']
        Data = request.form['Data']
        Opis = request.form['Opis']
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Wizyty (ID_wizyty, ID_pacjenta, ID_lekarza, Data, Opis) VALUES (?, ?, ?, ?, ?)", (ID_wizyty, ID_pacjenta, ID_lekarza, Data, Opis))
        conn.commit()
        conn.close()
        return redirect(url_for('wizyty'))
    return render_template('wizyty.html')

@app.route('/platnosci', methods=['GET', 'POST'])
def platnosci():
    if request.method == 'POST':
        ID_wizyty = request.form['ID_wizyty']
        Kwota = request.form['Kwota']
        Data_platnosci = request.form['Data_platnosci']
        ID_lekarza = request.form['ID_lekarza']
        ID_pacjenta = request.form['ID_pacjenta']
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Platnosci (ID_transakcji, Kwota, Data_platnosci, ID_lekarza, ID_pacjenta) VALUES (?, ?, ?, ?, ?)", (ID_wizyty, Kwota, Data_platnosci, ID_lekarza, ID_pacjenta))
        conn.commit()
        conn.close()
        return redirect(url_for('platnosci'))
    return render_template('platnosci.html')

@app.route('/lekarze', methods=['GET', 'POST'])
def lekarze():
    if request.method == 'POST':
        imie_i_nazwisko = request.form['imie_i_nazwisko']
        pesel = request.form['pesel']
        nr_telefonu = request.form['nr_telefonu']
        adres = request.form['adres']
        specjalizacja = request.form['specjalizacja']
        email = request.form['email']
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Lekarze (imie_i_nazwisko, pesel, nr_telefonu, adres, specjalizacja, email) VALUES (?, ?, ?, ?, ?, ?)",(imie_i_nazwisko, pesel, nr_telefonu, adres, specjalizacja, email))
        conn.commit()
        conn.close()
        return redirect(url_for('lekarze'))
    return render_template('lekarze.html')

@app.route('/pacjenci', methods=['GET', 'POST'])
def pacjenci():
    if request.method == 'POST':
        imie_i_nazwisko = request.form['imie_i_nazwisko']
        pesel = request.form['pesel']
        nr_telefonu = request.form['nr_telefonu']
        adres = request.form['adres']
        email = request.form['email']
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Pacjent (imie_i_nazwisko, pesel, nr_telefonu, adres, email) VALUES (?, ?, ?, ?, ?)", (imie_i_nazwisko, pesel, nr_telefonu, adres, email))
        conn.commit()
        conn.close()
        return redirect(url_for('pacjenci'))
    return render_template('pacjenci.html')

@app.route('/recepty', methods=['GET', 'POST'])
def recepty():
    if request.method == 'POST':
        if 'ID_Recepty' not in request.form:
            return "Błąd: Brak ID_Recepty w żądaniu"

        ID_Recepty = request.form['ID_Recepty']
        Data_Wystawienia = request.form['Data_Wystawienia']
        ID_Pacjenta = request.form['ID_Pacjenta']
        ID_Lekarza = request.form['ID_Lekarza']

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Recepta (ID_Recepty, Data_Wystawienia, ID_Pacjenta, ID_Lekarza) VALUES (?, ?, ?, ?)", (ID_Recepty, Data_Wystawienia, ID_Pacjenta, ID_Lekarza))
        conn.commit()
        conn.close()
        return redirect(url_for('recepty'))
    return render_template('recepty.html')

if __name__ == '__main__':
    app.run(debug=True)
