from google import genai
from pathlib import Path


client = genai.Client(api_key="AIzaSyD2YqIHUQ-1VZP3UhPEX_pSU6ZVdk8GR5w")

# Paths
VAULT_PATH = Path(r"C:\Users\MR Soltions\Desktop\AI_Employee_Vault")
DASHBOARD = VAULT_PATH / "Dashboard.md"

def update_dashboard():
    try:
        
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents="System Status Check: I am an AI Employee. Write 'AI Employee is Online and Connected' in one sentence."
        )

        
        with open(DASHBOARD, "a", encoding="utf-8") as f:
            f.write(f"\n- [AI Activity Log]: {response.text}")
        
        print("--- Success! ---")
        print("Obsidian Dashboard update ho gaya hai.")
        print(f"Likha gaya: {response.text}")
        
    except Exception as e:
        print(f"Masla abhi bhi hai? Error Details: {e}")

if __name__ == "__main__":
    update_dashboard()
