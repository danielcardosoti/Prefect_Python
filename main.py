from prefect import flow, task
import subprocess


# Task para executar o script PowerShell Instegração ISI
@task
def run_powershell_script(script_path: str):
    try:
        # Comando para executar o PowerShell
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Retorna a saída do script PowerShell
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Captura e registra erros
        return f"Erro ao executar o script PowerShell: {e.stderr}"


# Flow principal
@flow
def execute_script_powershell():
    script_path = r"C:\Scripts\Script_Transfer_ISI.ps1"  # Caminho do script PowerShell
    output = run_powershell_script(script_path)
    print("Saída do script PowerShell:")
    print(output)


if __name__ == "__main__":
    execute_script_powershell.serve()
