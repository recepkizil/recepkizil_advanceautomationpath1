# Insider Career Flow Test

Selenium + pytest ile yazılmış UI otomasyon projesi.

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

## CI/CD Pipeline

Bu repo, GitHub Actions üzerinde çalışan bir UI test pipeline'ı içerir ([.github/workflows/ui-tests.yml](.github/workflows/ui-tests.yml)).

- **Tetikleyici:** `main` branch'ine açılan her pull request'in oluşturulması veya üzerine yeni commit push edilmesi (`opened`, `synchronize`, `reopened`).
- **Adımlar:** Bağımlılıkların kurulması, Chrome kurulumu, testlerin headless modda çalıştırılması.
- **Raporlama:** Her çalıştırma sonunda `reports/` klasörü (HTML test raporu, JUnit XML ve başarısız testlerin ekran görüntüleri) GitHub Actions "Artifacts" bölümüne yüklenir ve indirilebilir.

### Test sonuçlarını PR için zorunlu kontrol (required check) yapma

1. GitHub'da repo → **Settings → Branches**.
2. `main` branch'i için bir **branch protection rule** ekleyin (veya mevcut olanı düzenleyin).
3. **Require status checks to pass before merging** seçeneğini işaretleyin.
4. Açılan listeden `ui-tests` check'ini seçin (en az bir workflow çalıştıktan sonra listede görünür).
5. Kaydedin. Bundan sonra bu check geçmeden PR merge edilemez.
