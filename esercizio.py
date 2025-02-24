
def mostra_menu():
   # Mostra il menu delle operazioni disponibili.
   print("\n--- BANCOMAT ---")
   print("1️⃣ Prelievo")
   print("2️⃣ Deposito")
   print("3️⃣ Controllo saldo")
   print("4️⃣ Esci")

def prelievo(saldo, importo):
   """
   Gestisce il prelievo verificando che il saldo sia sufficiente.
   """
   if importo > saldo:
       print("❌ Saldo insufficiente!")
   elif importo <= 0:
       print("❌ Importo non valido!")
   else:
       saldo -= importo
       print(f"✅ Prelievo effettuato! Nuovo saldo: {saldo:.2f}€")
   return saldo

def deposito(saldo, importo):
   """
   Gestisce il deposito verificando che sia un importo valido.
   """
   if importo <= 0:
       print("❌ Importo non valido!")
   else:
       saldo += importo
       print(f"✅ Deposito effettuato! Nuovo saldo: {saldo:.2f}€")
   return saldo

def mostra_saldo(saldo):
   """
   Mostra il saldo attuale.
   """
   print(f"💰 Saldo attuale: {saldo:.2f}€")

# Inizializzazione del saldo
saldo = 1000.0

# Loop principale
while True:
   mostra_menu()
   scelta = input("🔹 Scegli un'opzione: ")

   try:
       if scelta == "1":
           importo = float(input("💵 Quanto vuoi prelevare? "))
           saldo = prelievo(saldo, importo)
       elif scelta == "2":
           importo = float(input("💰 Quanto vuoi depositare? "))
           saldo = deposito(saldo, importo)
       elif scelta == "3":
           mostra_saldo(saldo)
       elif scelta == "4":
           print("👋 Grazie per aver usato il bancomat!")
           break
       else:
           print("⚠️ Scelta non valida! Riprova.")
   except ValueError:
       print("❌ Errore: Inserisci un numero valido!")


