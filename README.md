# Insider Career Flow Test

Selenium + pytest ile yazılmış UI otomasyon projesi.

> CI/CD pipeline demo PR.

## Kurulum

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Çalıştırma

```bash
pytest tests/ -v
```

Headless modda çalıştırmak için:

```bash
HEADLESS=true pytest tests/ -v
```
