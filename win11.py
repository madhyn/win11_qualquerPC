import winreg

def criar_chave_registro():
    """Windows 11 em qualquer PC!"""
    try:
        # Verifique permissões administrativas
        chave = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\Setup\LabConfig")

        # Criar valores DWORD
        winreg.SetValueEx(chave, "BypassTPMCheck", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(chave, "BypassSecureBoot", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(chave, "BypassRAMCheck", 0, winreg.REG_DWORD, 1)

        # Fechar chave
        winreg.CloseKey(chave)
        print("Chaves de registro criadas com sucesso!")
    except PermissionError as e:
        print(f"Erro: {e}. Execute como administrador.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    criar_chave_registro()
