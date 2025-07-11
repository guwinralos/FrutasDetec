import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

modelo = YOLO("best.pt")


info_nutricional = {
    "Maçã":       {"kcal": 95,  "prot": 0.5,  "carb": 25,  "gord": 0.3},
    "Banana":     {"kcal": 105, "prot": 1.3,  "carb": 27,  "gord": 0.3},
    "Kiwi":       {"kcal": 42,  "prot": 0.8,  "carb": 10,  "gord": 0.4},
    "Limão":      {"kcal": 17,  "prot": 0.6,  "carb": 5.4, "gord": 0.2},
    "Laranja":    {"kcal": 62,  "prot": 1.2,  "carb": 15,  "gord": 0.2},
    "Morango":    {"kcal": 4.8, "prot": 0.11, "carb": 1.15,"gord": 0.045}
}

def detectar_frutas(imagem_bgr):
    resultado = modelo(imagem_bgr, verbose=False, conf=0.7)[0]
    contagem = {}

    for caixa in resultado.boxes:
        x1, y1, x2, y2 = map(int, caixa.xyxy[0])
        indice_classe = int(caixa.cls[0])
        nome_bruto = modelo.names[indice_classe].strip().capitalize()

        if nome_bruto in ["Maca", "Maça"]:
            nome = "Maçã"
        else:
            nome = nome_bruto

        contagem[nome] = contagem.get(nome, 0) + 1
        texto = f"{nome} ({contagem[nome]})"
        cv2.rectangle(imagem_bgr, (x1, y1), (x2, y2), (0, 200, 0), 2)
        cv2.putText(imagem_bgr, texto, (x1, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 200, 0), 1)

    detalhes = {}
    total_kcal = total_prot = total_carb = total_gord = 0

    for fruta, qtd in contagem.items():
        dados = info_nutricional.get(fruta)
        if dados:
            subtotal = {
                "qtd": qtd,
                "kcal": dados["kcal"] * qtd,
                "prot": round(dados["prot"] * qtd, 1),
                "carb": round(dados["carb"] * qtd, 1),
                "gord": round(dados["gord"] * qtd, 1)
            }
            detalhes[fruta] = subtotal
            total_kcal += subtotal["kcal"]
            total_prot += subtotal["prot"]
            total_carb += subtotal["carb"]
            total_gord += subtotal["gord"]

    resumo = {
        "detalhes": detalhes,
        "totais": {
            "kcal": total_kcal,
            "prot": total_prot,
            "carb": total_carb,
            "gord": total_gord
        }
    }

    

    return imagem_bgr, resumo
