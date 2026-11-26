# Калькулятор ипотеки — CI/CD (ПР №3)

Учебный проект по практической работе «Настройка CI/CD».

## Состав

- `calculator.py` — расчёт ежемесячного аннуитетного платежа.
- `calculator_gui.py` — десктопный интерфейс на tkinter.
- `app.py` — веб-интерфейс для продуктового контура (порт 8000).
- `test_calculator.py`, `test_app.py` — тесты pytest.
- `.github/workflows/ci.yml` — пайплайн GitHub Actions.

## Пайплайн

`push` в `main` запускает:

1. **Lint (flake8)** — проверка стиля кода.
2. **Tests (pytest)** — 7 тестов расчётов и веб-интерфейса.
3. **Docker build** — сборка образа и прогон тестов внутри контейнера.
4. **Deploy** — публикация кода в `/opt/mortgage-calculator` на продуктовом
   контуре и перезапуск контейнера на порту 8000.

Все job'ы выполняются на self-hosted runner'е, установленном на продуктовой
виртуальной машине (Ubuntu, Docker).

## Локальный запуск

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -v
.venv/bin/python app.py      # http://localhost:8000
```
