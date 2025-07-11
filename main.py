import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from detector import detectar_frutas, info_nutricional

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class AplicativoFrutas(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Detector de Frutas")
        self.geometry("1100x700")
        self.minsize(950, 550)

        self.entradas_quantidade = {}
        self.rotulos_frutas = {}
        self.rotulo_total = None
        self._foto_ref = None

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)

        self.quadro_imagem = ctk.CTkFrame(self, corner_radius=15)
        self.quadro_imagem.grid(row=0, column=0, sticky="nsew", padx=(30, 10), pady=30)

        self.rotulo_imagem = ctk.CTkLabel(self.quadro_imagem, text="Selecione uma imagem", anchor="center")
        self.rotulo_imagem.pack(expand=True, fill="both", padx=15, pady=15)

        self.quadro_info = ctk.CTkFrame(self, corner_radius=15)
        self.quadro_info.grid(row=0, column=1, sticky="ns", padx=(10, 30), pady=30)

        self.botao_selecionar = ctk.CTkButton(
            self.quadro_info,
            text="Selecionar Imagem",
            font=("Segoe UI", 16, "bold"),
            command=self.carregar_imagem,
            height=45,
            corner_radius=10
        )
        self.botao_selecionar.pack(pady=(20, 15), padx=20)

        self.painel_info = ctk.CTkScrollableFrame(self.quadro_info, width=300, height=500, corner_radius=10)
        self.painel_info.pack(padx=20, pady=(0, 20), fill="both", expand=True)

    def carregar_imagem(self):
        caminho = filedialog.askopenfilename(
            title="Escolher Imagem",
            filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png")]
        )
        if not caminho:
            return

        imagem = cv2.imread(caminho)
        imagem_com_anotacoes, resultado = detectar_frutas(imagem)

        imagem_rgb = cv2.cvtColor(imagem_com_anotacoes, cv2.COLOR_BGR2RGB)
        imagem_pil = Image.fromarray(imagem_rgb)
        imagem_pil.thumbnail((700, 600))
        self._foto_ref = ImageTk.PhotoImage(imagem_pil)
        self.rotulo_imagem.configure(image=self._foto_ref, text="")

        for widget in self.painel_info.winfo_children():
            widget.destroy()
        self.entradas_quantidade.clear()
        self.rotulos_frutas.clear()

        if resultado:
            for fruta, info in resultado["detalhes"].items():
                bloco = ctk.CTkFrame(self.painel_info, corner_radius=8)
                bloco.pack(padx=5, pady=8, fill="x")

                ctk.CTkLabel(bloco, text=fruta, font=("Segoe UI Semibold", 16)).pack(anchor="w", padx=10, pady=(8, 2))

                quadro_qtd = ctk.CTkFrame(bloco, fg_color="transparent")
                quadro_qtd.pack(anchor="w", padx=10, pady=2, fill="x")
                ctk.CTkLabel(quadro_qtd, text="Quantidade:", font=("Segoe UI", 14)).pack(side="left")
                entrada = ctk.CTkEntry(quadro_qtd, width=50)
                entrada.insert(0, str(info["qtd"]))
                entrada.pack(side="left", padx=(5, 0))
                entrada.bind("<FocusOut>", lambda e, f=fruta: self.atualizar_totais())
                entrada.bind("<Return>", lambda e, f=fruta: self.atualizar_totais())
                self.entradas_quantidade[fruta] = entrada

                quadro_nutri = ctk.CTkFrame(bloco, fg_color="transparent")
                quadro_nutri.pack(anchor="w", padx=10, pady=2, fill="x")

                rot_kcal = ctk.CTkLabel(quadro_nutri, text=f"Calorias: {info['kcal']} kcal", font=("Segoe UI", 14))
                rot_kcal.pack(anchor="w")
                rot_prot = ctk.CTkLabel(quadro_nutri, text=f"Proteína: {info['prot']} g", font=("Segoe UI", 14))
                rot_prot.pack(anchor="w")
                rot_carb = ctk.CTkLabel(quadro_nutri, text=f"Carboidratos: {info['carb']} g", font=("Segoe UI", 14))
                rot_carb.pack(anchor="w")
                rot_gord = ctk.CTkLabel(quadro_nutri, text=f"Gorduras: {info['gord']} g", font=("Segoe UI", 14))
                rot_gord.pack(anchor="w")

                self.rotulos_frutas[fruta] = {
                    "kcal": rot_kcal,
                    "prot": rot_prot,
                    "carb": rot_carb,
                    "gord": rot_gord
                }

            self.rotulo_total = ctk.CTkLabel(self.painel_info, text="", font=("Segoe UI", 16, "bold"))
            self.rotulo_total.pack(pady=(15, 5))
            self.atualizar_totais()
        else:
            ctk.CTkLabel(self.painel_info, text="Nenhuma fruta detectada!", font=("Segoe UI", 15)).pack(pady=20)

    def atualizar_totais(self):
        total_kcal = total_prot = total_carb = total_gord = 0

        for fruta, entrada in self.entradas_quantidade.items():
            try:
                qtd = int(entrada.get())
            except:
                qtd = 0
            unidade = info_nutricional.get(fruta)
            if unidade:
                kcal = unidade["kcal"] * qtd
                prot = unidade["prot"] * qtd
                carb = unidade["carb"] * qtd
                gord = unidade["gord"] * qtd

                total_kcal += kcal
                total_prot += prot
                total_carb += carb
                total_gord += gord

                self.rotulos_frutas[fruta]["kcal"].configure(text=f"Calorias: {kcal} kcal")
                self.rotulos_frutas[fruta]["prot"].configure(text=f"Proteína: {prot:.1f} g")
                self.rotulos_frutas[fruta]["carb"].configure(text=f"Carboidratos: {carb:.1f} g")
                self.rotulos_frutas[fruta]["gord"].configure(text=f"Gorduras: {gord:.1f} g")

        if self.rotulo_total:
            self.rotulo_total.configure(
                text=f"{int(total_kcal)} kcal | {total_prot:.1f}g P | {total_carb:.1f}g C | {total_gord:.1f}g G"
            )

if __name__ == "__main__":
    app = AplicativoFrutas()
    app.mainloop()
 