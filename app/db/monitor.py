import time
from db.connection import execute_select

def monitorar(intervalo_segundos=60 ):
    print("Monitoramento iniciado...1")
    snapshot_anterior = None 

    while True:
        snapshot_atual = execute_select()
        # if not bool(snapshot_atual):

        if snapshot_atual is False:
            print("Erro consulta DB")

        elif snapshot_anterior is None:
            print(f"Estado inicial carregado — {len(snapshot_atual)} registro(s).")
            snapshot_anterior = snapshot_atual
        else:
            for row_atual in snapshot_atual:
                row_anterior = next((r for r in snapshot_anterior if r["ID"] == row_atual["ID"]), None)

                if row_anterior is None:
                    continue

                val_anterior = row_anterior["Status_Processamento"]
                val_atual = row_atual["Status_Processamento"]

                if val_anterior != val_atual:
                    print(f"🔄 Alteração detectada — ID {row_atual['ID']}: '{val_anterior}' → '{val_atual}'")

            if snapshot_atual == snapshot_anterior:
                print("Nenhuma alteração detectada.")

            snapshot_anterior = snapshot_atual

        time.sleep(intervalo_segundos)
