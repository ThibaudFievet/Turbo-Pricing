def calcul_prix_turbo(prix_sous_jacent, strike, parite, type_turbo):
    """
    Formule :
    - Call : (Sous-jacent - Strike) / Parité
    - Put  : (Strike - Sous-jacent) / Parité
    """
    if type_turbo == "call":
        return (prix_sous_jacent - strike) / parite
    elif type_turbo == "put":
        return (strike - prix_sous_jacent) / parite
    else:
        raise ValueError("Le type de turbo doit être 'call' ou 'put'.")


def calcul_stop_loss(mise_initiale, prix_turbo, perte_max):
    """
    Calcule le prix du turbo en Stop Loss.
    """
    quantite_turbos = int(mise_initiale // prix_turbo) #Quantity can't a float
    prix_turbo_sl = prix_turbo - (perte_max / quantite_turbos) #ex: 2.50−200/400 = 2.50−0.5 = 2.00

    if prix_turbo_sl <= 0:
        raise ValueError("Stop Loss invalide")

    return prix_turbo_sl


def main():
    print("\n Calcul du Stop Loss pour un Turbo \n")

    try:
        # Saisie et validation du type de turbo
        type_turbo = input(" Type de turbo (call/put) : ").strip().lower() # in order to avoid errors
        if type_turbo not in ["call", "put"]:
            raise ValueError("Le type de turbo doit être 'call' ou 'put'.")

        # Choix de calcul du prix du turbo
        mode_calcul = input(" Voulez-vous calculer le prix d'achat du turbo ? (o/n) : ").strip().lower()

        if mode_calcul == "o":
            prix_sous_jacent = float(input(" Prix du sous-jacent : "))
            strike = float(input(" Strike du turbo : "))
            if type_turbo == "call":
                if prix_sous_jacent <= strike:
                    raise ValueError("Pour un call, le prix du sous jacent ne peut pas être inférieur ou égal au strike") # car sinon prix du turbo est négatif ou égal à 0, ce qui n'est pas possible
            if type_turbo == "put":
                if prix_sous_jacent > strike:
                    raise ValueError("Pour un put, le prix du sous jacent ne peut pas être supérieur ou égal au strike")
            parite = float(input(" Parité du turbo : "))

            # Calcul du prix du turbo en fonction des paramètres
            prix_turbo = calcul_prix_turbo(prix_sous_jacent, strike, parite, type_turbo)
            print(f"\n Prix du Turbo utilisé : {prix_turbo:.3f} €\n")

        else:
            prix_turbo = float(input(" Entrez le prix d'achat du turbo : "))
            if prix_turbo <= 0:
                raise ValueError("Le prix du turbo doit être positif.")

        # Saisie des autres paramètres
        perte_max = float(input(" Perte maximale autorisée (€) : "))
        mises = []
        erreur_detectee = []

        for m in input("Entrez la ou les mises (séparées par un/des espaces) : ").split(): #.split renvoie une liste de chaine de caratères
            try:
                val = float(m)
                if val > 0:
                    mises.append(val)
                else:
                    erreur_detectee.append(m)  # nombre nul ou négatif
            except ValueError:
                erreur_detectee.append(m)  # pas un nombre (ex : 'abc')

        if erreur_detectee:
            if len(erreur_detectee) == 1:
                print(f" {erreur_detectee[0]} est une valeur impossible.")
            else:
                print("Les valeurs suivantes sont impossibles :")
                for i in erreur_detectee:
                    print(f"-{i}")

        if not mises:
            raise ValueError("Aucune mise initiale valide n’a été fournie.")

    except ValueError as e:
        print(f"\n Erreur de saisie : {e}\n")
        return

    # Calcul et affichage des Stop Loss
    print(" Prix Turbo SL (€) ")

    for mise in mises:
        prix_turbo_sl = calcul_stop_loss(mise, prix_turbo, perte_max)
        if prix_turbo_sl is not None:
            print(f" {prix_turbo_sl:3f} ")
        else:
            print(f" Erreur  ")

if __name__ == "__main__":

    main()
